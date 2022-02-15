#!/usr/bin/python3
import os
import sys
import socket

if len(sys.argv)<2:
    print ('Usage: nettools.py www.example.com ' )
    sys.exit(1)

socket.setdefaulttimeout(0.5)
host=str(sys.argv[1])
ip=(socket.gethostbyname(host))
fqdn=(socket.getfqdn(ip))

def port_check(ip,port):

    DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result_of_check = DEVICE_SOCKET.connect_ex((ip,port))

    if result_of_check == 0:
        print('Listening on port ' + str(port))
        DEVICE_SOCKET.close()
    else:
        print('Not listening on port ' + str(port))
        DEVICE_SOCKET.close()

def rev_text(title):
    os.system('tput rev')
    print (title)
    os.system('tput sgr0')


os.system('clear')
print( 'Let\'s check some DNS stuff')
print('for ' +str(host))
rev_text('###########################')
print('IP   = ' +str(ip))
print('FQDN = ' +str(fqdn))
print('')

rev_text('[Checking ports 21,25,80,443]')
ports=(21,25,80,443)
for port in ports:
  port_check(ip,port)

print('')

rev_text('[Checking MX]')
os.system('nslookup -q=mx ' +str(fqdn))

rev_text('[Checking DNS]')
os.system('nslookup -q=ns ' +str(host))

rev_text('[Checking zonefile]')
os.system('nslookup -q=txt ' +str(host))

rev_text('###  Have a nice day!  ####')




