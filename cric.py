from bs4 import BeautifulSoup
import requests
import time
import sys, os
import subprocess as SE

cricinfoRss = 'http://static.cricinfo.com/rss/livescores.xml'

def getURLtext(url):
    retryCount = 5
    r = requests.get(url)
    while r.status_code is not 200:
        if retryCount == 0:
            print 'Check your internet connectivity'
            sys.exit(1)
        retrycount -= 1
        print 'Request failed, trying again..'
        time.sleep(3)
        r = requests.get(url)
    data  = r.text
    soup = BeautifulSoup(data)
    return soup

def findMatches():
    global allMatches
    liveMatches = getURLtext(cricinfoRss)
    allMatches = liveMatches.find_all('description')

    if len(allMatches) > 1:
        askUser()

def askUser():
    global choice
    for index, game in enumerate(allMatches[1:], 1):
        print '%d.'%index , str(game.string)
    
    choice = int(input('Choose preferred match:\n'))

    while True:
        if choice in range(1, index + 1):
            break
        choice = int(input('Invalid Choice. Enter your choice: '))

def guiNotify(message):
    if os.path.isfile('/etc/lsb-release'):
        SE.Popen(['notify-send', message])

def getScore():
    scoreURL = str(allMatches[choice].find_next_sibling().string)
    mainPage = getURLtext(scoreURL)
    score = str(mainPage.title.string).split('|')[0]
    inningsReq = mainPage.find("div", { "class" : "innings-requirement" }).string.strip()
    message = score + inningsReq
    guiNotify(message)
    print message

try:
    findMatches()
    getScore()
    notify = raw_input('Would you like to get notification?\nEnter (y|n)\n>')
    if notify == 'y':
        min = int(input('How many minutes once you would like to get notified?\nEnter min>') )
        while True:
            time.sleep(min * 60)
            getScore()
except KeyboardInterrupt:
    print 'keyboard interrupted, program end'