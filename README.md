# ULTIMATE Battleships
## How to play
## Features
## Data Model
## Testing
## Bugs
### Solved Bugs
- **Stuck in a While Loop:**
    When playing the original game, I noticed that once either the player or the computer had won, the terminal only prompted to continue and did not give the option to exit. This was a feature I was looking to add. The issue I found was that when playing the first match, leaving the game was not a problem, but if you continued to play a new game and then went to leave the second game, the break function would only throw you out of the loop and into the function, thereby repeating itself and leaving you stuck in the game.

    I had a tutoring session with Code Institute to help me with the debugging, adding print statements in each function to help indicate where I was at within the loops and functions. After many hours of trying different methods, the only way I found that could make it work was by adding a global variable, PLAY_GAME, which was set to true unless the player prompted otherwise, thus taking them out of the game. This global PLAY_GAME variable is used to close off the while loop if it does not return true.

    What I found interesting was that the function would continue to try and enter the while loop for the number of times a new game was played. So, I added a global LOOP_COUNTER and a COLOR list that would change the color of a print statement and count up each time it was printed, indicating the number of times it had taken to break out of the loop, or how many times the player had started a new game.

- **Giving the same Random Values**
    Fixed a bug where the ship was not being appended to the board correctly. I forgot that the random function can generate the same values multiple times, which sometimes resulted in only 3 ships being printed instead of 4. To fix this, I put the random functions in a while loop with an if statement.

After uploading to Heroku, I realized that the logic I used to break out of the while loop in the play_game function was incorrect. Instead of crashing the game to access the terminal, it should remain in a continuous loop. So, I called the new_game function instead and adjusted the output messages for a better user experience. I also decided to keep the loop counter and color list to add a bit of character and as a reminder to myself to push to Heroku earlier for testing.

### Remaing Bugs
## Testing
### Manual Testing
### Validator Testing
## Deployment
## Credits
- Code Institute for the [ULTIMATE Battleships game](https://p3-battleships.herokuapp.com/)
- [Colorama](https://pypi.org/project/colorama/) for colors in terminal
- [W3S](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [Python Forum](https://python-forum.io/index.php)