#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()  # Used for Read Options
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")  # Add Interface Option
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")  # Add New MAC address option
    (options, arguments) = parser.parse_args()
    # return parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options



def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])  # Down the interface
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])  # Change the MAC adress
    subprocess.call(["ifconfig", interface, "up"])  # Up the mac address

def get_current_mac():
    ifconfig_result = subprocess.check_output(['ifconfig', options.interface])  # Getting New MAC Address
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)  # Search New MAC Address
    if mac_address_search_result:
        return mac_address_search_result.group(0)  # return new MAC Address
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()  # Getting Arguments
print("[+] My Mac Changer")
old_mac = get_current_mac()  # Getting return value from get_current_mac() function
change_mac(options.interface, options.new_mac)  # Changing mac address
new_mac = get_current_mac()  # Getting return value from get_current_mac() function
if new_mac == options.new_mac:
    print("[+] Old MAC Address: " + str(old_mac))  # Printing Old MAC
    print("[+] New MAC Address: " + str(new_mac))  # Printing New MAC
    print("[+] MAC Address successfully changed.")  # Printing success msg
else:
    print("[-] MAC Address did not changed.")  # Printing Error Msg


