import os
import nmap
import datetime

# Create an instance of the nmap.PortScanner class
nm = nmap.PortScanner()

nm.scan(hosts='192.168.1.1/24', arguments='-v -T2 -sS --open')

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string
filename = f'scan_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.txt'

# Open a new file to write the scan results to
with open(filename, 'w') as f:
  # Iterate over the list of hosts returned by the scan
  for host in nm.all_hosts():
    # Check if the host has any open ports or running services
    if 'tcp' in nm[host]:
      # Write the IP address of the host to the file
      f.write("IP Address: " + host + "\n")

      # Write the hostname of the host to the file, if available
      if 'hostname' in nm[host]:
        f.write("Hostname: " + nm[host]['hostname'] + "\n")

      # Write the MAC address of the host to the file, if available
      if 'mac' in nm[host]:
        f.write("MAC Address: " + nm[host]['mac'] + "\n")

      # Write the open ports and services/OS of the host to the file
      f.write("Open Ports:\n")
      for port in nm[host]['tcp']:
        f.write("  Port " + str(port) + ": " + nm[host]['tcp'][port]['name'] + "\n")
        f.write("  Service/OS: " + nm[host]['tcp'][port]['product'] + " " + nm[host]['tcp'][port]['version'] + "\n")
      f.write("\n")

  # Write a summary of the hosts to the file
  f.write("\n" + "-"*50 + "\n")
  f.write("Summary:\n")
  f.write("Number of hosts: " + str(len(nm.all_hosts())) + "\n")
  f.write("Hosts: " + ", ".join(nm.all_hosts()) + "\n")
