import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code, region_code_for_number
from phonenumbers import carrier, geocoder
import requests
from faker import Faker
import random
import string
import threading
import concurrent.futures
import os
import sys
import socket
import subprocess
import platform
import urllib
import time
import textwrap
import urllib.request
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style

fake = Faker()
x = PrettyTable()
init()

print(Back.BLACK,Style.BRIGHT,Fore.YELLOW+"""
           .__                           .___ 
  __  _  __|__|_______   ____          __| _/ 
  \ \/ \/ /|  |\_  __ \_/ __ \ ______ / __ |  
   \     / |  | |  | \/\  ___//_____// /_/ |  
    \/\_/  |__| |__|    \___  >      \____ | prv  
                            \/            \/ 
""")
print(Style.RESET_ALL)


print("""
   Filter by Provider              Filter by Location

   [1]  O2                         [23] Isle of man
   [2]  EE                         [24] Jersey
   [3]  Orange                     [25] Guernsey            
   [4]  Vodaphone
   [5]  Three
   [6]  Virgin
   [7]  Lycan
   [8]  Oxygen
   [9]  UK Broadband
   [10] TalkTalk
   [11] Layonyx
   [12] Limitless
   [13] Sky
   [14] Manx Telecom
   [15] Gamma Telecom
   [16] Airwave    
   [17] Stour Marine limited
   [18] SMSRelay
   [19] Confabulate
   [20] Sure
   [21] JT
   [22] Airtel

   [00] All

""")

tag = input("   <W-IR3D>: ")


if tag =="1":
    tag = "O2"
if tag =="2":
    tag = "EE"
if tag =="3":
    tag = "Orange"
if tag =="4":
    tag = "Vodaphone"
if tag =="5":
    tag = "Three"
if tag =="6":
    tag = "Virgin Mobile"
if tag =="7":
    tag = "Lycamobile"
if tag =="8":
    tag = "Oxygen8"
if tag == "9":
    tag = "UK Broadband"
if tag == "10":
    tag = "TalkTalk"
if tag == "11":
    tag = "Lanonyx"
if tag =="12":
    tag = "Limitless"
if tag =="13":
    tag = "Sky"
if tag =="14":
    tag = "Manx Telecom"
if tag =="15":
    tag = "Gamma Telecom"
if tag =="16":
    tag = "Airwave"
if tag =="17":
    tag = "Stour Marine"
if tag =="18":
    tag = "SMSRelay AG"
if tag =="19":
    tag = "Confabulate"
if tag =="20":
    tag = "Sure"
if tag =="21":
    tag = "JT"
if tag == "22":
    tag = "Airtel"
if tag =="23":
    tag = "Isle Of Man"
if tag =="24":
    tag = "Jersey"
if tag =="25":
    tag = "Guernsey"

if tag =="9922":
    tag ="London"
    

if tag =="00":
    tag = ""

def mainxnumber():
    print("\n"*2)

    while True:
    
        pswrd = 7
        nm = "123456789012535556438"
        nm = "".join(random.sample(nm, pswrd))

        pswrd = 3
        dd = "123456789012535556438"
        dd = "".join(random.sample(dd, pswrd))
        
        fnal = "+44"+dd+nm
        cd = phonenumbers.parse(fnal)

        dfg = "|number found in ===> ",geocoder.description_for_number(cd, "en")," |=== provider ===> ", carrier.name_for_number(cd, "en"),"."," |=== number ===>",cd 
        string = dfg
        string = str(string)

        string = string.replace(" (    )  ","not found")
        string = string.replace(""">', '', ' ""","\n")
        string = string.replace("""""","")
        string = string.replace("""', '""","")
        string = string.replace("""('number found in ===>  number ===> +""","")
        string = string.replace(")","")
        string = string.replace("(","")
        string = string.replace("""'""","")
        string = string.replace(" . ","")
        string = string.replace(">number ","")
        string = string.replace(" ======> ","")
        string = string.replace("in+44","")
        string = string.replace(" ===> ", " =======> ")
        string = string.replace("."," ===>")
        string = string.replace("number found in =======>","                        target found in =====>")
        string = string.replace("number found","")
        string = string.replace(" 1","")
        string = string.replace(" 2","")
        string = string.replace(" 3","")
        string = string.replace(" 4","")
        string = string.replace(" 5","")
        string = string.replace(" 6","")
        string = string.replace(" 7","")
        string = string.replace(" 8","")
        string = string.replace(" 9","")
        string = string.replace(" 0","")
        string = string.replace("_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None","")
        string = string.replace("in, PhoneNumbercountry_code=44,","")
        string = string.replace("  national_number=","")
        string = string.replace("extension=None, italian_leading_zero=None, number_of","")
        string = string.replace("PhoneNumbercountry_code=44,","")
        string = string.replace("national_number=","")
        string = string.replace(",","")
        string = string.replace("target found in =====>  provider ===> ===> number =======>","")
        string = string.replace("provider ===> ","service provider not found")
        string = string.replace("                           4","")
        string = string.replace("                           5","")
        string = string.replace("                           6","")
        string = string.replace("                           7","")
        string = string.replace("                           8","")
        string = string.replace("                           9","")
        string = string.replace("                           0","")
        string = string.replace("                           1","")
        string = string.replace("                           2","")
        string = string.replace("                           3","")
        string = string.replace("target found in =====>  |=== service provider not found===> |=== number =======>   ","")
        string = string.replace("|                        0","")
        string = string.replace("|                        1","")
        string = string.replace("|                        2","")
        string = string.replace("|                        3","")
        string = string.replace("|                        4","")
        string = string.replace("|                        5","")
        string = string.replace("|                        6","")
        string = string.replace("|                        7","")
        string = string.replace("|                        8","")
        string = string.replace("|                        9","")
        string = string.replace("|                          |=== provider ===>|=== number =======>   ","")
        string = string.replace(" provider ===>|","")
        string = string.replace("target found in","location")
      
        if "provider" in string:

            string = string.replace("=","")
            string = string.replace(">","")
            string = string.replace("number","Number: (+44)")
            string = string.replace("provider","Provider:")
            string = string.replace("location","Location:")
          
            if tag in string:
                             
                string = string.replace("United Kingdom",geocoder.description_for_number(cd, "en"))
            
                if "" in string:
                    if "|" in string:
                        print(string)
                    else:
                        pass
                else:
                    pass
    
            else:
                pass
        else:
            pass

def thread():
    while True:
        mainxnumber()

for i in range(100):
    r = threading.Thread(target=mainxnumber())
    r.start()



