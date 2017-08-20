# Repository with code for my django tutorial :

Python version: 3.6.1
Django version: 1.11.3

[link to playlist](https://www.youtube.com/watch?v=C90bAExJBd8&list=PLPRsICSqu9FoOpFyr8dlfLh9_n4nt_05u)

### Setup
Use git to clone the repository OR download it in zip in link above.
```
git clone https://github.com/rusnano0/dyt.git
```
Use pip to install requirements from requirements.txt
```
pip install -r requirements.txt
```
### Launch
To launch the server use this command
```
python manage.py runserver
```
Check it out on: ```http://127.0.0.1:8000/```

### Admin
```http://127.0.0.1:8000/admin```

use this to go to admin section
```
login: admin
password: admin1234
```

or create your own superuser
```
python manage.py createsuperuser --username=joe --email=joe@example.com
```

### Search
```http://127.0.0.1:8000/search/```

### Live HashTag Search
```http://127.0.0.1:8000/search/hashtag```

### Login and Logout URLs
```
http://127.0.0.1:8000/login
http://127.0.0.1:8000/login

```