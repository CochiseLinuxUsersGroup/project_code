#!/usr/bin/python
# -*- coding:utf-8 -*-


import socket, urllib2, re, os
import urllib, httplib
from datetime import datetime
import time

USER = 'ascii'
auto_connect = True

bot_default     = USER + "_bot"
network_default = 'irc.freenode.net'
chan_default    = '#cochisetest'

if not auto_connect:
    botname = raw_input('Say my name! (' + bot_default + ') ')
    if not botname:
        botname = bot_default

    network = raw_input('IRC network? (' + network_default + ') ')
    if not network:
        network = network_default

    chatchannel = raw_input('Channel Name (' + chan_default + ') #')
    if not chatchannel:
        chatchannel = chan_default
else:
    chatchannel = chan_default
    network = network_default
    botname = bot_default

end = '\n'

start_time = str(datetime.now())[:16]

port = 6667

premess = 'PRIVMSG ' + chatchannel + ' :'
irc = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
irc.connect( ( network, port ) )
print irc.recv( 4096 )
irc.send( 'NICK ' + botname + end )
irc.send( 'USER ' + USER + 'bot botty bot bot: Python IRC' + end )
irc.send( 'JOIN ' + chatchannel + end )

# Used to store messages users leave for one another
left_messages = {}
left_priv_messages = {}

# Dictionaries of the form d == {'username1': 4, 'username2': 17}
utter_counts = {}
bot_response_counts = {}

# DO NOT CONFUSE THIS WITH irc.msg
def irc_msg(msg):
    """Sends msg to channel"""
    irc.send(premess + msg + end)
    return

def priv_msg(user, msg):
    """Sends private msg to username"""
    irc.send('PRIVMSG ' + user + ' :' + msg.strip('\r\n ') + end)

def getuser():
    """Returns nick of current message author"""
    try:
        #user = data.split()[2].strip(':')
        #user = data.split()[0].split('~')[0].strip(':!')
        user = data.split()[0].split('!')[0].strip(':')
    except:
        user = data.split('!')[0].strip(':')
    return user

def timescrapes():
    """Sends current time in given city to IRC channel"""
    html = urllib2.urlopen('http://www.timeanddate.com/worldclock/').read()
    local = 'Phoenix'
    city = data.split(':!time')[1].strip('\r\n ')
    print "city = ", city
    if not city:
        city = local
    city = ' '.join([word.capitalize() for word in city.split()]) #cap words
    print "city = ", city
    time = html.split(city)[1].split('>')[3].split('<')[0]
    irc_msg(time)
    return

def timescrapes24():
    """Sends current time in given city to IRC channel"""
    html = urllib2.urlopen('http://www.timeanddate.com/worldclock/').read()
    local = 'Phoenix'
    city = data.split(':!time24')[1].strip('\r\n ')
    if not city:
        city = local
    city = ' '.join([word.capitalize() for word in city.split()]) #cap words
    time = html.split(city)[1].split('>')[3].split('<')[0]
    if time.split()[2] == 'PM':
        hours = int(time.split()[1].split(':')[0]) + 12
        minutes = time.split()[1].split(':')[1]
        time = ' '.join([time.split()[0], str(hours) + ':' + str(minutes)])
    else:
        time = ' '.join(time.split()[:2])
    irc_msg(time)
    str(datetime.now())[:16].split()[1]
    return


loadfile = "projectlinks.txt"
i = 0
def read():
    """Reads local db"""
    dbfile = open(loadfile, 'r')
    dbold = dbfile.read()
    dbfile.seek(0)
    for line in dbfile:
        irc_msg(line)
    dbfile.seek (0)
    dbfile.close()

def empty():
    """Empties local db"""
    dbfile = open(loadfile, 'w')
    dbfile.close()

def writea():
    """Write given project info to local db"""
    dbfile = open(loadfile, 'r')
    dbold = dbfile.read()
    dbfile.close()
    link = get_content('project add')
    link = username + str(link)
    dbfile = open(loadfile, 'w')
    dbfile.write(link + str(dbold))
    dbfile.close()

def inc_bot_response_counts():
   try:
       bot_response_counts[username] += 1
       print "Bot responses to", username, " ==", bot_response_counts[username]
   except:
       try:
           bot_response_counts[username] = 1
       except:
           print "inc_bot_response_counts is REALLY broken"

def inc_utter_counts():
   try:
       utter_counts[username] += 1
       print "Utter count of", username, " ==", bot_response_counts[username]
   except:
       try:
           utter_counts[username] = 1
       except:
           print "inc_utter_counts is REALLY broken"

def get_content(keyword):
    return data.split(':!' + keyword + ' ')[1].strip('\r\n ')

while True:
   data = irc.recv ( 4096 )
   datasp = data.split(' :')[0]
   datasp = str(datasp)

   username = getuser()
   inc_utter_counts()

   if 'PING' in data:
      irc.send( 'PONG ' + data.split()[1] + end )

   if ':!quit' in data.lower():
       irc_msg("I am immortal.")

   if ':!spider' in data.lower():
       irc_msg("/X\(-_-)/X\ ")

   if ':!monkey' in data.lower():
       irc_msg("@('_')@")

   if ':!bunny' in data.lower():
       irc_msg("()()")
       irc_msg('(*-*)')
       irc_msg("""c(")(")""")


   print data

   if ':!help' in data:
       irc_msg("Options: !bunny !monkey !spider  # More to come!")
       inc_bot_response_counts()
