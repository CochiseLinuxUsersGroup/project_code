#! /bin/bash
#written by David Garcia
#this script is a loop guessing of my favorite color

echo "What is my favorite color?"; read FavColor
while [ "$FaveColor" != "lime green" ] ; do
	echo "Nope, You guessed wrong! "; read FaveColor
done

echo "Yes you got it!"
