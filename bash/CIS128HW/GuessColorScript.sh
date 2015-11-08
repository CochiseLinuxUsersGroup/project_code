#! /bin/bash
#Written By David Garcia
#This Script Allows the user to attempt to guess my favorite color

clear

echo -n "What is my favorite color? "
read Color
if [ "$Color" = "lime green" ]
then
	echo "Yes My Favorite Color is lime green."
else
	echo "Nope! Guess Again!"
fi 
