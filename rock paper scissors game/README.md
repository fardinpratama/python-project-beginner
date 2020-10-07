=============================================
Rock Paper Scissors Game  
=============================================

By : Fardin Pratama Yudha

This is a simple suit game game that uses the "pygame" library as 
its GUI and uses an object oriented programming paradigm. the workflow
is to compare the player's choice with a random enemy selection using 
a "random" library.

The game is started by clicking the start text or pressing the "Space" key, 
after which the player types "suit" by clicking one of the button icons 
provided while holding. the result will appear after the player one of the buttons. 
The game can be the player pressing the text "play again" or the "room" key and 
the score will continue to grow. let's play and check your lucky level today.
good luck.

algorithm used:
1. Change the suit type to the form of a number:
    - rock = 1
    - paper = 2
    - scissors = 3
2. Take the "player" option then reduce it by the choice "enemy"
3. analyze the results:

    R - R = 0 ()
    R - P = -1 (loss)
    R - S = -2 (win)

    P - P = 0 (draw)
    P - R = 1 (win)
    P - S = -1 (loss)

    S - S = 0 (draw)
    S - R = 2 (loss)
    S - P = 1 (win)

    - if the result 1 or -2 then "player" win
    - if the reslut 0 then draw
    - other than the value above the "player" loses