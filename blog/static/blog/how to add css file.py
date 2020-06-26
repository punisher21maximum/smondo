#how to add url name in .html
#create super user 
^C(venv) gaurav7x7@ubuntu:~/workspace/ConviMax3/weworkout$ python3.6 manage.py createsuperuser
Username (leave blank to use 'gaurav7x7'): vishal
Email address: vishal7x7@gmail.com
Password: 
Password (again): 
Superuser created successfully.
(venv) gaurav7x7@ubuntu:~/workspace/ConviMax3/weworkout$ 
#to view the sql code of migrations you have run
(venv) gaurav7x7@ubuntu:~/workspace/ConviMax3/weworkout$ python3.6 manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
#creating model(Post model) objects in django shell
(venv) gaurav7x7@ubuntu:~/workspace/ConviMax3/weworkout$ python3.6 manage.py shell
>>> from blog.models import Post
>>> from django.contrib.auth.models import User

>>> User.objects.all()
<QuerySet [<User: vishal>]>
>>> User.objects.filter(username='vishal').first()
<User: vishal>


>>> u = User.objects.filter(username='vishal').first()
>>> post_1 = Post(title='fitness', content='first post content', author = u)
or
>>> post_1 = Post(title='fitness', content='first post content', author_id = u.id)#by uder id
>>> post_1.save()
>>> Post.objects.all()
<QuerySet [<Post: fitness>]>




# how to add css file

step1 : where to store main.css
blog/
	static/
		blog/
			main.css 

step2 : write code in main.css 

step3 : how to load main.css file in base.html 

1)at top load static folder : {{load static}}

2)in head add main.css : 
    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

#main blog
#1 - get started with django
step1 : create new project
$ django-admin startproject weworkout // name of website
s2 : go to weworkout dir
$ cd weworkout
s3 : run website
$ python3.6 manage.py runserver
s4 : go to browser at localhost or 127.0.0.1
#2 get started with your webpage
s1 : create a new app
$ python3.6 manage.py startapp blog
s2 : include app in weworkout/settings.py 
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
	...
]
s3 : create view in blog/views.py 

# start : 
step1 : 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

