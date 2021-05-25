# [Project Bixert](https://bixert.xyz/)

## Packages used 
- [Django](https://www.djangoproject.com/)
- [CKeditor](https://ckeditor.com/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [Numpy](https://numpy.org/)

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
