!# /bin/bash

#Written by David Garcia
#This script takes user selected options and outputs the desireed command



clear

while true;
do
	echo "Please choose an option below to run your command."
	echo "1. List Files In Current Directory"
	echo "2. Print Current Working Directory"
	echo "3. Print Current Date and Time"
	echo "4. Show Currently Logged in users"
	echo "5. Exit"

echo -n "Please choose an option. (1-5): "
read userchoice

case "$userchoice" in

	1)
	ls -l
	echo "Press enter to continue"
	read
	clear
	;;
	
	2)
	pwd
	echo "Press enter to continue"
	read
	clear
	;;
	
	3)
	date
	echo "Press enter to continue"
	read
	clear
	;;
	
	4)
	w
	echo "Press enter to continue"
	read
	clear
	;;
	
	5)
	break
	;;

	*)
	echo "Please enter 1-5 as an option"
	read
	clear
	;;	

esac

done
