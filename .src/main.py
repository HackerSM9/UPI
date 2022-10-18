import os,sys

r = '\033[1;31m'
y = '\033[1;33m'
v = '\033[1;34m'
e = '\033[0m'
q = y+'['+r+'?'+y+']'+e

print("\n")
pa = input("[?] Enter UPI ID: ")
pn = input("[?] Enter Name: ")
am = input("[?] Enter Amount: ")

print("\nUPI is Ready: UPI://pay?pa={0}&pn={1}&am{2}".format(pa,pn,am))      
