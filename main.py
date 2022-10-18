import os,sys

lb = '\033[0;37m'
g = '\033[1;32m'
r = '\033[1;31m'
e = '\033[0m'

os.system("clear")
print('''

$$\   $$\ $$$$$$$\ $$$$$$\       $$\  $$\            | Author:  HackerSM9
$$ |  $$ |$$  __$$\\_$$  _|      \$$\ \$$\           | Origin:  Made in INDIA
$$ |  $$ |$$ |  $$ | $$ |         \$$\ \$$\          | Version: 5.5.0
$$ |  $$ |$$$$$$$  | $$ |          \$$\ \$$\         | G-DEV:   HackerSM9
$$ |  $$ |$$  ____/  $$ |          $$  |$$  |        | Twitter: HackerSM9_
$$ |  $$ |$$ |       $$ |         $$  /$$  /         |
\$$$$$$  |$$ |     $$$$$$\       $$  /$$  /  
 \______/ \__|     \______|      \__/ \__/   
                                             
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
