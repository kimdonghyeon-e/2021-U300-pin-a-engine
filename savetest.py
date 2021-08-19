import os

lastsearchfile = open('/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/lastsearch.txt', 'r')
lastsearch = lastsearchfile.readlines()
last = int(lastsearch[0])
print(last)

wfile = open('/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/lastsearch.txt', 'w')
wfile.write(str(1))
