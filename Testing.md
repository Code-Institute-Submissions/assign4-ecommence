## Testing

Manual Test.
### Testing without Authentication (Anonymous User)
1. Index Page.  
    i. As an Anonymous User, the index page shows the below image:  
    ![Anon User Screenshot](https://res.cloudinary.com/doa7bkzvs/image/upload/v1598626553/homepage.jpg)  
    ii. The navbar has the following links : Home, Books, Authors, Cart, Login/SignUp/Sign Out, Username and Shopping Cart Icon.  
    iii. On clicking the call to Explore Button, the page is redirect to the Books page.
    iv. The Popular Title Section shown on right can be view by scroll up and down.
    v. The Shopping cart icon on the Right side of Navbar will shown the number of list item added to the cart. And Upon
       click on it, it will redirect to the Cart page.

2. Books Page.
a. Search bar functionality  
    i. KeyIn the keyword on title or select the author name from the dropdown bar will show all the result in the scroll card section below.
b. List book functionality
   i. Touch and scroll to right can view all the books in the list.
   ii. CLick on the book title will redirect to the book details view page.
   iii. Click on add to cart button will add the item to cart and a message show" item successful added to cart" will be shown on the
   navbar.
3. Author Page  
a. Card 
   i. Click on the name of author will redirect to the author details view page.

4. Other NavBar Links  
    i. Click on the Cart link will redirect the User to the Shopping Cart Page. 
    ii. Click on the Login link will redirect the User to the Login page. 
    iii. Click on the SignUp link will redirect the User to the Sign Up page.  

5. Shopping Cart Page  
    i. If shopping cart is empty, user will see only summary with 0 amount at the bottom of the page. 
    ii. If items have already been added to cart, user will see the list of added items on the top and the billing summary on the
        bottom.  
    iii.  Users will be able to see a blue Checkout Button, when clicked, will link to Stripe Payment Page.

6. Stripe Payment Page
    i. There will be an input to fill in the e-mail, the card information, the name on the card and the country or region the
        user is in. The test credit card number used is Default U.S. card—4242 4242 4242 4242. Test payment is done with any
        three-digit CVC code and an expiration date in the future.  
    ii. On payment success, user will be directed to the [home] page with Flash Message:Your purchase been completed"  
    iii.The number of item beside cart icon will be shown 0.


### Testing with Permission Access SuperUser (Admin).
1. Index Page.  
    i. As an Anonymous User, the index page shows the below image:  
    ![Super User Screenshot](https://res.cloudinary.com/doa7bkzvs/image/upload/v1598628184/admin.jpg)  
    ii. The navbar has the following links : Home, Books, Authors, Cart, add a book, add a author,Login/SignUp/Sign Out, Username and Shopping Cart Icon.  
    iii. On clicking the call to Explore Button, the page is redirect to the Books page.
    iv. The Popular Title Section shown on right can be view by scroll up and down.
    v. The Shopping cart icon on the Right side of Navbar will shown the number of list item added to the cart. And Upon
       click on it, it will redirect to the Cart page.

2. Books Page.
a. Search bar functionality  
    i. KeyIn the keyword on title or select the author name from the dropdown bar will show all the result in the scroll card section below.
b. List book functionality
   i. Touch and scroll to right can view all the books in the list.
   ii. CLick on the book title will redirect to the book details view page.
   iii. Click on add to cart button will add the item to cart and a message show" item successful added to cart" will be shown on the
   navbar.
3. Author Page  
a. Card 
   i. Click on the name of author will redirect to the author details view page.

4. Other NavBar Links  
    i. Click on the Cart link will redirect the User to the Shopping Cart Page. 
    ii. Click on the Login link will redirect the User to the Login page. 
    iii. Click on the SignUp link will redirect the User to the Sign Up page.  

5. Shopping Cart Page  
    i. If shopping cart is empty, user will see only summary with 0 amount at the bottom of the page. 
    ii. If items have already been added to cart, user will see the list of added items on the top and the billing summary on the
        bottom.  
    iii.  Users will be able to see a blue Checkout Button, when clicked, will link to Stripe Payment Page.

6. Stripe Payment Page
    i. There will be an input to fill in the e-mail, the card information, the name on the card and the country or region the
        user is in. The test credit card number used is Default U.S. card—4242 4242 4242 4242. Test payment is done with any
        three-digit CVC code and an expiration date in the future.  
    ii. On payment success, user will be directed to the [home] page with Flash Message:Your purchase been completed"  
    iii.The number of item beside cart icon will be shown 0.

7. CRUD functionality(for books and authors)
    a. View Page
    i. Click on the title of the books / author name will redirect to the view page.
    ii. Add to cart button, update button and delete button was shown on the right side on the page.
    b. Update page
    i. It can redirect to the Update page form with the clicking on the update button at books/author view details page.
    2. CLick on submit button will procees the update the editing data in the form and redirect to home page with message"Books/Author updated."
    c. Delete Page
    i. It can redirect to the Delete page  with the clicking on the delete button at books/author view details page.
    ii. Click on yes button will complete the delete process and redirect to home page with message"Books/Author Deleted"
    iii. Click on Cancel will redirect to all books /authors page.

    
### Testing with Permission Access Authentical User (Customer).
1. Index Page.  
    i. As an Anonymous User, the index page shows the below image:  
    ![ User Screenshot](https://res.cloudinary.com/doa7bkzvs/image/upload/v1598627804/user.jpg)  
    ii. The navbar has the following links : Home, Books, Authors, Cart, Login/SignUp/Sign Out, Username and Shopping Cart Icon.  
    iii. On clicking the call to Explore Button, the page is redirect to the Books page.
    iv. The Popular Title Section shown on right can be view by scroll up and down.
    v. The Shopping cart icon on the Right side of Navbar will shown the number of list item added to the cart. And Upon
       click on it, it will redirect to the Cart page.

2. Books Page.
a. Search bar functionality  
    i. KeyIn the keyword on title or select the author name from the dropdown bar will show all the result in the scroll card section below.
b. List book functionality
   i. Touch and scroll to right can view all the books in the list.
   ii. CLick on the book title will redirect to the book details view page.
   iii. Click on add to cart button will add the item to cart and a message show" item successful added to cart" will be shown on the
   navbar.
3. Author Page  
a. Card 
   i. Click on the name of author will redirect to the author details view page.

4. Other NavBar Links  
    i. Click on the Cart link will redirect the User to the Shopping Cart Page. 
    ii. Click on the Login link will redirect the User to the Login page. 
    iii. Click on the SignUp link will redirect the User to the Sign Up page.  

5. Shopping Cart Page  
    i. If shopping cart is empty, user will see only summary with 0 amount at the bottom of the page. 
    ii. If items have already been added to cart, user will see the list of added items on the top and the billing summary on the
        bottom.  
    iii.  Users will be able to see a blue Checkout Button, when clicked, will link to Stripe Payment Page.

6. Stripe Payment Page
    i. There will be an input to fill in the e-mail, the card information, the name on the card and the country or region the
        user is in. The test credit card number used is Default U.S. card—4242 4242 4242 4242. Test payment is done with any
        three-digit CVC code and an expiration date in the future.  
    ii. On payment success, user will be directed to the [home] page with Flash Message:Your purchase been completed"  
    iii.The number of item beside cart icon will be shown 0.




    

