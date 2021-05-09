<p align="center">
    <a href="/">
        <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build" />
    </a>
    <a href="https://www.djangoproject.com/">
        <img src="https://img.shields.io/badge/django-2.0-blue.svg" alt="django" />
    </a>
    <a href="https://getbootstrap.com/">
        <img src="https://img.shields.io/badge/bootstrap-4.0-orange.svg" alt="Bootstrap" />
    </a>
    <a href="https://github.com/mahmudahsan/pythonbangla.com/blob/master/LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License" />
    </a>
</p>

# Students marks information system
A content management system that is used to store the marks of students and maintain it. Instructors can store and edit the marks under their courses, while students can view the marks marks and sgpa of specific semester, and also their overall cgpa.

## Usage

# Table of Contents
- [Technology Used](#technology-used)
- [Features](#features)
- [Setup in local machine](#setup-in-local-machine)
- [Configuration](#configuration)
- [Operation](#operation)
- [Folder Structures](#folder-structures)

### Technology Used
1. [Django](https://www.djangoproject.com/)
2. [HTML]()
3. [CSS]()
4. [JS]()
5. [Bootstrap](https://getbootstrap.com/)
6. [MySQL](https://www.mysql.com)

## Features


## Setup in local machine

Let assume our project name will be djangodemo

1. First clone this project or fork and clone your fork url
```shell
git clone https://github.com/Akhileshkumar-12/marks-management-system.git
cd marks-management-system # Enter the project dir
```

2. Now run and install django by [pipenv](http://thinkdiff.net/python/python-official-pipenv-packaging-tool-for-virtualenv-and-pip-in-mac-and-windows/)

```shell
pipenv install django
pipenv shell # Activate pipenv
```
3. Start django server locally
```shell
python3 manage.py runserver
```
4. Visit http://127.0.0.1:8000/ in a web browser.
5. Quit the server with CONTROL-C in terminal

## Configuration
## Operation
## Folder Structures
```
├───marksManagement
│   ├───button
│   └───navbar    
├───marks_management_system
├───static
├───templates
│   ├───dashboard
│   ├───favicon
│   └───report_card    
├───db.sqlite3    
├───manage.py
```
## Project Notes
## Design Notes
## Credits
