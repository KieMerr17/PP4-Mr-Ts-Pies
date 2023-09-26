# Mr T's Pies

![Am I Responsive](docs/am-i-responsive.PNG)

**Developer: Kieran Merrett**

💻 [Visit live website](https://mrtspies.herokuapp.com/)  
(Ctrl + click to open in new tab)



## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)

### About

Mr Ts Pies is a website designed to help promote a local pie making business, sharing recent news, advertise workshops and allow users to book onto a workshop of their choice.
<hr>

### User Goals

- To promote the business and inform customers of areas we operate
- To view a list of current pies, news articles and upcoming workshops
- To be able to view edit and cancel workshop bookings

### Site Owner Goals

- To provide a solution to allow users to book onto a workshop
- To attract more business with a well crafted site
- Provide a modern application with an easy navigation
- Fully responsive and accessible
<hr>


## User Experience

### Target Audience
- Users that wish to book a pie making workshop for themselves and friends
- Past and new customers for the business
- Tourists visiting the area that are looking for a cooking experience
- People wanting to find out more and learn more about the company

### User Requirements and Expectations

- Fully responsive
- Accessible
- A welcoming design
- Social media
- Contact information
- Accessibility

##### Back to [top](#table-of-contents)<hr>


## User Stories

### Users

1.	As a User i can navigate across the site so that I can move to each feature of the site easily
2.	As a User i can use a navbar, footer, and social icons so that I can navigate the site, access menus, and access socials
3.	As a User i can view the contact details so that I know how to contact them via email, phone and socials
4.	As a User i can book onto an workshop so that i can reserve a space
5.	As a User i can update my booking so that i can change the details on my booking
6.	As a User i can delete my booking so that i can free up space for someone else
7.	As a User i can view my booking so that i can check the details of the workshop
8.	As a User i can be notified of my action in creation, editing, or deleting of a booking so that i know it has been successful
9. As a User i can register for a new account so that i can make a booking at an event and leave comments
10. As a User i can log in to my account so that i can make a booking or leave comments
11. As a User i can see login status so that i know if i am logged in or not
12. As a User i can view the sites news articles so that I can learn more information, read articles
13. As a User i can Create Read Update and Delete my comments on articles so that i can connect with the site owner
15. As a User i can not book an event in the past so that my booking remains valid
16. As a User i can view news articles page-by-page so that the screen isn't crowded with information

28. As a User i can View a list of events so that I can choose which one i want to book onto
29. As a User i can hide past events so that I can NOT book an event in the past
30. As a User i can view event likes so that i can see the popular events
31. As a User i can view events in pages so that the screen doesn't get blocked up with too many events




### Admin / Authorised User
17. As a Admin i can login so that i can access the back end of the site
18. As a Admin i can manually add a booking so that people can book onto an event in other ways
19. As a Admin i can accept or reject booking so that we avoid false bookings
23. As a Admin i can filter events by date so that I can see what events we have for a particular day
27. As a Site Admin i can create, update and delete events so that users can book onto them



### Site Owner  
24. As a Site Owner i can provide a fully responsive site for my customers so that they have a good user experience
25. As a Site Owner i can validate data entered into my site so that all submitted data is correct to avoid errors
26. As a Site Owner i can provide a contact us page so that users can get in touch with the business


### Kanban & User Stories
- GitHub Kanban was used to track all open user stories
- Backlog, In Progress, Done headings were used in the kanban

<details><summary>User Stories</summary>

![User stories](docs/features/user-stories.png)

</details>

<details><summary>Kanban</summary>

![Kanban mid](docs/features/kanban-in-progress.png)
![Kanban finish](docs/features/kanban-complete.png)

</details>


##### Back to [top](#table-of-contents)<hr>


## Design

### Colours

I chose dark colours, mainly black and white with other colours which are slight variations as the company colours are predominately black and white. I added in the colour orange to buttons to give it a warmer feeling and to add some modernness to it.

The colors I wanted to stay close to  [Coolors.co](https://coolors.co/)
<details><summary>See colour pallet</summary>
<img src="docs/features/colour-pallette.png">
</details>

### Fonts

 The fonts selected were from Google Fonts, Roboto with sans-serif as a backup font.

### Structure

#### Website pages

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer contains all relevant social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.

- The site consists of the following pages:
  - Homepage with information about the 2 chefs, and also the current markets they operate at.
  - About:
    - About Us page to give the customer information about the company, how it came to be and more detailed information about where the pies are made and they source the ingredients.
    - News page where the user can find current articles written by the company to highlight their most current and up to date acheivements and things which may be happening in the business.
  - Pies page is where a list of all the pies the company make are displayed along with the ingredients and all associated allegies
  - Events:
    - Markets this section displays a list of the current markets they operate at, information about the area along with a Google map link to get directions straight to its location
    - Workshops here is displayed the up coming list of workshops the company are hosting along with available spaces should a visiting customer wish to sign up and book on.
  - Register is a page where the user can sign up to the website, this will allow them to be able to leave comments and likes on news articles, like pies and book onto workshops
  - Login / Logout here a authenticated user can choose to log into their profile or log out should they wish to.
  - Profile page is a area where the logged in user can read, update and delete any of their current and upcoming bookings.
  - Get In Touch this page is where the visiting customer can contact the business through a form or through a link to their Facebook Messenger or Whatsapp details
  - 404 error page to display if a 404 error is raised

#### Database

- Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)

<details><summary>Show diagram</summary>
<img src="">
</details>


##### User Model
The User Model contains the following:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

##### Workshop Model
The Workshop Model contains the following:
- title
- slug
- event_date
- spaces
- chef
- content
- featured_image
- excerpt
- created_on
- status
- likes

##### Booking Model
The Booking Model contains the following:
- user
- workshop
- name
- email
- phone_number
- spaces
- dietary_requirements
- booked_on
- approved

##### Article Model
The Article Model contains the following:
- title
- slug
- author
- content
- featured_image
- excerpt
- created_on
- status
- likes


##### Comment Model
The Comment Model contains the following:
- post
- name
- email
- body 
- created_on

##### Pie Model
The Pie Model contains the following:
- title
- slug
- description
- featured_image
- excerpt
- diet
- allergies
- likes


### Wireframes
The wireframes were created using Balsamiq
<details><summary></summary>
<img src="">
</details>


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [EmailJS](https://www.emailjs.com/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)

## Features

### Home page
- Home page includes nav bar, main body and a footer

<details><summary>See feature images</summary>

![Home Page](docs/features/home-page.png)

</details>


### Logo & Navigation
- Display business logo
- Fully Responsive
- On small screens switches to hamburger menu
- Indicates login/logout in status
- displayed on all pages

<details><summary>See feature images</summary>

![Footer](docs/features/home-page-logo.png)
![Footer](docs/features/home-page-register.png)
![Footer](docs/features/profile-page-1.png)
![Footer](docs/features/home-page-hamburger.png)
</details>


### Footer
- Contains social media links
- displayed across all pages

<details><summary>See feature images</summary>

![Footer](docs/features/home-page-footer.png)
</details>

### About -> About Us
- This displays a picture of the owner and employees and a description of the business
  
<details><summary>See feature images</summary>

![About Us](docs/features/about-us-1.png)
![About Us](docs/features/about-us-2.png)

</details>

### About -> News
- The news displays each post made by a staff member
- Paginations is used to display 3 posts per page
- A 'read more' link is present to encourage the reader to read further into the article.
- Number of likes given to the post is displayed
- A section to allow logged in users to like or leave comments, prompted to signup or log in if not currently so
  
<details><summary>See feature images</summary>

![News](docs/features/news-1.png)
![News](docs/features/news-2.png)
![News](docs/features/news-3.png)
![News](docs/features/news-4.png)
![News](docs/features/news-5.png)
![News](docs/features/news-6.png)

</details>

### Comments
- Logged in users may leave comments on articles to communicate their thoughts about the article to the company owner.
- The user may delete their comment should they wish to and are notified to ensure this is the action they wish to take
  
<details><summary>See feature images</summary>

![Pies Menu](docs/features/comments-1.png)
![Pies Menu](docs/features/comments-2.png)
![Pies Menu](docs/features/comments-3.png)

</details>

### Pies Menu
- The Pies page displays all the current pies sold by the company.
- All items are updated in the Admin panel by Staff and superusers ONLY
- Each Pie displays the details and also allows logged in users to like/unlike pies as they feel.
  
<details><summary>See feature images</summary>

![Pies Menu](docs/features/pies-page-1.png)
![Pies Menu](docs/features/pies-page-2.png)

</details>

### Events -> Markets
- Clicking this navigates to a lateral scrolling list of all markets the company currently do.
- Details of times and when they are there are also given
- A link to to a google location for each market is used by clicking the 'Visit Us' button.
- Map directions open in a seperate page
  
<details><summary>See feature images</summary>

![Markets](docs/features/markets-1.png)
![Markets](docs/features/markets-2.png)
![Markets](docs/features/markets-3.png)

</details>

### Events -> Workshops
- Here is displayed a current list of workshops the company offer and the number of available spaces, it is paginated by 4 to save overfilling the page.
- Users can click to get more detail and if logged in, book spaces for themselves
- If not logged in, users are directed to login or sign up to book on.
  
<details><summary>See feature images</summary>

![Markets](docs/features/workshops-1.png)
![Markets](docs/features/workshops-2.png)
![Markets](docs/features/workshops-3.png)
![Markets](docs/features/workshops-4.png)
![Markets](docs/features/workshops-5.png)

</details>

### Booking
- Allow users to make a booking for a workshop
- Allows users to input their details and select dietary requirements
- redirected back to profile page following successful booking

<details><summary>See feature images</summary>

![Register](docs/features/booking-1.png)
![Register](docs/features/booking-2.png)
![Register](docs/features/booking-3.png)
</details>

### Sign up / Register
- Allow users to register an acoount
- Username and password is required, email is optional

<details><summary>See feature images</summary>

![Register](docs/features/signup.png)
</details>


### Login
- User can login to book a workshop, view/edit and delete their bookings and leave likes and comments on the website
- On successful sign in, redirected to your profile page to see your bookings.

<details><summary>See feature images</summary>

![Login](docs/features/sign-in.png)
![Login](docs/features/profile-page-2.png)
</details>


### Logout
- Allows the user to securely log out
- Ask user if they are sure they want to log out

<details><summary>See feature images</summary>

![Logout](docs/features/logout-1.png)
![Logout](docs/features/logout-2.png)
</details>


### Profile Page
- Allow the users to view, edit and delete their bookings
- If user has no bookings, then a note is shown to inform them and ask them if they would like to look at workshops and make a booking.

<details><summary>See feature images</summary>

<details><summary>Profile Page</summary>

![Book](docs/features/profile-page-1.png)
![Book](docs/features/profile-page-2.png)

</details>
<details><summary>Edit Booking</summary>

![Book](docs/features/profile-page-edit-1.png)
![Book](docs/features/profile-page-edit-2.png)

</details>
<details><summary>Delete Booking</summary>

![Book](docs/features/profile-page-delete-1.png)
![Book](docs/features/profile-page-delete-2.png)

</details>

<details><summary>No Bookings</summary>

![Book](docs/features/no-booking-1.png)
![Book](docs/features/no-booking-2.png)

</details>
</details>

### Contact Us
- Using EmailJS, a contact form is presented to all people wishing to contact the business.
- other options include Whatsapp and Facebook Messenger
  
<details><summary>See feature images</summary>

![Contact Us](docs/features/contact-1.png)
![Contact Us](docs/features/contact-2.png)
</details>


### Social Media Links
- A logo and link is used for each social media displayed
- All links open in a new tab to ensure user is not directed away from the business
- Displayed on all pages
  
<details><summary>See feature images</summary>

![Social Media Links](docs/features/social-1.png)
![Social Media Links](docs/features/social-2.png)

</details>


##### Back to [top](#table-of-contents)<hr>


## Validation

The W3C Markup Validation Service

<details><summary>Home</summary>
base.html
<img src="docs/validation/html/html-validation base.png">
index.html
<img src="docs/validation/html/html-validation index.png">
</details>

<details><summary>About</summary>
about-us.html
<img src="docs/validation/html/html-validation about-us.png">
news.html
<img src="docs/validation/html/html-validation news.png">
news-detail.html
<img src="docs/validation/html/html-validation news-detail.png">
</details>

<details><summary>Pies</summary>
pies.html
<img src="docs/validation/html/html-validation pies.png">
</details>

<details><summary>Workshops</summary>
workshops.html
<img src="docs/validation/html/html-validation workshops.png">
workshops-detail.html
<img src="docs/validation/html/html-validation workshop-detail.png">
</details>

<details><summary>Booking</summary>
booking-form.html
<img src="docs/validation/html/html-validation booking-form.png">
edit-booking.html
<img src="docs/validation/html/html-validation edit-booking.png">
delete-booking.html
<img src="docs/validation/html/html-validation delete-booking.png">
</details>

<details><summary>Account Pages</summary>
login.html
<img src="docs/validation/html/html-validation login.png">
logout.html
<img src="docs/validation/html/html-validation logout.png">
register.html
<img src="docs/validation/html/html-validation register.png">
</details>

<details><summary>Profile Page</summary>
profile-page.html
<img src="docs/validation/html/html-validation profile-page.png">
</details>

<details><summary>Contact</summary>
base.html
<img src="docs/validation/html/html-validation contact.png">
</details>
<hr>


### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>
<img src="docs/validation/css/css-validation.png">
</details><hr>

### JavaScript Validation
JSHint JS Validation Service

<details><summary>Script.js</summary>
<img src="docs/validation/js/JSHint-validation-script.png">
</details>
<details><summary>Alert.js</summary>
<img src="docs/validation/js/JSHint-validation-alert.png">
</details>
<details><summary>Contact.js</summary>
<img src="docs/validation/js/JSHint-validation-contact.png">
</details>
<details><summary>Reviews.js</summary>
<img src="docs/validation/js/JSHint-validation-reviews.png">
</details><hr>

### PEP8 Validation
PEP8 Validation Service was used to check the code for PEP8 requirements via Pycodestyle as PEP8online was down


### Lighthouse

Performance, best practices and SEO was tested using Lighthouse.


### Wave
WAVE was used to test the websites accessibility.


##### Back to [top](#table-of-contents)<hr>

