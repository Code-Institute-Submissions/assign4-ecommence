# Code Institute Full Stack Frameworks with Django

# BooksTreasureProject E-Commerce Website

## Project Objectives
This website serves the purpose for user who with authenticated account doing online Classic Books purchases beside visit the shop.
With technologies available nowadays, users can purchase any item with just some simple touch on mobile. Aside from the others book ecommences 
website, user can drop an email if choice of books not available on the website for owner to arrange the purchase item available online.
A new user could register for a new account, login, change or reset a password, view his/her profile and logout. 
The user could also search for books by title or author name.
A logged in superuser has advantage books CRUD rights which allow him/her to add a books/authors, edit the books/authors's data and even delete it from the database.

Please register as a new user or use the following accounts to navigate the website:

To log in as a user without game CRUD rights, please use the following:

Username: vapal14749@banetc.com
Password: asd1234567
To log in as a user with game CRUD rights, please use the following:

Username: admin
Password: sky760131


## Deployed Link
The deployed website can be found [here](https://ecommence-books.herokuapp.com/)

## UX/UI
### Overview and Colour
The layout of this website is choosen based on illustrations ideas to give customers an attractive webpage.
Which aside from mostly ecommence website, the idea of choose image and color is to give customer refreshing look while browsing the page.
The name of the website as its meaning "treasure classic books", and its purpose for provides all the treasure classic books over the years
can still be purchased and collect by all classic book lovers.
Image of illustrations was purposely placed in certain position and size of the page for the unique design effect for users.
Hence, this is not code error effect.
A clear and direct navbar for user easily recognized to click on the features.
Info such as user name and flash message for each success process complete will be display on top of the page.
This idea is provides user no need to scroll down the page to look for those info as the navbar was placed with fixed-top features.
Color that choosen provide comfortable view page to users while browsing important info on the webpage.
Title of the webpage tag along with the webpage content about.


## User Stories
### Basic User Stories
1. As a customer of the website, he/she will be able to direct to books catalog by just clicking on explore button on the homepage/or
    [Home](https://ecommence-books.herokuapp.com/) on the navbar. Besides that, popular books among the customer will be show on the home page as well.
2. As a user of the website, he/she should be able to search for the books available, either by a search on title keyword or by sorted from
   author name dropdown bar in the [Books](https://ecommence-books.herokuapp.com/books/all).
3. User can views the books more info by clicking on that book's "title" on the [Books](https://ecommence-books.herokuapp.com/books/all) page. 
   Highlighted info of the books such as author, price and add cart link are placed together with the list of books column. 
4. User can views the whole list of books available for purchase by scroll/swipe to the left.
5. User also can view list of author on [Authors](https://ecommence-books.herokuapp.com/books/all) tab on navbar. Furthermore, user will access author info 
   by clicking on the author name.
6. User can easy make purchase by clicking on the "add to cart" button from the list of books page [Books](https://ecommence-books.herokuapp.com/books/all) 
   or book details page [Views](https://ecommence-books.herokuapp.com/books/view/1/).
7. User can view their cart by clicking [Cart](https://ecommence-books.herokuapp.com/carts/view) before making payment or the cart icon on the right side of 
   the navbar with the cart icon image. The total item that have been added showed to user beside the cart icon.
8. User create the account with SignUp on the navbar.Once Signup and email verified, user can log in to the website with login.
   Upon successful login, the logout tab will be showed on navbar.
9. User can understand the company by clicking on [About us](https://ecommence-books.herokuapp.com/info/about_us/).
10. User can view company terms and conditions by clicking on [Terms and conditions](https://ecommence-books.herokuapp.com/info/terms_and_conditions/).
11. User can contact us by submit his/her request by clicking on [Contact Us](https://ecommence-books.herokuapp.com/info/contact_us/).

### Additional User Stories
1. User with superuser account(admin) can 
 a. add a book [add book](https://ecommence-books.herokuapp.com/books/create)
 b. add a author [add author](https://ecommence-books.herokuapp.com/books/authors/create)
 c. edit a book [edit book](https://ecommence-books.herokuapp.com/books/update/3)
 d. edit a author [edit author](hhttps://ecommence-books.herokuapp.com/books/authors/update/2)
 e. delete a book [delete book](https://ecommence-books.herokuapp.com/books/delete/3)
 f. delete a author [delete author](hhttps://ecommence-books.herokuapp.com/books/authors/delete/3)
## Wireframes

## E-Classic Books Shop Features
### Index/Home page

### Books page

### Authors Pages

### Cart Page

### Login/Logout/SignUp Page
* The account management pages are managed by Django-AllAuth


## Superuser additional access page 
### add a book Page

### add a author Pages



### NavBar Links

## Technologies Used
The technologies used for this project are:
1. [Django(Release 2.2.14)](https://www.djangoproject.com/start/overview/). Django is a Python Web Framework that encourages rapid
development and clean design. It is the main requirement of this project.
2. [Python(Release 3.8.3)](https://www.python.org/downloads/release/python-383/). Python is the programming language that Django 
is built on.
3. [HTML5](https://html.spec.whatwg.org/). HTML is the markup language that structures the webpage documents.
4. [CSS3](https://www.w3.org/TR/2001/WD-css3-roadmap-20010523/). Cascading style sheet is the language that presents and styles 
the HTML documents.
5. [Javascript and JQuery](https://developer.oracle.com/sg/javascript/). Javascript and Jquery is used primarily to do DOM 
manipulation and it is the main engine to serve interactivity and event handling to the webpages.
6. [Bootstrap (Release 4.5)](https://getbootstrap.com/docs/4.5/getting-started/introduction/). Bootstrap is the layout framework
used to organize the website's display.
7. [Gitpod](https://www.gitpod.io/)  
Gitpod is an online IDE that can be launched in Github. It is used to develop and write the code for this project.
8. [Git and Github](https://github.com/)  
Github is an online hosting service for software development that utilizes Git for version control.
9. [Stripe](https://stripe.com/en-sg). Stripe is a financial software service provider that provides the API for software developers
to integrate payment into their websites and mobile apps.
10. [Google Fonts](https://fonts.google.com/). Google Fonts Poppins (sans-serif) is used for headings. Google Fonts Bitter (serif)
is used for body and in paragraph tags. Google Font Delius Swash Caps is used in the navbar brand/logo name.
11. [Font Awesome](https://fontawesome.com/) Font Awesome Icons are used in this project to give illustrations to some edit and 
delete buttons.

### Django Libraries
1. [Django-AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html) is a Django Library that manages authentication, 
registration, account management as well as 3rd party (social) account authentication 
2. [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is Django package that provides DRY Django Forms.

### Database
The database used in the project is PostgreSQL. PostgreSQL is an open source Relational Database Management System that is similar
to MySQL but it has an object oriented database model which are directly supported in database schemas and query language.

### Database Structure
A UML diagram to illustrate the relationship between models is drawn and shown [here](https://github.com/Oraclebun/ci-fullstack-project4/blob/master/documents/UML.pdf)

## Testing
Due to the shortage in time, testing is for this project is done manually. The details of testing is documented in 
[Testing.md](https://github.com/skyeoh06/assign4-ecommence)

## Deployment
### Running the project locally.
This project is build using Gitpod.
The steps I went through to run the project locally are as follows:

1. Install the gitpod extensions for the local machine browser.
2. Sign up for a github account and login.
3. Sign up for a gitpod account and link it to github account.
4. Go to the personal github pages and start a new repository using the 
[Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)
5. The project folder will be available on the personal github page repository.
6. At the top right of the personal repository, there is a green coloured Gitpod button like the picture below:
![Gitpod Button](https://github.com/Oraclebun/ci-fullstack-project4/blob/master/documents/readme_images/Gitpod_link.png)
7. Click on the Gitpod link to open up the development environment for this project in Gitpod.
8. Once the project has fully loaded in the browser, a Visual Studio Code-like editor with a terminal will be seen.
9. In the Coding environment terminal, install the following requirements:  
    a. pip3 install django==2.2.14  
    b. pip3 install django-allauth  
    c. pip3 install django-crispy-forms
10. Set up the environment variables as follows:  
    a. Create a .env file  
    b. Create a .gitignore file to list the names of files to be omitted from git.  
    c. In the .env file, place the Django Secret Key, and the Stripe Publishable Key, Stripe Secret Key and Stripe Endpoint Secret.  
    d. The initial coding is done using SQLite. On deploy after obtaining the database url, the production database url is to be 
    inserted into the .env file too.
11. Generate the requirements.txt file with the following commands typed into the terminal:
```console
$ pip3 freeze --local > requirements.txt
```
12. Setting up Django  
a. To start a project, the following command is keyed into the terminal:
```console
$ django-admin startapp `<project_name>` .
```
b. To start a new app under this project, the following command is keyed into the terminal:
```console
$ django-admin startapp `<app_name>`
```
c. To setup the database programmatically via Django:
```console
$ python3 manage.py migrate
```
d. To create migration files for the database:
```console
$ python3 manage.py makemigrations
```
e. To create superuser:
```console
$ python3 manage.py createsuperuser
```

13. Data is populated manually via the admin interface or via the written codes, depending on the website design.  

14. Finally, the website pages are served by typing the below into the console:
```console
$ python3 manage.py runserver 8080
```

## Deployment on Heroku
1. Install the following dependencies via the terminal:
```console
$ pip3 install gunicorn
$ pip3 install psycopg2
$ pip3 install Pillow
$ pip3 install whitenoise
$ pip3 install dj_database_url
```

2. Add whitenoise to the middleware. White noise is for helping Django to serve static files in production.
```
MIDDLEWARE = [
.....
'whitenoise.middleware.WhiteNoiseMiddleware'
]
```

3. Sign up for Heroku account
4. Login Heroku in the terminal

```console
$ heroku login -i

```

5. Type in the below to create a heroku app, where `<the_name_of_the_project>` is the name of the project to be deployed.  

```console
$ heroku create <name_of_the_project>

```

6. then create a remote repository by typing in 

```console
$ git remote -v
```

7. Create a Procfile with the content "web gunicorn `<name of the project>`.wsgi:application
8. Update the allowed host in settings.py to the newly created heroku app domain name.
9. Freeze all project dependencies by keying in to the terminal 

```console
$ pip3 freeze --local > requirements.txt 
```
10. Add STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

11. Finally push the project to git as below:

```console
$ git add.
$ git commit -m <deployment message>
$ git push heroku master
```

## Setting Up the Database for Production.
1. Add import dj_database_url to settings.py
2. Change the databases setting in settings.py to get the default database url from env variable as below:
```
DATABASES = {'default': dj_database_url.parse(os.environ["DATABASE_URL"])}
```
3. Run database migrate again to setup the database:
```console
$ python3 manage.py migrate
```
4. Setup superuser account and populate the database with data like the steps described in section "Running the project locally
12c-12e."

## Acknowledgements and Credits
### E-Classic Book store images 

### Data


### Technical Related Attribution and Acknowledgement:
1. My teachers in Trent Global College for teaching me programming.
2. The college teaching assistant: John for his valuable feedback and suggestion for this project.
3. [Django Read the Docs](https://docs.djangoproject.com/en/2.2/)
4. [StackOverflow](https://stackoverflow.com/) for various post shared by the ever brilliant community of Python and Django 
fanatics out there.

## Disclaimer
Any content and images used on this website is purely for personal development and educational purpose. They are not meant for profit or for income purposes.