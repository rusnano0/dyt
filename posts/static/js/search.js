/**
 * Created by vevoj on 06.08.2017.
 */

$('#search-form').submit(function(e) {
    $.post('/search/', $(this).serialize(), function(data) {
        $('.posts').html(data);
    });
    e.preventDefault();
});
