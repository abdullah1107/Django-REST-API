
## Django Rest Api


### Environment setup

First of all create a virtual environment by using command or anaconda (if installed)

### source activate virtualenvironment

1. (djangoenv)Muhammads-MacBook-Pro:library_project muhammadabdullahalmamun$

(djangoenv) Mylocal_Directory$

2.install necessary python packages don't forget to install djangorestframework

3.(djangoenv)Muhammads-MacBook-Pro:Desktop muhammadabdullahalmamun$ mkdir projectFolderName && cd projectFolderName

4.(djangoenv)Muhammads-MacBook-Pro:projectFolderName muhammadabdullahalmamun$django-admin startproject projectName

#### want a superuser for this project and app like (admin)

(djangoenv)Muhammads-MacBook-Pro:projectFolderName muhammadabdullahalmamun$ python manage.py createsuperuser

#### if i using an app for the project then using this command

5.(djangoenv)Muhammads-MacBook-Pro:Desktop muhammadabdullahalmamun$ python manage.py startapp appName

#### after model setup then migration this model

6.(djangoenv)Muhammads-MacBook-Pro:projectFolderName muhammadabdullahalmamun$ python manage.py makemigrations

7.(djangoenv)Muhammads-MacBook-Pro:projectFolderName muhammadabdullahalmamun$ python manage.py migrate


#### For running the server

8.(djangoenv)Muhammads-MacBook-Pro:projectFolderName muhammadabdullahalmamun$ python manage.py runserver
