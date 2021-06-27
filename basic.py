#!/usr/bin/python3

print("content-type:text/html")
print()

import subprocess as sp  #equilv to system func
import cgi

y = cgi.FieldStorage()
cmd = y.getvalue("x")

out = sp.getoutput("sudo "+cmd)
print(out)
