#!/usr/bin/env python3
import os
from time import sleep as sl
##############################3
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
      ###############################3

print("        "+unknown+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown2+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown3+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown4+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
print("        "+unknown15+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
print("        "+unknown14+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
print("        "+unknown13+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
print("        "+unknown12+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
print("        "+unknown11+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
print("        "+unknown10+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
print("        "+unknown5+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
print("        "+unknown2+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
print("        "+unknown9+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
print("        "+unknown8+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
print("        "+unknown10+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
print("        "+unknown15+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
print("        "+unknown4+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
print("        "+unknown8+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
print("        "+unknown+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
print("        "+unknown2+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
print("        "+unknown14+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown6+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown7+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown8+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown9+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"                   "+unknown2+"["+unknown14+"Cryptz"+unknown5+"]"+unknown+"         ")
print("     "+purple+"           "+unknown13+"["+unknown10+"Created By Do0pH2ck && i.nc0gnit0"+unknown2+"]"+unknown10+"    "+Reset+"\n")

if os.getuid() != 0:
	exit("\033[31m" + "Please run this as root, or use sudo!" + "\033[0m")
os.system("apt-get update")
os.system("apt-get install python3")
os.system("apt-get install python3.7-dev")
os.system("apt-get install python3-pip")
os.system("pip3 install pybase64")
sl(1)
print(unknown3 + "Use ./cryptz | to run the tool\nHave Fun With Our Tool :D")
sl(3)
os.system("clear")
os.system("./cryptz")
