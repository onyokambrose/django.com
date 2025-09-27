import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.db import models
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY='a-random-secret-key',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    INSTALLED_APPS=[
       "django.contrib.admin"
    
         "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",

        "django.contrib.messages",
        "django.contrib.staticfiles",
        __name__,
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    }],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    STATIC_URL='/static/',
)
import django
django.setup()
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class postForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'content']
            def home(request):
                posts = Post.objects.all().
                <doctype html>
html>
<head>
    <title>My Blog</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-4">My Blog</h1>
        <a href="/new/" class="btn btn-primary mb-4">New Post</a>
        {% for post in posts %}
            <div class="card mb-4">
                <div class="card-body">
                    <h2 class="card-title
">{{ post.title }}</h2>
                    <p class="card-text">{{ post.content }}</p>
                    <p class="card-text"><small class="text-muted">Posted on {{ post.created_at }}</small></p>
                </div>
            </div>
        {% empty %}
            <p>No posts yet.</p>
        {% endfor %}
    </div>
                return render(request, 'home.html', {'posts': posts})
            def new_post(request):
                if request.method == 'POST':
                    form = PostForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect('home')
                else:
                    form = PostForm()
                return render(request, 'new_post.html', {'form': form})
            urlpatterns = [
                path('', home, name='home'),
                path('new/', new_post, name='new_post'),
            ]
            if __name__ == "__main__":
                execute_from_command_line(sys.argv)
                </body>
</html>
"""
from django.template import engines
template_engine = engines['django'].from_string(html)
return HttpResponse(template_engine.render(context, request))
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {'form': form}
    html = """
<!doctype html>

<html>
<head>
    <title>Create Post</title>
</head>
<body>
    <h1>Create Post</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>
"""
from django.template import engines
template_engine = engines['django'].from_string(html)
return HttpResponse(template_engine.render(context, request))
urlpatterns = [
    path('', home, name='home'),
    path('new/', create_post, name='create_post'),
]
if __name__ == "__main__":
    execute_from_command_line(sys.argv)