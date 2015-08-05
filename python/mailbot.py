#!/usr/bin/env python
#Written by paulbe,  github code written by elimisteve

import feedparser, socket, time, pywapi, string

#Connection info for IRC
USER = 'CLUG_INFO'  #set bot name
botname     = USER #+ "_bot"
network     = 'irc.freenode.net' #set irc network to connect to
chatchannel = '#cochiselinux' #set channel to connect to
port = 6667  #set port number
end = '\n'

#IRC setup
premess = 'PRIVMSG ' + chatchannel + ' :'
irc = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
irc.connect( ( network, port ) )
print irc.recv( 4096 )
irc.send( 'NICK ' + botname + end )
irc.send( 'USER ' + USER + 'bot botty bot bot: Python IRC' + end )
irc.send( 'JOIN ' + chatchannel + end )


# Helper Functions
def irc_msg(msg):
    """Sends msg to channel"""
    irc.send(premess + msg + end)
    return

def getuser():
    """Returns nick of current message author"""
    try:
        user = data.split()[0].split('!')[0].strip(':')
    except:
        user = data.split('!')[0].strip(':')
    return user

#
# GitHub code from elimisteve, thanks!
#
account_name = 'cochiselinuxusersgroup'
branch = 'master'
repo_names = ['cochiselinuxusersgroup.github.io', 'projectcode']
SLEEP_SECONDS = float(60*2.4)/len(repo_names)  # Check each repo once/couple minutes


def force_check_github():
    old_version = {}
    for repo in repo_names:
        old_version[repo] = feedparser.parse(
            'https://github.com/' + account_name +
            '/' + repo + '/commits/' + branch + '.atom'
            )
            
    for repo in repo_names:
        new = feedparser.parse('https://github.com/' + account_name +
                               '/' + repo + '/commits/' + branch + '.atom')
        try:
			author = new.entries[0].author_detail.href.split('/')[-1]
			commit_msg = new.entries[0].title
			print '\n'
			print"[" + repo + "] " + author + ": " + commit_msg
			print '\n'
			irc_msg("[" + repo + "] " + author + ": " + commit_msg)
			
        except:
            print "GitHub fucked up, I think. Here's what they gave us:"
            print new
            
# Mail function       
def check_mail():
	new_mail = feedparser.parse("https://www.freelists.org/feed/cochiselinux")
	mail_msg = new_mail.entries[0].title
	irc_msg( mail_msg )
	return
	
# Calendar functions
def calendar():
	calendar = feedparser.parse("https://www.google.com/calendar/feeds/fp9et4ecr2c131rth7ftvfua1g%40group.calendar.google.com/public/basic")
	latest_ev = calendar.entries[0].title
	latest_sum = calendar.entries[0].summary
	if '&nbsp;' in latest_sum:
		print 'Stripping'
		stripped_sum = latest_sum.replace('&nbsp;', '')
		irc_msg( '[Next CLUG event]: ' + latest_ev + ' | ' + stripped_sum )
	else:
		irc_msg( '[Next CLUG event]: ' + latest_ev + ' | ' + latest_sum )
	return
	
			
# Weather function			
def check_weather():		
	weather = pywapi.get_weather_from_noaa('KFHU') #setup weather results ('location')
	irc_msg("Sierra Vista current weather: " + weather['temp_f'] + "F and " + weather['weather'])
	return
	
# Information function
def info():
	website = "CochiseLinuxUsersGroup.github.io"  #CLUG website
	mailing = "https://www.freelists.org/feed/cochiselinux" #CLUG mailing list feed
	irc_msg( 'Website: ' + website )
	irc_msg( 'Mailing archive: ' + mailing )
	
# Help function
def irchelp():
	irc_msg( "Available commands: ")
	irc_msg( "!info - Show website and mailing information")
	irc_msg( "!lastmail - Show the title of the latest email to the mailing list")
	irc_msg( "!lastpush - Show the last commits to github repos")
	irc_msg( "!weather - Show current weather in sierra vista")
	irc_msg( "!nextevent - Show the next calendar event")
	irc_msg( "more to come")
	return
		
# Main Loop
while True:
	data = irc.recv ( 4096 )
	datasp = data.split(' :')[0]
	datasp = str(datasp)

	username = getuser()

	if 'PING' in data:
		irc.send( 'PONG ' + data.split()[1] + end )

	if ':!info' in data.lower(): #Display info for website and mailing list
		print data
		info()
		
	if ':!help' in data.lower(): #Display help functions, list available commands
		print data
		irchelp()
			
	if ':!lastmail' in data.lower(): #Lastmail function
		print data
		check_mail()
	
	if ':!lastpush' in data.lower(): #Lastpush function
		print data
		force_check_github()
		
	if ':!weather' in data.lower(): #Weather function
		print data
		check_weather()
		
	if ':!nextevent' in data.lower(): #Calendar function
		print data
		calendar()

