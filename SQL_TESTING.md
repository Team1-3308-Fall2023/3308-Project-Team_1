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
