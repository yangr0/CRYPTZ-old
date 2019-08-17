import os
if os.getuid() != 0:
	exit("\033[31m" + "Please run this as root, or use sudo!" + "\033[0m")
os.system("apt-get update")
os.system("apt-get install python3")
os.system("apt-get install python3-pip")
os.system("pip3 install pybase64")
os.system("pip3 install pyarmor")
os.system("pip3 install sqlite3")
print("\n")
print("\033[31m" + "Please run the command: python3 cryptz.py" + "\033[0m")
print("\n")