# [Project Bixert](https://bixert.xyz/)

## Packages used 
- [Django](https://www.djangoproject.com/)
- [CKeditor](https://ckeditor.com/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [Numpy](https://numpy.org/)

## Technologies We used
![](https://img.shields.io/badge/DJANGO-5da673?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/sklearn-ed9437?style=for-the-badge&logo=scikit-learn&logoColor=white)
![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![](https://img.shields.io/badge/FireBase-3997de?style=for-the-badge&logo=firebase&logoColor=f6be0f)


## How to Run locally

- ### Cloning and creating virtual env
  - Clone this repo - `git clone https://github.com/rawho/bixert`
  - Move to the cloned repo - `cd bixert`
  - Create a virtual environment - [help](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
  - install all the packages - `pip install -r requirements.txt`
- ### Creating Database
  - install mysql - [help](https://www.javatpoint.com/how-to-install-mysql)
  - Create a user by entering to the mysql shell- `CREATE USER 'bixert'@'localhost' IDENTIFIED BY 'Bixert@123';`
  - `CREATE DATABASE bixert;`
- ### migrating and running
  - `python manage.py migrate`
  - `python manage.py runserver` - Head over to http://localhost:8000 and see the magic 

