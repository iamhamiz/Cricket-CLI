import feedparser
import re
global choice


d = feedparser.parse('http://static.cricinfo.com/rss/livescores.xml')
"""
print India
print Australia
print Pakistan
print SouthAfrica
print NewZeland
print
print
print
print
print
print
print
"""
choice = "(.*)(P|p)akistan(.*)" | "(.*)(P|p)akistan(.*)" 
for (index,post) in enumerate(d.entries):
    if re.match(choice,post.title):
        print d['feed']['title']
        print post.title
f = feedparser.parse('http://www.espncricinfo.com/rss/content/story/feeds/0.xml')

for (index,post) in enumerate(f.entries):
    if re.match(choice,post.title):
        print f['feed']['title']
        print post.title