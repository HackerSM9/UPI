import os,sys

lb = '\033[1;30m'
lg = '\033[0;32m'
o = '\033[0;31m'
g = '\033[1;32m'
r = '\033[1;31m'
y = "\033[1;33m"
b = "\033[0;34m"
e = '\033[0m'

os.system("clear")
print(f'''

{lb}₹₹\   ₹₹\ ₹₹₹₹₹₹₹\ ₹₹₹₹₹₹\{e}       {o}₹₹\  {lg}₹₹\{e}            {b}| Author:  {y}HackerSM9
{lb}₹₹ |  ₹₹ |₹₹  __₹₹\\_₹₹  _|{e}       {o}\₹₹\ {lg}\₹₹\{e}           {b}| Origin:  {y}Made in INDIA
{lb}₹₹ |  ₹₹ |₹₹ |  ₹₹ | ₹₹ |{e}         {o}\₹₹\ {lg}\₹₹\{e}          {b}| Version: {y}5.5.0
{lb}₹₹ |  ₹₹ |₹₹₹₹₹₹₹  | ₹₹ |{e}          {o}\₹₹\ {lg}\₹₹\{e}         {b}| G-DEV:   {y}HackerSM9
{lb}₹₹ |  ₹₹ |₹₹  ____/  ₹₹ |{e}          {o}₹₹  |{lg}₹₹  |{e}        {b}| Twitter: {y}HackerSM9_
{lb}₹₹ |  ₹₹ |₹₹ |       ₹₹ |{e}         {o}₹₹  /{lg}₹₹  /{e}         
{lb}\₹₹₹₹₹₹  |₹₹ |     ₹₹₹₹₹₹\{e}        {o}₹₹ /{lg}₹₹  /{e}  
{lb} \______/ \__|     \______|{e}      {o}\__/ {lg}\__/{e}   
                                             
''')
print(g+"1) Generate UPI\n2) More Tools\n3) About\n4) Upgrade\n"+e+r+"0) EXIT\n\n"+e)
url = int(input("\033[1;36m\n >> Enter your Choice: \033[0m"))
if (url == 1):
    os.system("cd .src && python3 main.py")
if (url == 2):
    os.system("xdg-open https://GitHub.com/HackerSM9")
if (url == 3):
    os.system("cd .src && python3 about.py")
if (url == 4):
    os.system("bash update")
if (url == 0):
    print("Exited Successfully :)\n")
elif (url >= 5):
    print(r+"Invalid Option Ó╭╮Ò"+e)
else:
    print("\033[1;46m\nDone !\033[0m")
    print("\n")
