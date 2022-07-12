Tool used to scan a network to discover devices, ports, and services that are running.
Awesome network security tool

----------

# Scan a single target (sends packets and analyzes servers response)
nmap thenewboston.com

# Also by IP
nmap 54.186.250.79

This displays ports detected, states, and services associated with that port

----------

States

open - active and open to connections
closed - responds to probes but most likely no services running
filtered - usually means protected by firewall
unfiltered - Nmap cant determine whether its open or closed

----------

# Scan multiple targets by seperating with space
nmap 192.168.0.9 192.168.0.17 192.168.0.23

# Scan a range of IP addresses
nmap 192.168.0.1-30

# You can also scan an entire subnet (0-255)
nmap 192.168.0.*

----------

# Make a targets.txt file
cat targets.txt
- 54.186.250.79
- 192.168.0.3

# Scan a list of targets (iL means input or import from list)
nmap -iL targets.txt

----------

# Perform an aggressive scan (tries to detect OS, versions, traceroute, etc...) basically more info
nmap -A 54.186.250.79

----------

# Trace path to host (all the routers you pass through)
nmap --traceroute thenewboston.com

This is useful when you have a slow connection and you want to figure out where the bottle neck is.

----------

OS and service detection

# -O to try to detect operating system (usually able to determine the OS from the response)
nmap -O thenewboston.com

# Determine service versions
nmap -sV thenewboston.com

----------

Port scanning options

There are 65,535 ports available and by default Nmap only scans the 1,000 most popular ones

# -F to only scan the 100 most popular ones (DNS, http, ssh, ftp, etc...)
nmap -F thenewboston.com

# -p to only scan specific port(s)
nmap -p 20-25,80,443 thenewboston.com

# You can also scan ports by name
nmap -p http,mysql thenewboston.com

# Scan all ports (takes a long time)
nmap -p- 192.068.0.1

# Only display open ports (I use almost always)
nmap --open thenewboston.com

----------

# Save scan results to a text file (-oX for XML)
nmap -F -oN Desktop/results.txt thenewboston.com
cat Desktop/results.txt

----------

# Verbose updates you more in real time
nmap -v thenewboston.com

# Display NICs and routes for your system
nmap --iflist
