# Code Institute Full Stack Frameworks with Django

# BooksTreasureProject E-Commerce Website

## Project Objectives
1. This website is created with the purpose to provide Collection of Classic Books ecommence platform for user.
2. An authenticated user only will be able to complete the purchase online beside visit the shop.
3. The view of books catalog is design in swipe with finger features which is mobile-friendly.
4. So, the user can make purchases with any electronic devices once the login to the website.
5. Responsive to all kind of mobile devices / electronice devices provides the user an easy accss and clear view browsing layout.
6. A new user could register for a new account, login, change or reset a password, view his/her profile and logout. 
7. The user can reach us online via contact us [contact us](https://ecommence-books.herokuapp.com/info/contact_us/) with enquiry 
   about books they wish to look for.
8. User also can access to Short biography of the author besides browsing the books.
9. Flash Message will be show on navbar to indicate the success of the process carry out such as add cart process, complete purchase and etc.
10. A logged in superuser(which is the admin of the website) has advantage books CRUD rights which allow him/her to add a books/authors, 
   edit the books/authors's data and even delete it from the database.
11. For quick access without sign up a new account for browsing and testing purpose, please use the existing user account details to
    proceed:

    a) To log in as a user without game CRUD rights, please use the following:

        Username: vapal14749@banetc.com
        Password: asd1234567

    b) To log in as a user with game CRUD rights, please use the following:

        Username: admin
        Password: sky760131


## Deployed Link
The deployed website can be found [here](https://ecommence-books.herokuapp.com/)

## UX/UI
### Overview and Colour
1. The layout concept behind this website is choose with the idea of illustrations which is different from most current ecommence 
   website nowadays.
2. The concept for the color and image that being placed in the website is to provide clean and refreshing look for user.
3. The Name of the website "TreasureClassicBooks" is explain the purpose of this website doing for the user.
    "Treasure Classic Books" for those user/customer who loves to collect and read classic books.
4. Image placed ideas of its position and size is based on design purpose and this is not an page error due to css or files.
5. Placement fixed top navbar is for user easily access ,recognized and direct to the features in anytime.
6. Username of user upon successful created and login will be showed on right side of the navbar.
7. An Icon of cart with the info of how many items in the cart at this moment easily noticed by user on the right side of the navbar(
    beside the username).
8. Color of that choosen mainly results calm effect and clear browsing.
9. On bottom of the website, access on mobile app download link, Get to Know Us and Connect with Us On was placed as a footer of the
   websites.



## User Stories
### Basic User Stories
1. Once user access in the website/app with authenticated account, it will be direct to the home page [Home](https://ecommence-books.herokuapp.com/).
   In this page, Info about popular books among the customer can be seen.
2. The fixed top navbar provides info of shop icon and name, webpage feature, username, cart info and success flash message.
3. A users access the all books collection via [Books](https://ecommence-books.herokuapp.com/books/all) and browse with only swipe 
  to the right with finger touch.
4. A Users can directly search for the available books, either by a search on title keyword or by sorted from author name dropdown bar.
5. As the user of the websites, the info about books in the collection list comes with title, author, price and add to cart button for 
  directly purchase access.
6. The user of the websites can access the more details of the book by clicking on its title.
7. User of the website also can carried on with add cart process while browsing more info about the books in view page
   [view](https://ecommence-books.herokuapp.com/books/view/2/).
8. As user of the website, he/she also can browse all the name of author in the website via [authors](https://ecommence-books.herokuapp.com/books/authors/).
9. With clicking on the author name, a short biography of the author [views](https://ecommence-books.herokuapp.com/books/view/authors/3)
   can be views by user of the website.
10. As user of website, he/she can access to cart[cart](https://ecommence-books.herokuapp.com/carts/view) to view the list of cart before complete to 
   payment. All purchase required a valid and authenticated user account.
11. User will be directly to payment process via checkout button in the cart webpage, he/she will be asked to fill in credit card info to 
    complete the transaction of purchase.
12. As user of the websites, he/she can access the info about the shop as below:
    a. Available on Apps link for iphone and googleplay users.
    b. Get to Know Us link for [About us](https://ecommence-books.herokuapp.com/info/about_us/), [Terms and conditions](https://ecommence-books.herokuapp.com/info/terms_and_conditions/),
       [Contact Us](https://ecommence-books.herokuapp.com/info/contact_us/).
    c. Connect With Us for Instagram , pinterest and Github(this is for website creator owner).
    
### SuperUser Stories
1. User with superuser account(admin) can 
 a. add a book [add book](https://ecommence-books.herokuapp.com/books/create)
 b. add a author [add author](https://ecommence-books.herokuapp.com/books/authors/create)
 c. edit a book [edit book](https://ecommence-books.herokuapp.com/books/update/3)
 d. edit a author [edit author](hhttps://ecommence-books.herokuapp.com/books/authors/update/2)
 e. delete a book [delete book](https://ecommence-books.herokuapp.com/books/delete/3)
 f. delete a author [delete author](hhttps://ecommence-books.herokuapp.com/books/authors/delete/3)
 g. access the database.

## Wireframes
The idea of webpage wireframes for this project was completed with AdobeXD tools. The document was saved as pdf format in the
folder named docs or click on the link [wireframes]().

## E-Classic Books Shop Features
### Index/Home page
a. Features for user attraction
* Popular books list with image and brief description on the right side of the webpage and easy to browsing with touch and scroll up.
* An Explore button which direct the user to the books collection.
b. Features for user navigation
* A fixed top clear navbar allow users to navigate to Home, Books, Authors, carts, Login/signup/logout.
c. Features for user notification
* Flash message will be show on the navbar allow user to be notify for successful process such login, logout, add to cart, 
   payment complete, etc
d. Features for user info and shopping cart
* Username and Number of item in the cart show on the right of the navbar.

e. Hidden features
* if the logging as superuser/admin, navigation to add a book and add a author can be seen on navbar menu.
* Only logging as superuser/admin, can perform CRUD functions for books and authors.

### Books page
a. Search Features
* Two search type input can be choose for search purpose by users.
* Option One is user can keyin a keyword related to the book title.
* Option Two is user can browse the Author dropdown bar of current complete list of available author name.

b. Card display
* Touch and swipe action to for user to browse all the books in the collection.
* The search result of the query will be display on this card.
* Each books card comes with its own info such as title, author, price and individual add to cart button.
* User can click on the books title for more info about that selected books to directly to the books view page.
* The selected books can be added to cart directly via the individual add to cart button.

### Book View pages
a. Info Presentation
* The info of books that presents in this page such as book image, title, Author , price, ISBN, Date published, length, quotes and description.
* The individual add to cart button also place in the view page for user easy access add to cart without back to all books collection 
  page.

b.Hidden features
* Only with logging as superuser/admin, Update and edit button function can seen and access.


### Authors Pages
a. Column card
* The list of all author can be view in column card display with their name as the link to the biography info page.
* The use will be direct to author view page by click on the author name.

### Author View pages
a. Info Presentation
* The info about author that presents in this page such as Author image, Name , biography and his/her published book title list.

b.Hidden features
* Only with logging as superuser/admin, Update and edit button function can seen and access.

### Cart Page
a. Info Presentation
* The info that presents in this page are such as Book image, quantity , title , and total price.
* User can remove the item and change the item quantity(Updated button).
* The List of all item in the cart is presented in a table layout.
* Summary of total Payment for the Purchase are showed at the bottom left of the page.

b. Check process
* The Checkout button placed below of the summary of total purchase cost.
* It will redirect to credit card payment procees via click on the checkout button.


### Login/Logout/SignUp Page
* The account management pages are managed by Django-AllAuth


## Superuser additional access page 
### add a book Page
a. Form 
* A form with required fields of the books.
* All the fields in the book required to be fill in in order to successful add in a Book.
* Format for key in date in published field is YYYY-MM-DD.
* The Image field is fill with the image url link.
* Submission completed with Click on the Submit button.


### add a author Pages
* A form with required fields of the books.
* All the fields in the book required to be fill in in order to successful add in a Author.
* The Image field is fill with the image url link.
* Submission completed with Click on the Submit button.



## Technologies Used
The technologies used for this project are:
1. [Django(Release 2.2.14)](https://www.djangoproject.com/start/overview/). Django is a Python Web Framework that encourages rapid
development and clean design. It is the main requirement of this project.
2. [Python(Release 3.8.3)](https://www.python.org/downloads/release/python-383/). Python is the programming language that Django 
used tools for built on.
3. [HTML5](https://html.spec.whatwg.org/). HTML is the markup language that structures the base of webpage documents.
4. [CSS3](https://www.w3.org/TR/2001/WD-css3-roadmap-20010523/). Cascading style sheet is the language that presents and styles 
the HTML design idea documents.
5. [Javascript and JQuery](https://developer.oracle.com/sg/javascript/). Javascript and Jquery is used primarily to do DOM 
manipulation and it is the main engine to serve interactivity and event handling to the webpages.
6. [Bootstrap (Release 4.5)](https://getbootstrap.com/docs/4.5/getting-started/introduction/). Bootstrap is the layout framework
used to organize the website's display.
7. [Gitpod](https://www.gitpod.io/)  
Gitpod is an online IDE that can be launched in Github. It is used to perform CRUD function  with the code for this project.
8. [Git and Github](https://github.com/)  
Github is an online hosting service for software development that utilizes Git for version control.
9. [Stripe](https://stripe.com/en-sg). Stripe is a financial software service provider that provides the API for software developers
to integrate payment into their websites and mobile apps.
10. [Font Awesome](https://fontawesome.com/) Font Awesome Icons are used in this project to give illustrations to some edit and 
delete buttons.
11. [Cloudinary](https://cloudinary.com/) Cloudinary are used in this project to store the image of books and author for database.

### Django Libraries
1. [Django-AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html) is a Django Library that manages authentication, 
registration, account management as well as 3rd party (social) account authentication 
2. [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is Django package that provides DRY Django Forms.

### Database
The database used in the project is PostgreSQL. PostgreSQL is an open source Relational Database Management System that is similar
to MySQL but it has an object oriented database model which are directly supported in database schemas and query language.

### Database Structure
A UML diagram to illustrate the relationship between models is drawn and shown [here](https://github.com/skyeoh06)

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
6. At the top right of the personal repository, there is a green coloured Gitpod button.
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

## Bugs and improvements
1. The signup complete process faced a network error, it will be fixed in the future revisions.
2. Will be added in a user info database that shown info of past history purchases.

## Acknowledgements and Credits
### E-Classic Book store images 
1. Image form google [google](https://www.google.com./)

### Data
1. Books data from penguin website and goodreads website.
2. Author data from penguin website and wikipedia website.

### Design ideas
1. The design idea is inspired by UX UI design 2020 from youtube video.

### Technical Related Attribution and Acknowledgement:
1. My teachers in Trent Global College for teaching me programming.
2. The college teaching assistant: John for his valuable feedback and suggestion for this project.
3. [Django Read the Docs](https://docs.djangoproject.com/en/2.2/)
4. [StackOverflow](https://stackoverflow.com/) for various post shared by the ever brilliant community of Python and Django 
fanatics out there.

## Disclaimer
Any content and images used on this website is purely for personal development and educational purpose. They are not meant for profit or for income purposes.