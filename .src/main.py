import os,sys

print("\n")
pa = input("[!] Enter UPI ID: ")
pn = input("[?] Enter Name: ")
am = input("[?] Enter Amount: ")

print("UPI is Ready: UPI://pay?pa={0}&pn={1}&am{2}".format(pa,pn,am))      
