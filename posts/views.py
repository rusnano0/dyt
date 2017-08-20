from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
import json

# Create your views here.
from django.http import HttpResponse
from django.views import View
from .models import Post, HashTag
from user_profile.models import User
from posts.forms import PostForm, SearchForm, SearchTagForm

class Index(View):

    def get(self, request):
        context = {'text': 'Hello, world!'}
        print(context)
        return render(request, 'base.html', context)

class Profile(View):
    """ User Profile Page url: 127.0.0.1:8000/user/<username> """

    def get(self, request, username):
        user = User.objects.get(username=username)
        posts = Post.objects.filter(user=user)
        form = PostForm()
        context = {
            'posts' : posts,
            'user' : user,
            'form' : form,
        }
        return render(request, 'profile.html', context)

class PostPost(View):
    """Create Post View"""
    def post(self, request, username):
        form = PostForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            post = Post(text = form.cleaned_data['text'], user = user)
            post.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word.startswith('#'):
                    hash_tag, created = HashTag.objects.get_or_create(name=word)
                    hash_tag.post.add(post)
        return HttpResponseRedirect('/user/'+username)

class Search(View):
    """ Search all posts url: 127.0.0.1:8000/search/?q=<q>"""

    def get(self, request):
        form = SearchForm()
        context = {'search' : form}
        return render(request, 'search.html', context)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['q']
            posts = Post.objects.filter(text__icontains=q)
            context = {'q' : q, 'posts' : posts}
            return_str = render_to_string ('part_views/_post_search.html', context)
            return HttpResponse(json.dumps(return_str), content_type='application/json')
        else:
            HttpResponseRedirect("/search/")

class SearchTag(View):
    """ Search tags with autocomplete (live search) """

    def get(self, request):
        form = SearchTagForm()
        context = {'searchtag' : form}
        return render(request, 'search_tags.html', context)

    def post(self,request):
        q = request.POST['q']
        form = SearchTagForm()
        tags = HashTag.objects.filter(name__icontains=q)
        context = {'tags' : tags, 'searchtag' : form}
        return render(request, 'search_tags.html', context)

class TagJson(View):
    """ Search tags with autocomplete (live search) json data"""
    def get(self, request):
        q = request.GET.get('q', '')
        taglist = []
        tags = HashTag.objects.filter(name__icontains=q)
        for tag in tags:
            new = {'q' : tag.name, 'count' : int(len(tag.post.all()))}
            taglist.append(new)
        return HttpResponse(json.dumps(taglist), content_type="application/json")


















