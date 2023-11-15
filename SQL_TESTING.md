## SQL Testing - Team 1 <br>
### Linnea Fritz-Watson, Anthony Le, Brooke Neupert, Spencer Oram, Rebecca Toland

This document outlines the various SQL tables that will be used in the RecipeVault website project <br>
### Category Table: <br>
#### Description:
- Contains the possible categories that a recipe could be placed into. This table will contain the recipes that fall into each of the meal categories so that search results can be filtered to only show that category of meal
#### Table Items: 
- Breakfast: Contains all recipes that are breakfast recipes
- Lunch: Contains all recipes that are lunch recipes
- Dinner: Contains all recipes that are Dinner recipes. There may be some overlap with lunch.
#### Tests: 
- Insert Test:
  - If a category is selected under a recipe, that recipe is added to that category
- Delete Test:
  - If a category is removed from a recipe, then that recipe is removed from that table group.
##### Data Access Tests:
- If no categories are selected, all recipes appear (default to all recipes being shown)
  - User case name:
    - Verify Default page appearance
  - Description:
    - Ensures that all recipes are shown when no categories (filters) are selected
  - Pre-Conditions:
    - Recipe Database must be stocked and accessible
    - Filter Dropdown menu works
    - Recipes are tagged with categories
    - Search and VAult pages exist
  - Test Steps:
    1. Navigate to Search Page
    2. Open Filter Menu next to search bar
    3. Under "Meals" ensure no categories are selected
    4. Open recipe tiles on page to ensure that recipe tiles of all three categories are displayed
  - Expected Result:
    -Recipe tiles of all three categories are displayed
  
- If all categories are selected, all recipes appear.
  - User case name:
    - Verify all recipes are covered under at least one category
  - Description:
    - Ensures that all recipes are covered under a category label, so that when all categories are selected, all recipes are shown
  - Pre-conditions:
    - Recipe Database must be stocked and accessible
    - Filter Dropdown Works
    - Recipes are tagged with categories
    - Search and Vault pages exist
  - Test Steps:
    1. Navigate to Search Page
    2. Open Filter Menu next to search bar
    3. Under "meals" check all categories
    4. Ensure that recipes with all category tags are displayed. 
- For each category if it is selected alone, only the recipes in that category are shown
  - User Case Name:
    - Verify that filtering works for single category tags
  - Description:
    - Ensures that filtering works; when a category is selected only recipes in that category are shown
  - Pre-Conditions:
    - Recipe Database must be stocked and accessible
    - Filter Dropdown works
    - Recipes are tagged
    - Search and Vault pages exist
  - Test Steps:
    1. Navigate to Search Page
    2. Open filter dropdown menu
    3. Select each category one at a time
    4. Check the displayed recipe tiles to ensure that only recipes tagged with that category are shown
    5. Repeat in Vault page
- if two categories are selected, then none of the recipes in the other category are shown (unless they overlap)
  - User Case Name:
    - Verify that filtering works when multiple categories are selected
  - Description:
    - Ensures that filtering works; when multiple categories are selected only recipes in those categories are shown
  - Pre-Conditions:
    - Recipe Database must be stocked and accessible
    - Filter Dropdown works
    - Recipes are tagged
    - Search and Vault pages exist
  - Test Steps:
    1. Navigate to Search Page
    2. Open filter dropdown menu
    3. Select each category two at a time; check all combinations
    4. Check the displayed recipe tiles to ensure that only recipes tagged with the selected category tags are shown
    5. Repeat in Vault page
- recipes with both categories show up if either one of those categories is selected
  - User Case Name:
    - Verify that filtering works when a recipe has multiple category tags
  - Description:
    - Ensures that filtering works; when a recipe has multiple category tags it shows in the filtering/search results for either category
  - Pre-Conditions:
    - Recipe Database must be stocked and accessible
    - Filter Dropdown works
    - Recipes are tagged
    - Search and Vault pages exist
  - Test Steps:
    1. Navigate to Search Page
    2. Find an example recipe with two category tags
    3. Open filter dropdown menu
    4. Select each category the recipe is tagged as one at a time
    5. Check that the example recipe shows in each of the filtered searches
    6. Repeat in Vault page



### Tables

    Table Name: User
    Description: This table contains information pertaining to each individual user that has created a profile on the application. This table will also be used as a reference for the savedRecipes table to ‘connect’ individual users to their list of saved recipes. 
    Fields
        UserID (Primary Key): INT ID 
        Username: Contains user’s preferred username that will be displayed in app
        Email (Unique)(could be the Primary Key instead): Contains the users unique email address
        Password (Unique): Contains the users unique password
    Tests
        Primary Key Constraint Test:
            Check if the userID is unique for each record
            Ensure that there are no NULL values in the userID column
            Ensure none of the values are negative values
        UNIQUE Constraint Tests:
            Verify that the Username, Email, and Password columns do not contain duplicate values.
            Ensure that UserID, Email, and Password columns do not contain NULL values 
        Data Integrity Test:
            Confirm that the userID in the User_table is used as a foreign key in savedRecipes, userDietaryPreferences, ratings, and comments tables
        Data Consistency Test:
            Validate that the data in Username, Email, and Password columns is consistent with the defined constraints
        Insert Test:
            Insert a new user with a userID, Username, Email, and Password and confirm that the record is successfully added to the table 
            Confirm that users attempting to create a new account with an Email OR Password that is already in the system is declined
        Update Test:
            Update an existing user's information (e.g., change the Username, Email, AND/OR Password) and ensure that the changes are reflected correctly
        Delete Test:
            Delete a user from the table and confirm that it is removed without affecting other records
        Boundary Value Test:
            Test with extreme values to ensure that the table handles them correctly (e.g. exceptionally long username or email)
        Authentication Test:
            Test the login process to verify that users can sign-in using their username and password

<br>
<br>
<br>

    Table Name: DietaryPreferences
    Description: This table holds data pertaining to dietary preferences. It is also used as a reference to the userDietaryPreferences table which links to the user table. 
    Fields
        PreferenceID (Primary Key): INT ID 
        PreferenceName (e.g., Vegan, Gluten-Free, Vegetarian): Contains information regarding dietary preferences
    Tests
        Primary Key Constraint Test:
            Check if the PreferenceID is unique for each record
            Ensure that there are no NULL values in the PreferenceID column
            Ensure there are no negative values
        PreferenceName Constraint Test:
            Verify that the PreferenceName column does not contain NULL values.
            Ensure that the PreferenceName values are valid and adhere to the defined preferences (e.g., Vegan, Gluten-Free)
        Data Integrity Test:
            Confirm that the PreferenceID in the DietaryPreferences table is properly used as a foreign key in the userDietaryPreferences table

<br>
<br>
<br>

    Table NAme: UserDietaryPreferences 
    Description: This table serves as the ‘middle-man’ table to connect users and their dietary preferences. This enables a user to have multiple dietary preferences such as Gluten Free and Vegan. 
    Fields
        UserID (Foreign Key referencing Users.UserID): INT
        PreferenceID (Foreign Key referencing DietaryPreferences.PreferenceID): INT
    Tests
        Foreign Key Constraint Test:
            Check if the UserID and PreferenceID columns have foreign key constraints that reference the UserID in the Users table and PreferenceID in the DietaryPreferences table, respectively.
            Confirm that there are no orphaned records (records with non-existent foreign keys that could happen in a user deletion or such)
        Insert Test:
            Insert a new record into the UserDietaryPreferences table with a valid UserID and PreferenceID and confirm that the record is successfully added
        Update Test:
            Update an existing record in the UserDietaryPreferences table and ensure that the changes are reflected correctly
        Delete Test:
            Delete a record from the UserDietaryPreferences table and confirm that it is removed without affecting other records
        Cascade Deletion Test:
            Test if the deletion of a user or a dietary preference in the respective tables cascades to delete associated records in the UserDietaryPreferences_table
        Data Integrity Test:
            Check if changes in the Users table (e.g., deletion of a user) or the DietaryPreferences table (e.g., deletion of a dietary preference) are handled appropriately in the UserDietaryPreferences table (this kind of goes along with the Cascade Deletion Test)
        Query Test:
            Execute queries to retrieve data from the UserDietaryPreferences table and verify that the results match expectations.

<br>
<br>
<br>

    Table Name: SavedRecipes
    Description: This table stores the relationship between users and the recipes they have saved. It links user profiles to their saved recipe IDs.
    Fields:
        UserID (Foreign Key referencing Users.UserID): INT
        RecipeID (Foreign Key referencing Recipes.RecipeID): INT
    Tests:
        Foreign Key Constraint Test:
            Ensure UserID and RecipeID references an existing UserID in the Users table and existing RecipeID in the Recipes table
        Data Consistency Test:
            Validate that the combination of UserID and RecipeID is unique, ensuring that a user cannot save the same recipe multiple times
        Insert Test:
            Insert a new entry into the SavedRecipes table with a valid UserID and RecipeID, and confirm that it is successfully added.
        Delete Test:
            Remove a saved recipe record from the table and verify that it is deleted without affecting other records.
<br>
<br>
<br>

    Table Name: Ratings
    Description: This table stores user ratings for recipes, indicating their satisfaction with a particular recipe on a scale of 1 to 5.
    Fields:
        UserID (Foreign Key referencing Users.UserID): INT
        RecipeID (Foreign Key referencing Recipes.RecipeID): INT
        Rating (constraint where Rating >= 1 AND Rating <= 5): INT
    Tests:
        Foreign Key Constraint Test:
            Ensure that the UserID in Ratings references an existing UserID in the Users table.
            Verify that the RecipeID in Ratings references an existing RecipeID in the Recipes table.
        Data Consistency Test:
            Validate that the Rating field contains values within the range of 1 to 5.
        Insert Test:
            Insert a new rating with a valid UserID, RecipeID, and Rating, and confirm that it is successfully added.
            Verify that a rating that is outside our defined constraint (Rating >= 1 AND Rating <= 5) can't be added
        Update Test:
            Update an existing rating to change the Rating value and ensure that the change is correctly reflected.
    
<br>
<br>
<br>

    Table Name: Comments
    Description: This table stores comments made by users on recipes, including the comment text, the user who posted it, and the date it was posted.
    Fields:
        CommentID (Primary Key): INT
        UserID (Foreign Key referencing Users.UserID): INT 
        RecipeID (Foreign Key referencing Recipes.RecipeID): INT 
        CommentText: TEXT (can add constraint where users are only allowed to type x amount of characters/words for a comment)
        DatePosted: DATETIME
    Tests:
        Foreign Key Constraint Test:
            Ensure that the UserID in Comments references an existing UserID in the Users table.
            Verify that the RecipeID in Comments references an existing RecipeID in the Recipes table.
        Prinmary Key Constraint Test:
            Confirm that CommentID is unique for each record in the Comments table.
        Insert Test:
            Insert a new comment with valid UserID, RecipeID, CommentText, and DatePosted, and confirm that it is successfully added.
        Update Test:
            Update an existing comment to modify the CommentText or DatePosted, and verify that the changes are reflected correctly.
        Delete Test:
            Delete a comment from the table and confirm that it is removed without affecting other records.
        Boundary Value Test:
            Test with very long CommentText and DatePosted values to ensure the table handles them correctly.
        Data Consistency Test:
            Validate that DatePosted values are in the correct date format and that CommentText follows character limits if any are defined.
    
<br>
<br>
<br>

### Data access methods

       Use case name : 
            Verify login with valid user name and password
        Description:
            Test the Recipe Vault login page
        Pre-conditions (what needs to be true about the system before the test can be applied):
            User has valid user name and password
        Test steps:
            1. Navigate to login page
            2. Provide valid user name
            3. Provide valid password
            4. Click login button
        Expected result:
            User should be able to login 
        Actual result (when you are testing this, how can you tell it worked):
            User is navigated to either the home page with their username displayed in an upper corner OR taken to their profile page (haven't decided yet) with successful login
        Status (Pass/Fail, when this test was performed)
            Unknown, haven't completed test yet
        Notes:
            N/A
        Post-conditions (what must be true about the system when the test has completed successfully):
            User is validated with database and successfully signed into their account.
            The account session details are logged in database. 
