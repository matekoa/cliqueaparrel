# Clique Apparel

E-Commerce Website To Sell Clothing.

## Learning
| Frameworks | |
| --- | --- |
| Front End | Vue |
| Back End | Django |

## Features & Concepts

- Sign Up & Registeration
- Payment Integration
- Database Management


## Installed Packages

### Backend

1 Running On VirtualEnv
2 Latest Version of Django (4.1) installed in venv
3 Django Rest Framework
4 Django-Cors-Headers
5 Djoser
6 Pillow
7 Stripe

## FrontEnd (Vue)
1. Vue
2. Axios
3. Bulma

### 5 Djoser
- Handles Users and user authentication.
- Can Create Users and get authorisation tokens.

### 6 Pillow
- Resizing images (i.e image optimization)

### 7 Stripe
- Payment Gateway. To accept transactions

## Initializing Databases

python manage.py makemigrations

-Create super user
python manage.py createsuperuser

## Run Server
python manage.py runserver

## Install Vue CLI
npm install -g @vue/cli

## Install Axios
-Packages used to communicate to backend

## Install Bulma (can also use bootstrap)
- CSS Framework

## Add Font Awesome
Add to index.html in Vue directory
<link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">

## Creating Apps for the project.
E.g Products:
-python manage.py startapp products
