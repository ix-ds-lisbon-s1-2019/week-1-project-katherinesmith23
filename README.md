# ix-lisbon-project-week-1

Here is the repo with the project brief and where you should push your final poker game .py file. Might be a good idea to edit this README to include a link to your blog (where in a post you should link this repo too) :) 

The deadline is **tomorrow (Friday) the 31st of May at 8pm**.


My blog link:
https://katherinesmith23.github.io



My article about how to create a poker game:

In order to make a poker game, you have to follow a couple of steps:

•	First, you need to ask the computer user for the number of players in the game.  This can be done using the simple input() function.  

•	Then, you need to ask the computer user to enter the names of all of the players.  This again can be done with the input() function.  

•	Next, the program must deal out cards to all of the players.  This can be done by creating a simple list of all of the cards in the deck, and then randomly picking cards from this list.  Using a for loop, you can select 5 cards for each person and store them in a new list for each person.

    o	It is important to note that after these cards are added, they should be removed from the list of total cards.  This ensures that there will not be more cards of each number/face dealt than possible.
  
•	These players and each of these lists should be added to a dictionary.  The key should be the player name and the value should be the card list.

•	Lastly, the code needs to compare all of the hands to find the winner.  There are a couple ways to do this, but I chose this one:

    o	Sort each player’s hand in descending order
  
    o	Originally set a variable called “max” to 1 (lower than all possible card values)
  
    o	Check the first card in each hand
  
    o	If the first card of a player’s hand is greater than the max, it becomes the new winner
  
    o	If the first card of a player’s hand is equal to the max, it is added to the winners list, as these two players are currently tied
  
    o	If the first card of a player’s hand is less than the max, do nothing, as this player is not the winner
  
    o	Using a while list, continue this process for all five cards in each hand for as long as the winners list is greater than one (as this illustrates that there is still a tie)
  
    o	Finally, there should be only one player remaining in the winners list and this is the final winner of the poker game
