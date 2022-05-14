# Tipovací hra

This application/game is used for automatic football results scraping. It allows the user to add players and show their current score which is determined by how well they guessed the results of the matches.
Application provides basic GUI with all different statistics. For more info about the application interface read "Nápověda" at the main menu.
After selecting "Přidat hráče" option at the main menu, the user is asked to enter his name and select CSV file with his guesses. The CSV file must meet the given requirements:
    
1.  Always use the pre-pared table "csv/import_file.csv", just edit it.
2.  Every row represents one guess
3.  Player must guess every result of match during group stage, so he needs to fill in the score into column 4 and 5
4.  During knockout stage (every other phase than Group Stage) player guesses only the team that goes through. For example, in a row that starts with "Final" the player guesses the two teams that he thinks will get to the final.
5.  See "tests/csv/test_XXt.csv" for correctly filled in tables
    
This is actually the only non automatic feature in the app. All users must fill in the table and send it to the person who runs the application. He will add their tables to the game and from that point the user can see their points and all statistics.

Often times you can find "gs" and "ks" in the code which stands for "Group Stage" and "Knockout stage". For more information about this and all functionalities of the app read report "moravp15.pdf" in Czech. 


*  **Necessary dependencies to install: "requirements.txt"**
*  **To start the app execute in terminal: "python3 -m app.src.main" in the top folder "moravp15"**
*  **To run the tests execute in terminal: "python3 -m pytest tests" in the top folder "moravp15"**


First opening of the app could take a few seconds, because of scraping all the matches.

The app automatically downloads the data from sport website during opening the program and selecting "Souhrn hry" or "Procházet hráče" options at the main menu. If the user wants to update results from the internet manually, he/she can click on "Aktualizovat" button.

"src/list_of_teams.csv" contains list of all teams in the competition,
"src/group_stage_matches.csv" contains all duels in the group stage