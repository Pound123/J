#!/bin/bash
clear
cat l.txt | lolcat
echo
pkg install figlet
pkg install ruby
gem install lolcat
pkg install neofetch
pkg install toilet
pkg install wget -y
pkg install python -y
pkg install hydra -y
pkg install nmap -y
pkg install exiftool -y
pkg install unzip -y

###########################
unzip ngrok.zip
mv ngrok /$HOME
rm -rf ngrok.zip
cd
cd ../usr/etc
rm -rf bash.bashrc
rm -rf motd
cd
cd J
mv bash.bashrc /data/data/com.termux/files/usr/etc
mv kol /data/data/com.termux/files/usr/bin
cd ../../usr/bin
chmod +x *
cd /$HOME/J
xdg-open https://www.facebook.com/profile.php?id=100053713133557
clear
cat g.txt | lolcat
echo
###########################

