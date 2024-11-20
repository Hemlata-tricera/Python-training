# Django installation - Installing an official release via pip

 # py -m pip install Django

""" Verifying
1.To verify that Django can be seen by Python, type python from your shell. Then at the Python prompt, try to import Django:

>>> import django
>>> print(django.get_version())
5.1.3

OR
2.On command prompt-You can tell Django is installed and which version by running the following command in a shell prompt-
(indicated by the $ prefix):
...\> py -m django --version

CREATING A PROJECT-
Once Django is installed, you can create a new project using the django-admin command.Follow these steps:
1. Navigate to the directory where you want to create your project:
..\>mkdir djangolearning
Open a terminal or command prompt and use the cd command to change to the desired directory.

2. Create the project: Run the following command to create a new Django project. Replace mysite with your desired project name:
../>django-admin startproject mysite djangolearning
This will create a project called mysite inside the djangotutorial directory.


3. Navigate to your project directory: Once the project is created, navigate into the project directory:
../> cd mysite

4. Run the development server: Django comes with a built-in web server for development purposes. You can start it by running:
../> python manage.py runserver
OR

../> py manage.py runserver

By default, this will start the server on http://127.0.0.1:8000/. Open this URL in your browser,
and you should see the Django welcome page, indicating that the server is running successfully.

4. Structure of a Django Project
A typical Django project contains the following structure:

mysite/
    manage.py           # Script to manage your project (runserver, migrations, etc.)
    mysite/          # Main project directory (same name as the project)
        __init__.py     # Marks this directory as a Python package
        settings.py     # Configuration file for your project
        urls.py         # URL routing configuration
        asgi.py         # ASGI configuration (for async deployment)
        wsgi.py         # WSGI configuration (for traditional deployment)


5. Run Your Project
To make sure everything is set up correctly, visit http://127.0.0.1:8000/
in your web browser after running the server. You should see the Django welcome page.

"""

