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
![Mockup of Preference Page]([https://i.imgur.com/MPUmmpd.png](https://drive.google.com/file/d/164VOGlIfSgzPD1_9R3J9XRjrCB7_c10g/view?usp=sharing))

Parameters:<br>
<br>
*User ID<br>
    - Needed to link the users rating of the meal to their account to influence personalized recommendations<br>
    - Needed so that user can save recipe to their unique vault if they want to<br>
    <br>
Data Needed to Render Page:<br>
*Recipe Titles<br>
*Recipe prep time<br>
*Recipe cook time<br>
*Recipe serving size<br>
*List of ingredients needed for recipe<br>
*Cooking Instructions<br>
*Comments previously posted on recipe<br>
<br>
Links to other Destinations:<br>
*Link to Vault page<br>
*Link to Search page<br>
*Link back to user's profile page<br>
*Links to any other pages deemed necessary during development of website<br>
<br>
Tests to Verify Rendering:<br>
*Ensure that when another destination is selected, the link works and the user is taken to the correct page.<br>
*Test the functionality of one user leaving a comment and it still being there when another user views the same recipe.<br>
*Ensure that any changes to ratings remain after the user leaves the page<br>
*Verify that a new or updated rating will influence the recipe recommendations on other parts of the application.<br>



