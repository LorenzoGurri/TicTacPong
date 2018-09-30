# TicTacPong
TicTacToe but players can challenge other players moves with a game of pong

## Rules:
* Just like regular game of TicTacToe, three in a row in any direction is a win for either player
* After a player moves the other player is allowed to challenge that move. Players cannot challenge past moves and can only challenge a given move once.
* When the challenge button is pressed, a game of pong is started.
* The challenger <b>always</b> uses the w and s keys and the defender <b>always</b> uses the up and down arrow keys.
* The first player to get three points wins pong. If the challenger wins, they are able to take the spot and then move again, if they loose, they loose their turn as well.

## Pictures:

![TicTacToe preview](img/ttt.png "TicTacToe")

![Pong preview](img/pong.png "Pong")

## TODO:
### v1.0
- [x] Rename TicTacToe window to TicTacPong
- [x] Make it so players can only challenge a move once (challenge button disabled)
- [x] Make it so a challenging player looses his turn if he looses the challenge
- [x] Add a count down before the pong game starts
- [x] Remove all print statements and replace them with popup windows
- [x] Document code better
### v1.1
- [ ] Improve movement of pong paddles
- [ ] Add a turn indicator
- [ ] Make code cleaner
