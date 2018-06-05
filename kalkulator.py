#!/usr/bin/python
# -*- coding:  iso-8859-2 -*-
dzialanie = 'true'
while dzialanie != 'koniec':
	a= input("A: ")
	b= input("B: ")
	dzialanie = input("podaj dzialanie( 1.add, 2.sub, 3.mul, 4.div,): ")
	if dzialanie == '1': print (a, "+", b, "=", a+b)
	elif dzialanie == '2': print (a, "-", b, "=", a-b)
	elif dzialanie == '3': print (a, "*", b, "=", a*b)
	elif dzialanie =='4': 
		if b=='0':
			print "Nie wolno dzielic przez 0"
		print (a, "/", b, "=", a/b)



