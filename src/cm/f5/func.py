from ipaddress import IPv4Address
import re
    
def is_ipaddress(ip):
    try:
        IPv4Address(ip)
        return True
    except:
        return False
    
def is_domain(domain):
    regex = r"^(?!:\/\/)([a-zA-Z0-9-_]+(\.[a-zA-Z0-9-_]+)*\.[a-zA-Z]{2,63}|localhost)$"
    if re.match(regex, domain):
        return True
    else:
        return False


def check_access_rule_input(data, index):
    rule_index = index + 1
    error_message = str()
    if data != []:
      service_name = data[1]
      virtual_server = data[2]
      pool_member = data[3]
      client_profile = data[4]
      server_profile = data[5]
      
    return error_message