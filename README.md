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

[Student marks information sytem](http://sudha6567kumari.pythonanywhere.com/) - For Students

# Table of Contents
- [Technology Used](#technology-used)
- [Features](#features)
- [Setup in local machine](#setup-in-Local-Machine)
- [Operation](#operation)
- [Folder Structures](#folder-structures)
- [Screen shots](#screen-shots)

### Technology Used
1. [Django](https://www.djangoproject.com/)
2. [HTML]()
3. [CSS]()
4. [JS]()
5. [Bootstrap](https://getbootstrap.com/)
6. [SQLite3](https://www.sqlite.org)

## Features
1. Admin Student accounts by the Admin.
2. Add and managing marks of students by Admin.
3. Viewing a compiled reportcard by the Student.

## Setup in Local Machine

1. First clone this project or fork and clone your fork url
```shell
git clone https://github.com/Akhileshkumar-12/marks-management-system.git
cd marks-management-system # Enter the project dir
```

2. Install [django](https://www.djangoproject.com/)
```shell
pip install django
```
3. Start django server locally
```shell
python3 manage.py runserver
```
4. Visit http://127.0.0.1:8000/ in a web browser.
5. Quit the server with CONTROL-C in terminal

## Operation
### 1. Create a SuperUser(Admin)
1. Call the following command to create the superuser. You will be prompted to enter a username, email address (optional) , and strong password.
 ```shell
 python3 manage.py createsuperuser
 ```
 2. Run the django server locally.
  ```shell
 python3 manage.py runserver
 ```
 3. Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) in a web browser.
    
4. Login with the credentials you used to create the account.

### 2. Navigating django Admin site
**![](https://lh3.googleusercontent.com/X7i9rJx7fp1guXtkj4Mcu0qwaD8yDvrXOvGu3Y4cibMXqdM1k5brQR0XLdPf3lGbvRlHJlM-qfvQ_rexjbM2Ui5dKJeBRvb1ArnyRxTX98L6Ag3qat_-CWR-nd7jiMz2KiNObJ_w)**
#### 2.1 Creating Faculty Accounts:
1.  After logging in, on the navigation bar on the left select ‘Facultys’.
2.  On the top right click on the ‘Add Faculty’ to start adding the user.(As Highlighted)
3.  Here the credentials, such as Id, password, name, subject name, subject code and credits of subject, of the Faculty can be added.    
4.  After which, select one of the save options in the bottom right.
#### 2.2 Creating Student Accounts:
1.  After logging in, on the navigation bar on the left select ‘Students’. 
2.  On the top right click on the ‘Add Student’ to start adding the user.(Similar to what is shown above.)
3.  Here the credentials, such as roll number, password and name, of the Student can be added.
4.  After which, select one of the save options in the bottom right.
#### 2.3 Attaching Student to a Subject:
1.  After logging in, on the navigation bar on the left select ‘Subjects’.
2.  On the top right click on the ‘Add Subject’.(Similar to what is shown above.)
3.  Fill in the roll number of the Student, Subject name and code.
4.  After which, select one of the save options in the bottom right.
#### 2.4 Adding SGPA:
1.  After logging in, on the navigation bar on the left select ‘Sem_grades’.
2.  On the top right click on the ‘Add Sem_grade’.(Similar to what is shown above.)
3.  Fill in the roll number of the Student, semester, sgpa and total credits in that semester.
4.  After which, select one of the save options in the bottom right.
### 3. Navigating django Admin site
**![](https://lh3.googleusercontent.com/TtmlF1brjy_NyXFpnQh_Y3Z9GvLTDSxNkoPjTsU1w177aB29iKCNadWKDd1QvAefdtsFxkkxcDwseHHX6U-jAjdGEmqfdj7-gfhge3XdQip0xnYGsQqsxD9c-aamv3jgdnVUMbhW)**
#### 3.1 Student Side:
1.  Select ‘Student’ as the option in the Login Page.
2.  Login using the id and password for the Student account. Login using your respective (credentials) id ,password
3.  After logging in, using the Navigation Bar on the left of the website you can navigate between the Dashboard and the Report Card.
4.  In the dashboard you can hover over the points on the graph to view your GPA per semester.
5.  Here you can view a more detailed list of information on the marks obtained in a subject.
6.  You can select the subject you wish to view from the tab above the table.
#### 3.2 Faculty Side:
1.  Select ‘Faculty’ as the option in the Login Page.
2.  Login using the id and password for the Faculty account.
3.  After logging in, here a tabulated view of the marks of the student are displayed.
4.  Clicking on the ‘Modify’ button in the bottom right corner will expand a form on top.
5.  In this form you can modify the marks of the students.
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
## Screen shots
**![](https://lh6.googleusercontent.com/XxRP7l3E5-b4rA_piP-G4PQx6q65lLYNAecVgI1Re3RkbEf40h-AK7KeWdp-pC2fRAKxEYsI2daIff6MtuIoDmQ4ynCRMmvkepgChoMzLKxumfynv4vq11-p07zPxwQBY8-PIZ-q)**
**![](https://lh3.googleusercontent.com/oDWNsLYPpgPhfptm-xT6wDjdB-66pIemjDpdRzvVvhAbwWSTeQLsGQvYbD9jbAO3fzzb7UGNwg9dEqrz2X0Io7Ltk0k_DOPwsJhvDowPAJxaaAEVVmDB47NxhvEzAnQQjeYw_xz7)**

