#!/usr/bin/env python3
# Created By benelhaj_younes(Do0pH2ck) and i.nc0gnt0(inc0gnit0)
# CopyRight , All rights Received (GNU Rights)
# Don't Copy The Code Without Giving Me The Credits Nerds !!!
try:
    import pybase64,sqlite3,re,os,sys
    import datetime
    from time import sleep as sl
except ImportError:
        print("\033[31m" + "Please run: python3 install.py" + "\033[0m")
        exit(1)
def clear():
    os.system('clear || cls')

clear()
## Set Date ####
now = datetime.datetime.now()
hour = now.hour
min = now.minute
sec = now.second
timenow = "{}:{}:{}".format(hour,min,sec)
#######Colors###########
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
yellow="\033[1;36m"
Red="\033[1;31m"
purple="\033[35m"
Light="\033[95m"
cyan="\033[96m"
stong="\033[39m"
unknown="\033[38;5;82m"
unknown2="\033[38;5;198m"
unknown3="\033[38;5;208m"
unknown4="\033[38;5;167m"
unknown5="\033[38;5;91m"
unknown6="\033[38;5;210m"
unknown7="\033[38;5;165m"
unknown8="\033[38;5;49m"
unknown9="\033[38;5;160m"
unknown10="\033[38;5;51m"
unknown11="\033[38;5;13m"
unknown12="\033[38;5;162m"
unknown13="\033[38;5;203m"
unknown14="\033[38;5;113m"
unknown15="\033[38;5;14m"
##########################
def banner():
    print(unknown2 + "\n  https://github.com/doophack/cryptz\n")
    print(unknown15 + "   ####   #####   #   #  #####   #####  ###### ")
    print(unknown15 + "  #    #  #    #   # #   #    #    #        # ")
    print(unknown15 + "  #       #    #    #    #    #    #       # ")
    print(unknown15 + "  #       #####     #    #####     #      # ")
    print(unknown15 + "  #    #  #   #     #    #         #     # ")
    print(unknown15 + "   ####   #    #    #    #         #    ######  \033[31m" + "v3.0" + "\033[0m \n")
    print(unknown15 + "  made by: " + Red + "Do0pH2ck and inc0gnit0\n" + Reset)
    print(unknown15 + "  Instagram: " + Red +"benelhaj_younes(Do0pH2ck) i.nc0gnit0(inc0gnit0)\n" + Reset)
def main():
    for i in range(1):
        banner()
        password = input(unknown7 +"  Enter License Key: ")
        with sqlite3.connect('store.db') as db:
            connect1 = db.cursor()
        catch_pass = ("SELECT * FROM passman WHERE licensekey = ?")
        connect1.execute(catch_pass, [(password)])
        result = connect1.fetchall()
        if result:
            for i in result:
                print(unknown + "\n  Access Granted!!!")
                sl(3)
                print("  Started At {}".format(now))
                sl(0.10)
                print("  Loading Resources...[0%]")
                sl(0.10)
                print("  Loading Resources...[10%]")
                sl(0.10)
                print("  Loading Resources...[20%]")
                sl(0.10)
                print("  Loading Resources...[30%]")
                sl(0.10)
                print("  Loading Resources...[40%]")
                sl(0.10)
                print("  Loading Resources...[50%]")
                sl(0.10)
                print("  Loading Resources...[60%]")
                sl(0.10)
                print("  Loading Resources...[70%]")
                sl(0.10)
                print("  Loading Resources...[80%]")
                sl(0.10)
                print("  Loading Resources...[90%]")
                sl(0.10)
                print("  Loading Resources...[1000000000000%]")
                sl(1)
                print("  CRYPTZ is starting!!")
                print(unknown3+"""
                Welcome To CRYPTZ The Unbreakable Tool
                """)
                sl(3)
                clear()
                banner()
                strings = "1h3sgj5ks3erhg3h5dh23455wer32cfewjkf"
                def reverse_char(s):
                    return s[::-1]
                def unreversed_char(s):
                    return s[::-1]
                def add_string(s):
                    return s[:5] + strings + s[5:]
                def rem_string(text, char):
                    resul = ""
                    for c in text:
                        if c != char:
                            resul += c
                    return text.replace(char, "")
                choice = input(unknown + "  Do You Want To Encrypt Or Decrypt" + unknown3 + " [E/D,e/d]: " + Reset)
                print("\n")
                if choice in ["E",'e']:
                    data = input(unknown11 + "  Enter Your Plain Text Message: ")
                    print("\n")
                    data = data + strings
                    data = add_string(data)
                    data = reverse_char(data)
                    data = str.encode(data)
                    encode1 = pybase64._pybase64.b64encode(data)
                    encode1 = bytes.decode(encode1)
                    print(Green + encode1 + Reset)
                    print("\n")
                elif choice in ['D','d']:
                    clear()
                    banner()
                    data = input(unknown11 + "Enter Your Encrypted Message: ")
                    print("\n")
                    data = str.encode(data)
                    dec = pybase64._pybase64.b64decode(data)
                    dec = bytes.decode(dec)
                    strings = "1h3sgj5ks3erhg3h5dh23455wer32cfewjkf"
                    dec = rem_string(dec, strings)
                    dec = unreversed_char(dec)
                    dec = rem_string(dec, strings)
                    print(Green + dec + Reset)
                    print("\n")
                else:
                    print(Red + """  Unknown Option Quiting...\n  Don't forget to follow us on Instagram!!\n""" + Reset)
                    exit(1)
                break
        else:
            print("  Unauthorized Access !!\n  Warning Don't Try Random Things Or You'll Be Banned!!\n  To get a License Key you will need to contact creators for one")
            exit(1)
if __name__ == '__main__':
    main()