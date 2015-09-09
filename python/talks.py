#test talks.json script
import os;
import datetime;


td_date = datetime.date.today().strftime("%Y-%m-%d")
json_choice = raw_input("Would you like to add a talk? [yes/no] ")

if json_choice in {"Yes", "yes", "Y", "y"}:
	os.system("head -n -2 talks/talks.json > talks/temp.json ; mv talks/temp.json talks/talks.json")
		
	name = raw_input("Please enter the name of your talk. [Required] ")
	while not name:
		print "You didnt enter a name for the talk."
		name = raw_input("Please enter the name of your talk. [Required] ")
	
	title = raw_input("Please add a title for the talk. [Required]")
	while not title:
		print "You didnt enter a title for the talk."
		title = raw_input("Please add a title for the talk. [Required]")
		
	talk_date = raw_input("Please enter the date the talk will take place. [yyyy-mm-dd] ")
	while not talk_date:
		print "You didn't enter a date, using today's date."
		talk_date = td_date
		
	os.system("echo -e '\t''}, {' >> talks/talks.json")
	os.system("echo -e '\t''\t''\"'name'\"': '\"'" + name + "'\"'',' >> talks/talks.json")
	os.system("echo -e '\t''\t''\"'title'\"': '\"'" + title + "'\"'',' >> talks/talks.json")
	os.system("echo -e '\t''\t''\"'date'\"': '\"'" + talk_date + "'\"'',' >> talks/talks.json")
	
	url = raw_input("Enter the url for the talk: [Optional] ")
	if not url:
		os.system("echo -e '\t''\t''\"'url'\"': '\"''\"'',' >> talks/talks.json")
	else:
		os.system("echo -e '\t''\t''\"'url'\"': '\"'" + url + "'\"'',' >> talks/talks.json")
	
	os.system("echo -e '\t''\t''\"'country'\"': '\"'us'\"'',' >> talks/talks.json")
	os.system("echo -e '\t''\t''\"'city'\"': '\"'Sierra Vista, AZ'\"' >> talks/talks.json")
	os.system("echo -e '\t''}' >> talks/talks.json")
	os.system("echo -e ] >> talks/talks.json")
	
if json_choice in {"No", "no", "N", "n"}:
	print "Not creating a new talk, here are a list of existing talks. "
	os.system("less talks/talks.json | grep title | awk '{print $2, $3, $4}' | sed 's/,//' | sed 's/\"//g' |  nl")



'''
title - done
name - done
url - done
date - done
country/city Sierra Vista, USA
'''
