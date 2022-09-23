import subprocess
import optparse
import re

def get_input():
    opt_parse = optparse.OptionParser()
    opt_parse.add_option("-i","--interface", dest = "interface", help = "interface to change")
    opt_parse.add_option("-m", "--mac", dest = "macaddress", help = "new mac address")

    return opt_parse.parse_args()

def mac_changer(user_interface, user_mac):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_mac(user_interface):
    ifconfig = subprocess.check_output(["ifconfig", user_interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if new_mac:
        return new_mac.group(0)
    else:
        return None


(user_input, arguments) = get_input()
mac_changer(user_input.interface, user_input.macaddress)
final = control_mac(str(user_input.interface))
if final == user_input.macaddress:
    print("success")
else:
    print("Error")