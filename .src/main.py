import os,sys

r = '\033[1;31m'
g = '\033[1;32m'
y = '\033[1;33m'
v = '\033[1;34m'
e = '\033[0m'
q = y+'['+r+'?'+y+']'+e
w = y+'['+g+'✓'+y+']'+e

print("\n")

pa = input(f"{q} Enter UPI ID: ")
pn = input(f"{q} Enter Name: ")
am = input(f"{q} Enter Amount: ")

print(f"\nUPI is Ready: {v}UPI://pay?pa={0}&pn={1}&am{2}".format(pa,pn,am)) 

open = input (f"{q} Do you Want to Open UPI link [ y/n ]: ")     
