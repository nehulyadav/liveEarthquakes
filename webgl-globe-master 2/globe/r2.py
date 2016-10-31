from ast import literal_eval
import json

s = open ("input.json").readline()
s = literal_eval("'%s'" % s)
s = "[" + s[2:len(s)-6] + "]"
s = s.replace('""', '["')

f = open("input.json", "w")
f.write(s)
