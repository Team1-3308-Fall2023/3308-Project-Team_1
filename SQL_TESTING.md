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
  -
- If all categories are selected, all recipes appear.
- For each category if it is selected alone, only the recipes in that category are shown
- if two categories are selected, then none of the recipes in the other category are shown (unless they overlap)
- recipes with both categories show up if either one of those categories is selected
  
