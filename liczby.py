#!/usr/bin/python
# -*- coding:  iso-8859-2 -*-
f= open('liczby.txt', 'r')
a= int(f.read(2))
b= int(f.read(4))
print a+b
f.close
