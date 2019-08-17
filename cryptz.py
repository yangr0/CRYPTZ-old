#!/usr/bin/env python3
#DO NOT TAMPER OR COPY THIS SOURCE CODE
try :#line:5
    import pybase64 ,sqlite3 ,re ,os ,sys ,codecs #line:6
    import datetime #line:7
    from time import sleep as sl #line:8
except ImportError :#line:9
        print ("\033[31m"+"Please run: python3 install.py"+"\033[0m")#line:10
        exit (1 )#line:11
def clear ():#line:12
    os .system ('clear || cls')#line:13
clear ()#line:15
now =datetime .datetime .now ()#line:17
hour =now .hour #line:18
min =now .minute #line:19
sec =now .second #line:20
timenow ="{}:{}:{}".format (hour ,min ,sec )#line:21
Green ="\033[1;33m"#line:23
Blue ="\033[1;34m"#line:24
Grey ="\033[1;30m"#line:25
Reset ="\033[0m"#line:26
yellow ="\033[1;36m"#line:27
Red ="\033[1;31m"#line:28
purple ="\033[35m"#line:29
Light ="\033[95m"#line:30
cyan ="\033[96m"#line:31
stong ="\033[39m"#line:32
unknown ="\033[38;5;82m"#line:33
unknown2 ="\033[38;5;198m"#line:34
unknown3 ="\033[38;5;208m"#line:35
unknown4 ="\033[38;5;167m"#line:36
unknown5 ="\033[38;5;91m"#line:37
unknown6 ="\033[38;5;210m"#line:38
unknown7 ="\033[38;5;165m"#line:39
unknown8 ="\033[38;5;49m"#line:40
unknown9 ="\033[38;5;160m"#line:41
unknown10 ="\033[38;5;51m"#line:42
unknown11 ="\033[38;5;13m"#line:43
unknown12 ="\033[38;5;162m"#line:44
unknown13 ="\033[38;5;203m"#line:45
unknown14 ="\033[38;5;113m"#line:46
unknown15 ="\033[38;5;14m"#line:47
def banner ():#line:49
    print (unknown2 +"\n  https://github.com/doophack/cryptz\n")#line:50
    print (unknown15 +"   ####   #####   #   #  #####   #####  ###### ")#line:51
    print (unknown15 +"  #    #  #    #   # #   #    #    #        # ")#line:52
    print (unknown15 +"  #       #    #    #    #    #    #       # ")#line:53
    print (unknown15 +"  #       #####     #    #####     #      # ")#line:54
    print (unknown15 +"  #    #  #   #     #    #         #     # ")#line:55
    print (unknown15 +"   ####   #    #    #    #         #    ######  \033[31m"+"v3.0"+"\033[0m \n")#line:56
    print (unknown15 +"  made by: "+Red +"Do0pH2ck and inc0gnit0\n"+Reset )#line:57
    print (unknown15 +"  Instagram: "+Red +"benelhaj_younes(Do0pH2ck) i.nc0gnit0(inc0gnit0)\n"+Reset )#line:58
def main ():#line:59
    for O00OO0O00O00O0000 in range (1 ):#line:60
        banner ()#line:61
        OOO0O000000OOOO0O =input (unknown7 +"  Enter License Key: ")#line:62
        with sqlite3 .connect ('store.db')as O00O000OO0O00O00O :#line:63
            O0OO0OO0OO00O000O =O00O000OO0O00O00O .cursor ()#line:64
        OOO000O0O0O0000O0 =("SELECT * FROM passman WHERE licensekey = ?")#line:65
        O0OO0OO0OO00O000O .execute (OOO000O0O0O0000O0 ,[(OOO0O000000OOOO0O )])#line:66
        OOO00OO000O00000O =O0OO0OO0OO00O000O .fetchall ()#line:67
        if OOO00OO000O00000O :#line:68
            for O00OO0O00O00O0000 in OOO00OO000O00000O :#line:69
                print (unknown +"\n  Access Granted!!!")#line:70
                sl (3 )#line:71
                print ("  Started At {}".format (now ))#line:72
                sl (0.10 )#line:73
                print ("  Loading Resources...[0%]")#line:74
                sl (0.10 )#line:75
                print ("  Loading Resources...[10%]")#line:76
                sl (0.10 )#line:77
                print ("  Loading Resources...[20%]")#line:78
                sl (0.10 )#line:79
                print ("  Loading Resources...[30%]")#line:80
                sl (0.10 )#line:81
                print ("  Loading Resources...[40%]")#line:82
                sl (0.10 )#line:83
                print ("  Loading Resources...[50%]")#line:84
                sl (0.10 )#line:85
                print ("  Loading Resources...[60%]")#line:86
                sl (0.10 )#line:87
                print ("  Loading Resources...[70%]")#line:88
                sl (0.10 )#line:89
                print ("  Loading Resources...[80%]")#line:90
                sl (0.10 )#line:91
                print ("  Loading Resources...[90%]")#line:92
                sl (0.10 )#line:93
                print ("  Loading Resources...[1000000000000%]")#line:94
                sl (1 )#line:95
                print ("  CRYPTZ is starting!!")#line:96
                print (unknown3 +"""
                Welcome To CRYPTZ The Unbreakable Tool
                """)#line:99
                sl (3 )#line:100
                clear ()#line:101
                banner ()#line:102
                OOOO0OOOO0O00OOO0 ="1h3sgj5ks3erhg3h5dh23455wer32cfewjkf"#line:103
                def OO000O0O0000OO0OO (O00OO00OOOO0OO0O0 ):#line:104
                    return O00OO00OOOO0OO0O0 [::-1 ]#line:105
                def OO0O0O000O0000OO0 (O0000O00000000O00 ):#line:106
                    return O0000O00000000O00 [::-1 ]#line:107
                def O0OOOO000OOOO00OO (O0O0000O0O0O0O0O0 ):#line:108
                    return O0O0000O0O0O0O0O0 [:5 ]+OOOO0OOOO0O00OOO0 +O0O0000O0O0O0O0O0 [5 :]#line:109
                def O0OOO00O0OO0O00OO (OOOO000O00O0OO0O0 ,O000O0O00OO0OOO00 ):#line:110
                    O0O0O00O0O00O0O00 =""#line:111
                    for O0OO00O0OOO0OOO0O in OOOO000O00O0OO0O0 :#line:112
                        if O0OO00O0OOO0OOO0O !=O000O0O00OO0OOO00 :#line:113
                            O0O0O00O0O00O0O00 +=O0OO00O0OOO0OOO0O #line:114
                    return OOOO000O00O0OO0O0 .replace (O000O0O00OO0OOO00 ,"")#line:115
                O0O0O0OOOOO0O0O00 =input (unknown +"  Do You Want To Encrypt Or Decrypt"+unknown3 +" [E/D,e/d]: "+Reset )#line:116
                print ("\n")#line:117
                if O0O0O0OOOOO0O0O00 in ["E",'e']:#line:118
                    OOOO0O0OOO0OO00OO =input (unknown11 +"  Enter Your Plain Text Message: ")#line:119
                    print ("\n")#line:120
                    OOOO0O0OOO0OO00OO =OOOO0O0OOO0OO00OO +OOOO0OOOO0O00OOO0 #line:121
                    OOOO0O0OOO0OO00OO =O0OOOO000OOOO00OO (OOOO0O0OOO0OO00OO )#line:122
                    OOOO0O0OOO0OO00OO =OO000O0O0000OO0OO (OOOO0O0OOO0OO00OO )#line:123
                    OOOO0O0OOO0OO00OO =str .encode (OOOO0O0OOO0OO00OO )#line:124
                    O0OO0OO0OOO0OOOOO =pybase64 ._pybase64 .b64encode (OOOO0O0OOO0OO00OO )#line:125
                    O0OO0OO0OOO0OOOOO =bytes .decode (O0OO0OO0OOO0OOOOO )#line:126
                    print (Green +O0OO0OO0OOO0OOOOO +Reset )#line:127
                    print ("\n")#line:128
                elif O0O0O0OOOOO0O0O00 in ['D','d']:#line:129
                    clear ()#line:130
                    banner ()#line:131
                    OOOO0O0OOO0OO00OO =input (unknown11 +"Enter Your Encrypted Message: ")#line:132
                    print ("\n")#line:133
                    OOOO0O0OOO0OO00OO =str .encode (OOOO0O0OOO0OO00OO )#line:134
                    OO0OO0O0OO0OO0000 =pybase64 ._pybase64 .b64decode (OOOO0O0OOO0OO00OO )#line:135
                    OO0OO0O0OO0OO0000 =bytes .decode (OO0OO0O0OO0OO0000 )#line:136
                    OOOO0OOOO0O00OOO0 ="1h3sgj5ks3erhg3h5dh23455wer32cfewjkf"#line:137
                    OO0OO0O0OO0OO0000 =O0OOO00O0OO0O00OO (OO0OO0O0OO0OO0000 ,OOOO0OOOO0O00OOO0 )#line:138
                    OO0OO0O0OO0OO0000 =OO0O0O000O0000OO0 (OO0OO0O0OO0OO0000 )#line:139
                    OO0OO0O0OO0OO0000 =O0OOO00O0OO0O00OO (OO0OO0O0OO0OO0000 ,OOOO0OOOO0O00OOO0 )#line:140
                    print (Green +OO0OO0O0OO0OO0000 +Reset )#line:141
                    print ("\n")#line:142
                else :#line:143
                    print (Red +"""  Unknown Option Quiting...\n  Don't forget to follow us on Instagram!!\n"""+Reset )#line:144
                    exit (1 )#line:145
                break #line:146
        else :#line:147
            print ("  Unauthorized Access !!\n  Warning Don't Try Random Things Or You'll Be Banned!!\n  To get a License Key you will need to contact creators for one")#line:148
            exit (1 )#line:149
if __name__ =='__main__':#line:150
    main ()
