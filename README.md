# BrushBucket - A digital brush Ecommerce site.

## Introduction

This is my coding repository dedicated to the BrushBucket website. It is an e-commerce platform designed for digital artists and enthusiasts, focusing on the sale of Procreate brushes. BrushBucket began as an idea for a community-driven site where users could share and explore digital brushes. Due to project scope and technical considerations, it has evolved into a marketplace for purchasing, downloading, and rating a diverse range of digital brushes. One of the key features of the project is utilizing AWS for secure and efficient storage of the digital brush files, which ensures a smooth user experience in accessing and using these creative tools. This platform not only enhances the digital art experience for its users but also stands as a testament to the integration of artistic creativity with cutting-edge web technology.

[Visit the Website Here](https://brush-bucket-2ba4b4f41791.herokuapp.com/)

[Visit the Project's GitHub Repository Here](https://github.com/Stuartpkd/Brush-Bucket)

[Link to the projects board](https://github.com/users/Stuartpkd/projects/3)

![Image of site on different platforms]()

# User experience

The UX or User Experience centers on the website's accessibility and its level of user-friendliness, both of which play a critical role in determining the website's overall success.

These can be made up of 5 layers:

The Strategy Plane
The Scope Plane
The Structure Plane
The Skeleton Plane
The Surface Plane

## Strategy 

After thinking about the strategy for my site, I came up with a target audience which would influence the features included.

### Target Users:

1. Age Range: Primarily individuals aged 18-40 who are actively engaged in or interested in digital art creation and exploration.
2. Digital Art Enthusiasts: Users who are passionate about digital art, either as creators, learners, or appreciators.
3. Digital Brush Collectors: Those interested in expanding their toolkit with diverse digital brushes, enhancing their digital artwork.
4. Emerging Digital Artists: Individuals looking to discover and experiment with new digital brushes to refine their art style and techniques.
5. Art Community Members: Users who value the sense of community in the digital art world and enjoy connecting with fellow artists and art enthusiasts.

### What the user would look for:

* Visually Appealing and Non-Distracting Design: A clean and aesthetically pleasing interface that showcases digital brushes without overshadowing them.
* Ease of Navigation: A user-friendly and straightforward website layout that makes browsing, selecting, and purchasing digital brushes hassle-free.
* Efficient Downloading Process: A quick and seamless method for users to acquire and download their chosen digital brushes.
* Community Interaction: Features that allow users to rate brushes and provide feedback.
* Personal Collection Management: A system for users to save, organize, and revisit their favorite brushes, enhancing their collection and usage experience.
\
&nbsp;

### User Stories

| id  |  Content | Label |
| ------ | ------ | ------ |
| [1](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42174609) | As a buyer, I can browse a selection of digital brushes so that I can find the perfect brushes for my digital art projects. | Needed |
| [2](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42174609) | As a buyer, I can view detailed information about a digital brush, including its description, price, and user ratings, so that I can make an informed purchasing decision. | Needed |
| [3](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42174758) | As a buyer, I can add digital brushes to my shopping cart so that I can review and purchase them later. | Needed |
| [4](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42174837) | As a buyer, I can complete the purchase of selected digital brushes so that I can have access to the downloaded files for my art projects. | Needed |
| [5](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42174915) | As a buyer, I can access my purchase history and download links in my profile so that I can easily retrieve brushes I've purchased in the past. | Needed |
| [6](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42175047) | As a buyer, I can leave ratings for digital brushes I've purchased so that I can share my feedback and help others make choices. | Needed |
| [7](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42175176) | As a buyer, I can save my favorite digital brushes to a favorites list so that I can quickly access and consider them for future purchases. | Needed |
| [8](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42175359) | As a seller/admin, I can upload digital brushes to the marketplace so that I can offer my creations to a broader audience. | Needed |
| [9](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42175448) | As a seller/admin, I can manage and edit the product listings of the digital brushes I've added to the site so that I can keep them up to date. | Needed |
| [10](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42175448) | As a seller/admin, I can manage and edit the product listings of the digital brushes I've added to the site so that I can keep them up to date. | Needed |
| [11](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42175795) | As a seller/admin, I can view sales statistics to understand how well my digital brushes are performing on the platform. | Nice to have |
| [12](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42176082) | As an admin, I can manage user accounts and activities to ensure the safety and integrity of the platform. | Needed |
| [13](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42176934) | As a new user, I can click on the "Sign Up" button on the homepage so that I can create a new account. | Needed |
| [14](https://github.com/users/Stuartpkd/projects/3/views/1?pane=issue&itemId=42177096) | As a new user, I should receive an email with a verification link after registering. | Needed |
| [15](https://github.com/users/Stuartpkd/projects/3?pane=issue&itemId=45623755) | As a user I can leave feedback or ask for assistance via a contact page so that I can provide helpful suggestions and have any issues I have addressed. | Needed |
\
&nbsp;

## Scope

In the development of BrushBucket, I explored the ambitious idea of integrating an interactive canvas feature, allowing users to test out digital brushes directly on the website. This feature aimed to provide a hands-on experience, enabling users to truly feel the essence of each brush before making a purchase. However, during the testing phase, it became apparent that the canvas was quite resource-intensive, leading to significant browser performance issues. Given my commitment to ensuring a seamless and efficient user experience on BrushBucket, I decided to shelf this feature for the time being. It remains a key area of interest for future development, and I'm actively seeking more optimized solutions. For reference, I'm including a link to a similar canvas implementation that inspired my initial tests, showcasing the potential direction for this feature's future integration.
\
&nbsp;

| id  |  Content | Label |
| ------ | ------ | ------ |
| [1](https://github.com/users/Stuartpkd/projects/3?pane=issue&itemId=42176141) | As a user, I can test Procreate brushes on a simulated canvas so that I can get a feel for how they work before making a purchase. | Nice to have |
| [2](https://github.com/users/Stuartpkd/projects/3?pane=issue&itemId=42176221) | As a user, I can select different brushes from the collection to experiment with different styles and effects. | Nice to have |
| [3](https://github.com/users/Stuartpkd/projects/3?pane=issue&itemId=42176281) | As a user, I can choose different colors for my brushstrokes to create colorful and expressive digital art. | Nice to have |
| [4](https://github.com/users/Stuartpkd/projects/3?pane=issue&itemId=42176336) | As a user, I can undo and redo my actions to correct mistakes and experiment with different ideas. | Nice to have |
\
&nbsp;

## Development Sprints

### Sprint 1: Core Functionality and Basic Features
**Milestone:** Establishing the foundational platform.
- Enable buyers to browse a selection of digital brushes. (User Story 1)
- Allow buyers to view detailed information about each digital brush. (User Story 2)
- Implement a shopping cart for buyers. (User Story 3)
- Create a sign-up process for new users. (User Story 13)
- Implement email verification for new accounts. (User Story 14)

### Sprint 2: Enhancing User Experience and Seller/Admin Capabilities
**Milestone:** Enriching the platform with advanced features.
- Set up the checkout process for brush purchases. (User Story 4)
- Enable access to purchase history and downloads in user profiles. (User Story 5)
- Implement a feature for buyers to leave ratings. (User Story 6)
- Develop admin capabilities for user account management. (User Story 12)

### Sprint 3: Advanced Features and User Interactions
**Milestone:** Adding interactive and user engagement features.
- Implement a favorites list for buyers. (User Story 7)
- Enable sellers/admins to upload new brushes. (User Story 8)
- Allow sellers/admins to manage and edit product listings. (User Story 9 & 10)
- Create a contact page for user feedback and assistance. (User Story 15)

### Future Sprints: Further Development and Expansion
**Milestone:** Expansion and continuous improvement.
- Improve sales statistics for sellers/admins. (User Story 11)
- Explore integrating an interactive canvas for brush testing.
- Enhancements in UI/UX for easier navigation and accessibility.
- Additional security features and user account management options.
\
&nbsp;

## Structure

The project's structure is meticulously planned to ensure an organized approach to development, facilitating adherence to sprint steps and project goals. The project content is segmented into applications, each dedicated to handling different aspects of the platform. The data collected from users is structured into database tables for efficient organization and storage.
\
&nbsp;

### Project Applications
For BrushBucket, 6 applications were created, each with a specific focus:

1. **Home App** – Manages the landing page and general navigation across the site.
2. **Profile** – Handles profile management, purchase history and brush favourites.
3. **Brushes App** – Central to the project, this app allows users to browse, view, and rate digital brushes. It also includes functionalities for brush details and categorization.
4. **Bag App** – Manages the shopping cart functionality, enabling users to add brushes to their cart and review them before purchase.
5. **Checkout App** – Facilitates the checkout process, including payment handling and order confirmation.
6. **Contact App** – Allows users to send messages or inquiries through a contact form, facilitating communication between users and site administrators.

Each application serves a distinct purpose, contributing to the cohesive functionality of BrushBucket. This modular approach allows for efficient development and future scalability of the platform.
\
&nbsp;

### Project Databases
In the development of the "BrushBucket" application, my project employs a sophisticated database structure to support the intricate functionalities envisioned in the user stories. Initially, the project began with an ambitious database design, as illustrated in the initial SQL map. However, as the project evolved, driven by practical considerations of scope and time, the databases underwent several transformations, leading to the current and more refined structure.
\
&nbsp;

> ![Database Table 1](docs/database_schema/sql-map-1.png)
\
&nbsp;
> ![Database Table 1](docs/database_schema/sql-map-2.png)
\
&nbsp;

### Brushes Models:

#### BrushCategory Model
The BrushCategory model categorizes the various types of digital brushes available on the platform. It has been designed with simplicity and user-friendliness in mind, consisting of the following fields:
- `name`: A CharField with a maximum length of 200 characters, representing the technical name of the category.
- `friendly_name`: An optional CharField, also with a 200-character limit, designed to store a more user-friendly version of the category's name. This field can be blank or null.

These fields together enable clear categorization and easy retrieval of different types of digital brushes, enhancing the user experience in brush selection.

#### Brush Model
The Brush model lies at the heart of the platform, representing the digital brushes made available to users. This model includes a variety of fields to comprehensively describe each brush:
- `name`: A CharField limited to 100 characters for the brush's name.
- `category`: A ForeignKey linking to the BrushCategory model, specifying the category of the brush.
- `description`: A TextField for a detailed description of the brush.
- `price`: A DecimalField to represent the brush's price.
- `rating`: A DecimalField for the average rating of the brush, with a default value of 0.
- `rating_count`: An IntegerField tracking the number of ratings received.
- `image`: An ImageField for an image of the brush.
- `brush_file`: A FileField for uploading the actual digital brush file.
- `created_at`: A DateTimeField that automatically records the creation time of the brush entry.

Additionally, the Brush model includes an `update_average_rating` method to calculate and update the average rating based on user feedback.

#### Rating Model
The Rating model facilitates user ratings for each digital brush. It is structured to ensure each user can only rate a brush once:
- `brush`: A ForeignKey that links to the Brush model.
- `user`: A ForeignKey connected to the user model, identifying the user who provided the rating.
- `rating`: An IntegerField that stores the user's rating for the brush.

The Rating model includes an overridden save method to update the brush's average rating every time a new rating is saved. It uses a unique_together Meta option to prevent multiple ratings for the same brush from the same user, ensuring the integrity of the rating system.
\
&nbsp;

### Checkout Models:

#### Order Model
The Order model captures and manages the details of purchases made on the platform. Each order's attributes ensure a comprehensive record of the transaction, including user information and total amounts:
- `order_number`: A CharField with a unique order number generated using UUID.
- `user_profile`: A ForeignKey to the UserProfile model, linking the order to the user's profile. It's set to null on user profile deletion.
- `full_name`, `email`: CharFields to store the customer's name and email.
- `date`: A DateTimeField to automatically record the date and time of the order.
- `order_total`, `grand_total`: DecimalFields to store the total order amount and the grand total, respectively.
- `original_bag`: A TextField to store a snapshot of the user's shopping bag at the time of the order.
- `stripe_pid`: A CharField to store the Stripe payment intent ID.
- Methods `_generate_order_number` and `update_total` are included to handle order number generation and total amount calculation.

#### OrderLineItem Model
The OrderLineItem model is crucial in breaking down each order into its constituent items:
- `order`: A ForeignKey linking to the Order model.
- `product`: A ForeignKey linking to the Brush model, representing the purchased brush.
- `quantity`: An IntegerField to store the quantity of each brush in the order.
- `lineitem_total`: A DecimalField to store the total cost for each line item, calculated as the product's price times the quantity.
- The save method is overridden to calculate `lineitem_total` automatically.

Together, these models facilitate the management of orders and their details, providing a robust system for handling transactions and maintaining accurate records of purchases on the platform.
\
&nbsp;

### Contact Models:

#### ContactMessage Model
The ContactMessage model serves as the backbone for the contact feature of the site, enabling users to send messages to the website administrators. This model is structured to capture essential communication details, offering a straightforward yet effective way for users to engage with the site operators:
- `name`: A CharField to store the name of the user sending the message, with a maximum length of 100 characters.
- `email`: An EmailField to record the user's email address, facilitating follow-up communication.
- `subject`: A CharField to capture the subject of the message, allowing for a clear understanding of the message's intent.
- `message`: A TextField to store the user's message, providing ample space for detailed communication.
- `created_at`: A DateTimeField that automatically records the date and time when the message was created.
- The `__str__` method is customized to return a string representation of the message, including the sender's name and the subject, enhancing the readability and management of contact messages in the admin interface.

This model efficiently organizes user inquiries and feedback, ensuring that user voices are heard and addressed in a timely and organized manner.
\
&nbsp;

### Home Models:

#### UserProfile Model
The UserProfile model acts as a central hub for user-specific data, ensuring seamless management of individual preferences and historical records on the platform. Its key features include:
- `user`: A OneToOneField linking to the Django's standard User model, establishing a unique relationship with each user.
- `saved_brushes`: A ManyToManyField connected to the Brush model, allowing users to save their favorite digital brushes for easy access and future reference.
- A `__str__` method returning the username, making user profile identification straightforward in the admin interface.
- A `purchase_history` property method, efficiently retrieving the user's past orders from the 'Order' model, thus providing a convenient view of their transaction history.

#### SavedBrush Model
The SavedBrush model encapsulates the relationship between users and their saved digital brushes, enhancing the user experience by allowing for a personalized collection of preferred brushes. It includes:
- `user`: A ForeignKey to the User model, identifying the user who saved the brush.
- `brush`: A ForeignKey to the Brush model, indicating the specific saved brush. It features a 'related_name' for easy querying of all saved brushes associated with a particular brush.
- A `__str__` method that combines the user's username and brush name, offering a clear and concise representation of each saved brush entry.

Additionally, the models leverage Django signals to automate the creation or updating of user profiles upon user account creation or modification. This feature ensures that every user account is consistently linked with a corresponding user profile, streamlining the management of user-related data.
\
&nbsp;

## Skeleton
The skeleton provides a broad initial idea that is further refined and built on. 
\
&nbsp;

### Wireframes
I began by crafting a mobile rendition to align with my mobile-first strategy, subsequently crafting versions for medium and large screens. It's crucial to maintain a straightforward layout that doesn't overshadow the artwork posts while ensuring the website's responsiveness across different screen sizes. The brushes still feature in the wire frames, but their structure and layout was still used in the final designs for the website.

Basic wireframes can be found below (Note that these vary slightly from the final website design):

* [Home Page](docs/wireframes/Home_Desktop.pdf "Home Page")
* [Profile](docs/wireframes/Profile.pdf "Profile")
* [Brushes](docs/wireframes/Brushes.pdf "Brushes")
* [Brush Detail](docs/wireframes/Brush%20detail.pdf "Brush details")
* [Checkout](docs/wireframes/Checkout.pdf "Checkout")
* [Bag](docs/wireframes/Bag.pdf "Bag")
\
&nbsp;

## Surface
The surface plane primarily pertains to aesthetics and the interface, emphasizing the selection of an appropriate color palette, font, and icons that enhance the website's allure without detracting from the artwork's focal point.
\
&nbsp;

### Font
The font used is called Mukta, it has good readability and had a lot of weights to use for easier heirarchy. They were sourced from [here](https://fonts.google.com/specimen/Mukta?query=mukta) and were used in suitable sections.

### Colours

![Colours](docs/colours/colours.png)

I've designed the site's colour scheme to be minimalist yet visually intriguing. The subtle palette ensures that the artwork remains the focus, without any distractions. These careful colour choices add to the user experience without overshadowing the brushes.
\
&nbsp;

### Responsive Screens
The website's construction will commence with a focus on a compact 350px-width mobile screen, after which it will be adapted to fulfill the specifications for medium/tablet, large, and extra-large screens, as illustrated in the following table.

| Screen Size   | Breakpoint |
| -----------   | ---------- |
| small/mobile  |    350px   |
| medium/tablet |    768px   |
| large         |   992px    |
| extra-large   |   1400+px  |

\
&nbsp;

# Features

### Index Page

![Index Page](docs/images/index-page.png)

The Index Page serves as the main landing page for users, showcasing featured digital brushes and providing direct access to brush categories and other key areas of the site.

---

### Profile Page

![Profile Page](docs/images/profile-page.png)

The Profile Page acts as a personal hub for users, displaying their purchase history, saved brushes, and offering access to account settings.

---

### Brushes Page

![Brushes Page](docs/images/brushes-page.png)

The Brushes Page presents a comprehensive collection of digital brushes available for purchase, complete with filtering options by category.

---

### Brush Detail Page

![Brush Detail Page](docs/images/brush-detail-page.png)

This page provides detailed information on individual brushes, including descriptions, pricing, user ratings, and the ability to add them to the shopping bag or wishlist.

---

### Admin Product Management Page

![Admin Management](docs/images/admin-management-page.png)

An administrative interface that allows for the management of digital brushes inventory, crucial for site maintenance and product updates.

---

### Checkout Page

![Checkout Page](docs/images/checkout-page.png)

A secure checkout interface where users can complete their purchases, input billing information, and review their order summary.

---

### Checkout Success Page

![Checkout Success](docs/images/checkout-success-page.png)

A confirmation page post-purchase that summarizes the order details and provides download links for purchased brushes.

---

### Bag Page

![Bag Page](docs/images/bag-page.png)

Allows users to view and manage their selected digital brushes in their shopping bag, with options to adjust quantities or proceed to checkout.

---

### Contact Page

![Contact Page](docs/images/contact-page.png)

Dedicated for user inquiries and feedback, featuring a contact form for direct communication with the site administrators.

---

### Error 404 Page

![Error 404](docs/images/error-404-page.png)

A user-friendly 'Page Not Found' error page, guiding users back to the main website smoothly.

---

### Error 500 Page

![Error 500](docs/images/error-500-page.png)

Handles server errors by providing an informative notification and easy navigation back to the operational parts of the site.
\
&nbsp;

# Technologies Used

## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML "HTML") - To create the Django templates for the associated views and models in the project applications.
* [CSS](https://en.wikipedia.org/wiki/CSS "CSS") - To style the website.
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript") - To create interactive animations for the site.
* [Python]( https://en.wikipedia.org/wiki/Python_(programming_language) "Python") – Is the primary language of Django and used to create all forms, models and views.
\
&nbsp;

## Tools
* [Django](https://www.djangoproject.com/ "Django") – The framework used in this project to incorporate databases with a website.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Crispy Forms") – Formats the models into forms on webpages using the `|crispy` filter and `{% crispy %}` tag.
* [Cloudinary](https://cloudinary.com/ "Cloudinary") - Used to store website's images.
* [Gitpod](https://www.gitpod.io/ "Gitpod") – Used as the development environment.
* [GitHub](https://github.com/ "GitHub") – The project’s Version Control Management System.
* [Heroku](https://www.heroku.com/ "Heroku") – To deploy the webpage.
* [Illustrator](https://www.adobe.com/ie/products/illustrator/campaign/pricing.html?gclid=CjwKCAjwxaanBhBQEiwA84TVXPogNfGdqMqcbQ8FXjlOcbhv5YMqMEqN6UdeCt0m35siVj5JWbijqhoCHcgQAvD_BwE&mv=search&mv=search&mv2=paidsearch&sdid=GMCWY69B&ef_id=CjwKCAjwxaanBhBQEiwA84TVXPogNfGdqMqcbQ8FXjlOcbhv5YMqMEqN6UdeCt0m35siVj5JWbijqhoCHcgQAvD_BwE:G:s&s_kwcid=AL!3085!3!547974576454!e!!g!!illustrator!1426208079!56320331432&gad=1 "Illustrator") – For the creation of associated wireframes.
* [DrawSQL](https://drawsql.app/ "DrawSQL") – For the creation of the database diagrams.
* [CSSgradient](https://cssgradient.io/ "CSSgradient") – For the visualisation of gradients for the sites styling.
* [LottieFiles](https://lottiefiles.com/ "LottieFiles") – This hosts the animated logo at the top of the screen.

## Styling
* [Bootstrap](https://getbootstrap.com/ "Bootstrap") – To provide extra styling and out-of-the-box elements e.g. burger menu.
* [Google Fonts](https://fontawesome.com/ "Google Fonts") – For font used in the site.

## Validation
* [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML") – To validate all the HTML files, including the templates from Django itself, due to editing them.
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS") – To validate the “style.css” page as well as the specific css page made to create the Formula 1 teams’ logos.
* [JSHint](https://jshint.com/ "JSHint") – To validate the code within the “script.js” file.
* [Python Syntax Checker PEP8](https://www.pythonchecker.com/ "Python Syntax Checker PEP8") – To validate all the Python files, making sure they align with PEP8.
* [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en "Lighthouse") – To check the website’s performance and accessibility, making sure the best practices are used.

## Databases
* [SQLite](https://sqlite.org/index.html "SQLite") - The default database on Django, utilised for unittesting.
* [ElephantSQL](https://www.elephantsql.com/ "ElephantSQL") – The final database used for the deployed project.
* [AWS](https://aws.amazon.com/ "Amazon Web Services") – AWS was chosen as the primary cloud service provider for the final deployment of our project. It offered robust, scalable, and secure hosting solutions for our website's databases and static files, including the digital brush files.

# Testing

## Manual testing

![Home Page](docs/pages/Home-page.png)


## Profile Page

![Profile Page](docs/pages/Profile.png)


## Brushes Page

![Brushes Page](docs/pages/Brushes.png)


## Brush Detail Page

![Brush Detail Page](docs/pages/Brush-detail.png)


## Admin Product Management Page

![Admin Product Management Page](docs/pages/Admin-product-management.png)


## Checkout Page

![Checkout Page](docs/pages/Checkout.png)


## Checkout Success Page

![Checkout Success Page](docs/pages/Checkout-success.png)


## Bag Page

![Bag Page](docs/pages/Bag.png)


## Contact Page

![Contact Page](docs/pages/Contact.png)


## Error 404 Page

![Error 404 Page](docs/pages/Error-404.png)


## Error 500 Page


![Error 500 Page](docs/pages/Error-500.png)
\
&nbsp;

### W3C CSS Validator

My css passed as well when it came to testing as I was frequently testing it in the validator.

![Css code validation](docs/code-testing/css.png)
\
&nbsp;

### JS Hint

Each of my javascript code blocks passed the validator without any major issues.

#### Confirm delete functions

![Javascript validation](docs/code-testing/confirm-js.png)
\
&nbsp;

### CI Python checker

![Python](docs/code-testing/python.png)

I checked all of my python files with the Code Institute python checker and recieved no issues with any of the files. The NOQA tag was used in the settings.py file as when I tried to rearrange some of the code to avoid the character limit, python would get upset.

### Lighthouse

![Lighthouse](docs/code-testing/lighthouse.png)

The website performed very well when it came to the lighthouse review.

## Responsiveness 
The responsiveness of the design was manually checked using the Chrome Developer Tools for various screens.

This included:
* iPhone SE
* Pixel 5
* Samsung Galaxy S8, S20 Ultra
* iPad Air and Mini
* Galaxy Fold
* Nest Hub and Hub Max

I also opted to use the responsiveness option and checked the screens at the following width sizes:
* 350px
* 768px
* 992px
* 1400px

No issues arose, due to the simple layout of the site.
\
&nbsp;

# Bugs

## Bug 1: SVG glitches

![Lighthouse](docs/bugs/Bug_1.png)
\
&nbsp;

![Lighthouse](docs/bugs/Bug_1.1.png)
\
&nbsp;

Parts of artwork exported from illustrator would be coloured black unless I exported them in a vert particular way. Some of Adobes finest work.

# Deployment

## Create Application

1. If you don't have a Heroku account, start by signing up and logging in.
2. To establish a new application, click the "new" button located at the top right corner of the dashboard, then select "Create new app."
3. Pick a distinct name for the application, indicate your residing region, and proceed by clicking "Create App."

## ElephantSQL
1. Visit elephantsql.com, log in using GitHub, and establish a fresh instance.
2. Once your project instance is set up, copy the URL. You can store this value as an environment variable to match the DATABASES variable in settings.py.
3. Utilize pip3 install dj_database_url==0.5.0 to install the dj-database-url package version 0.5.0. This will format the URL into a Django-compatible format and necessitate an update to the requirements.txt file.

## Cloudinary

1. Set up a Cloudinary account.
2. Upload relevant project images to the "Media Library."
3. Retrieve the Cloudinary API URL from your dashboard.

## Final Repo Preparations
1. Execute necessary project migrations by entering python3 manage.py makemigrations followed by python3 manage.py migrate in the terminal.
2. Integrate a Procfile into the project, including the line web: gunicorn [project_name].wsgi:application.

## Heroku Deploy
1. Return to Heroku and navigate to the Project’s page. Open the "Settings" tab and locate the "Config Vars" section.
2. Within "Config Vars," input the following key-value pairs:
   Key = PORT : Value = 8000
   Key = SECRET_KEY : Value = Your Django Secret Key from settings.py
   Key = DATABASE_URL : Value = ElephantSQL URL (from step 5)
   Key = CLOUDINARY_URL : Value = Cloudinary API URL (from step 9)
3. Proceed to the "Deploy" tab and scroll to the GitHub deployment method.
4. Search and connect to the appropriate repository by selecting the "Connect" button.
5. Continue scrolling to the bottom of the "Deploy" Page and choose your desired deployment method. Opt for "Automatically Deploy" to 
   trigger deployment with each new code push, or manually deploy by selecting the button at the page's bottom.

Your application is now successfully deployed!

# Credits

## For Code Help and Advice
* [Harry Dhillon](https://github.com/Harry-Leepz)
* [Harry Dhillon](https://github.com/Daisy-McG)

## Helpful Resources
* [Stack overflow helped a lot with problem solving.](https://stackoverflow.com/)
* [MDM also contained a lot of helpful resources when building the project.](https://developer.mozilla.org/en-US/)
* [W3 schools always has very helpful threads on anything to do with coding.](https://www.w3schools.com/)
* [Github had plenty of repositories that helped a lot with coding.](https://github.com/)
* [Geeks for geeks had a lot of great information on python.](https://www.geeksforgeeks.org/python-programming-language/)


## For Content and Code

* [Building the base of the project with the I think therefore I blog.](https://github.com/Grawnya/I-think-therefore-I-blog)
* [Lottie files webplayer creator.](https://lottiefiles.com/web-player)
* [How to create a django view.](https://www.geeksforgeeks.org/views-in-django-python/)
* [Best practice for data models.](https://cloud.google.com/appengine/docs/legacy/standard/python/datastore/datamodeling)
* [How to use django tags.](https://www.w3schools.com/django/django_template_tags.php#:~:text=In%20Django%20templates%2C%20you%20can,them%20in%20%7B%25%20%25%7D%20brackets.)
* [Checking file types with.](https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file)

&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;



