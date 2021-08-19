import os

lastsearchfile = open(r'/Users/gimdonghyeon/Documents/GitHub/2021-U300-pin-a-engine/lastsearch.txt', 'r')
lastsearch = lastsearchfile.readlines()

print(lastsearch)

last = int(lastsearch[0])

print(last)