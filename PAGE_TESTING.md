# Preference Page
Page Description: <br>
* The Preference Page empowers users to tailor their recipe recommendations to their dietary restrictions and preferred cuisines. This page provides a user-friendly interface for users to specify their dietary restrictions and preferred cuisines. <br>
![Mockup of Preference Page](https://i.imgur.com/MPUmmpd.png)

Parameters Needed: <br>
* User ID: To link the user's preferences with their account and ensure personalized recommendations.

Data Needed to Render the Page: <br>
* User's existing dietary restrictions and preferred cuisines (if available) <br>
* A list of dietary restriction options (e.g., vegetarian, vegan, gluten-free) <br>
* A list of cuisine options (e.g., Italian, Mexican, Chinese) <br>

Link Destination: <br>
* Be able to navigate to Vault page <br>
* Be able to navigate to Search page <br>
* Be able to navigate back to user's profile page <br>
* Be able to navigate to other pages on website through other links provided/generated as needed through development of website <br>

Tests for Verifying Rendering: <br>
* Verify that the user's existing preferences (if available) are pre-selected in the form. <br>
* Test the functionality of the dietary restriction and cuisine selection interfaces. <br>
* Ensure that any changes to preferences are saved when the form is submitted. <br>
* Verify that updated preferences result in tailored recipe recommendations on other parts of the application. <br>
* Verify user can navigate to other portions of website from this page. <br>

# Login Page
Page Description: <br>
* Allows users to login to their existing account, has links to sign up as well.
![Wireframes](https://github.com/Team1-3308-Fall2023/3308-Project-Team_1/assets/134562390/c562a24d-b1a4-4c83-a88c-c4ba3c052616)

Parameters Needed: <br>
* First and Last Name
* Username (must be Unique)
* Email
* Password
* Phone Number (optional)

Data Needed to Render Page:
* Dimensions of login/signup page
* Dimensions of input boxes
* Input box titles
* Input box placeholder text
* Colors
* Page title
* Fonts 
* List of existing users including usernames

Link Destinations: <br>
* Sign-up: extra text boxes to sign up vs. login
* Login: takes user to their VAULT PAGE

Tests for Page: 
* Ensure that login page opens upon visiting site
* Ensure sign-up button adds extra text boxes for info
* Ensure correct formatting for all text box inputs ( i.e. phone number, email has @, etc.
* Ensure unique username, phone number to prevent duplicate accounts

# Vault Page: 
Page Description: <br>
This page displays a users saved recipes and categories.

![Wireframes(1)](https://github.com/Team1-3308-Fall2023/3308-Project-Team_1/assets/134562390/ee579d0e-0d36-46ea-8e11-e88a9f9d39b5)

Parameters Needed: <br>
* User’s recipes
* User preferences(Organization, Name, Colors, Settings, Categories)

Data Needed for Rendering: <br>
* Dimensions of recipe tiles
* Dimensions of page header
* Dimensions of Search bar
* Dimensions of side menu
* Filtering options
* User information
* User recipes
* Recently accessed recipes
* Recipe info for each recipe tile
* Category Separation

Link Destinations:
* Can return to Home page
* Can go to Search/Explore page
* Can pop up error pages if occurring

Tests for Page: 
* Test links to other pages
* Test adding/removing recipes and categories
* Ensure that all added recipes are present
* Ensure that user information and preferences are displayed correctly
* Ensure HTML/CSS elements are displayed correctly
* Ensure that errors pop up when necessary

# Search Page:

Page Description: <br>
On this page, users can browse recommended/popular recipes, and search for new ones with filtering
![Wireframes(2)](https://github.com/Team1-3308-Fall2023/3308-Project-Team_1/assets/134562390/07277820-7189-490b-ae7d-bd6bfe00f94a)

Parameters Needed: <br>
* List of recipes by popularity
* User preferences
* Username visible
* Colors
* Settings
* Available filters
* Sort-by categories
* User vault page link to save to

Data Needed for Rendering: <br>
* Dimensions of recipe tiles
* Dimensions of page header
* Dimensions of Search bar
* Dimensions of side menu
* Filtering options
* User information
* Popular recipe (sorted list)
* Recipe info for each recipe tile
* Category information for each recipe
* User saved recipes

Link Destinations: <br>
* Can return to Home page
* Can go to login page
* Can go to vault page
* Can pop up error pages if occurring

Tests For Page: <br>
* Test links to other pages
* Test adding/removing recipes to vault page
* Test search function and recipe tags/categories
* Ensure that user information and preferences are displayed correctly
* Ensure HTML/CSS elements are displayed correctly
* Ensure that errors pop up when necessary



# Recipe Page:

Page Description: <br>
* The Recipe Page displays a give recipe and all the information required to make that recipe. Users are also able to rate the recipe, save the recipe, and leave a comment if the wish to.<br>
<img src="https://tinypic.host/images/2023/10/25/recipe_page.png">

Parameters:<br>
* User ID<br>
  - Needed to link the users rating of the meal to their account to influence personalized recommendations<br>
  - Needed so that user can save recipe to their unique vault if they want to<br>
<br>

Data Needed to Render Page: <br>
* Recipe Titles
* Recipe prep time
* Recipe cook time
* Recipe serving size
* List of ingredients needed for recipe
* Cooking Instructions
* Comments previously posted on recipe

Links to other Destinations:<br>
* Link to Vault page
* Link to Search page
* Link back to user's profile page
* Links to any other pages deemed necessary during development of website

Tests to Verify Rendering:<br>
* Ensure that when another destination is selected, the link works and the user is taken to the correct page.
* Test the functionality of one user leaving a comment and it still being there when another user views the same recipe.
* Ensure that any changes to ratings remain after the user leaves the page
* Verify that a new or updated rating will influence the recipe recommendations on other parts of the application.



# Error Page:

Page Description: <br>
* The error page will be used to redirect users after making a bad request or trying to use a feature they don't have access to.<br>

![Invalid Address](images/invalid_address.png)
![Not a User](images/not_a_user.png)

Parameters:<br>
* User ID needed to verify if the user has an account or not (or not logged in)<br>
 

Data Needed to Render Page: <br>
* User error type


Links to other Destinations:<br>
* Link to home page
* Link to previous page
* Link to create an account
* Link to login page


Tests to Verify Rendering:<br>
* Test to make sure links return user to previous page, home page, create an account and login page
* Test to make sure user without an account are redirected to error page stating they need an account to access said functionality




# Home Page:

Page Description: <br>
* The home page is the default page when the user visits the website. It will have many features to direct the user to their current needs. <br>

<img width="552" alt="Screenshot 2023-10-26 at 6 47 52 PM" src="https://github.com/Team1-3308-Fall2023/3308-Project-Team_1/assets/97182468/950a2672-8b8c-45fc-a857-e8fff5e115f6">

Parameters: <br>
* Users Saved Recipes
* Users Preferences to recommend recipes within range
* History of recently viewed recipes

Data Needed to Render Page: <br>
* Images and multimedia (images, descriptions and titles of recipes)
* Links to recipes

Links to other Destinations: <br>
* Sign-in Page
* Saved Recipes
* Trending Recipes
* Occasional Recipes
* Recipes (random recipes to browse)
* Recipe of the Day
* Recently Viewd Recipes

Test to Verify Rendering: <br>
* Test to make sure each destination is the correct pathway.
* Ensure search bar works properly
* Images and multimedia work correcly and are not broken


