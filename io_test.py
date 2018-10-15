#!/usr/local/bin/python3

# Sample program to demonstrate input and output using variables and math basic functions
import os

v_pi = 3.1415926535
area = 0
circumference = 0

v_unused = os.system('clear')
v_rad = input("Enter the radius of your circle: ")

area = float(v_pi) * (float(v_rad) ** 2)
circumference = float(2) * float(v_pi) * float(v_rad)

print ("The area of the circle is: ", area)
print ("")
print ("The circumference of the circle is: ", circumference)

quit()
