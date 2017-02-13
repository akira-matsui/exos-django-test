# EXOS Django Test

## 1. Prerequirements
  Python 3.4 or later, Pip, Virtualenv is required to run this project.
  To install python 3.4, you can use Simple Python Version Management: pyenv.
  You can refer this link https://anil.io/blog/python/pyenv/using-pyenv-to-install-multiple-python-versions-tox/

## 2. Steps to run project
   - clone repo to your local using command `git clone https://github.com/akira-matsui/exos-django-test.git`
   - In the same level with repository directory, create virtual environment using command `virtualenv testenv`
   - Activate virtual environment using command `source testenv/bin/activate`
   - Go to django project root folder using command `cd exos-django-test`
   - Install Django framework using command `pip install -r requirements.txt`
   - Make migration file using command `python manage.py makemigrations`
   - Now run `python manage.py migrate` to create table in SQLite database.
   - Run server using command `python manage.py runserver`  
      `Performing system checks...`  

      `System check identified no issues (0 silenced).`  
      `Django version 1.10.5, using settings 'exostest.settings'`  
      `Starting development server at http://127.0.0.1:8000/`  
      `Quit the server with CONTROL-C.`  
## 3. Screenshots
  ![Alt text](/screenshots/user-list.png?raw=true "User list")  
  ![Alt text](/screenshots/user-create.png?raw=true "Create User")  
  ![Alt text](/screenshots/user-edit.png?raw=true "Edit User")  
  ![Alt text](/screenshots/csv.png?raw=true "Export to csv file")  
