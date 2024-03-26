from ipaddress import IPv4Network
from ipaddress import IPv4Address

def is_subnet(subnet):
    try:
        IPv4Network(subnet)
        return True
    except:
        return False

def get_available_ips(subnet, used_ips, count):
    network = IPv4Network(subnet)
    unused_ips = []
    for ip in network.hosts():
        ip_str = str(ip)
        if ip_str not in used_ips and ip_str != str(network.network_address):
            unused_ips.append(ip_str)
            if len(unused_ips) == count:
                break
    return unused_ips

def check_subnet_overlap(subnet, subnets):
    net = IPv4Network(subnet)
    overlapped = []
    for s in subnets:
        other = IPv4Network(s)
        if net.overlaps(other):
            overlapped.append(other)
    return overlapped

def check_list_ipaddress(datalist):
    try:
        for ip in datalist:
            if ip != 'any':
                IPv4Address(ip)
        return True
    except:
        return False

def check_list_protocol(datalist):
    try:
        for item in datalist:
            list_item = item.split('-')
            if len(list_item) == 2:
                if list_item[0] not in ['tcp', 'udp']:
                    return False
                else:
                    int(list_item[1])
                    if int(list_item[1]) < 0 or int(list_item[1]) > 65536:
                        return False
            elif len(list_item) == 3:
                if list_item[0] not in ['tcp', 'udp']:
                    return False
                else:
                    int(list_item[1])
                    int(list_item[2])
                    if int(list_item[1]) > int(list_item[2]):
                        return False
                    elif int(list_item[1]) < 0 or int(list_item[1]) > 65536:
                        return False
                    elif int(list_item[2]) < 0 or int(list_item[2]) > 65536:
                        return False
            else:
                return False
        return True
    except:
        return False


def check_access_rule_input(data, index):
    rule_index = index + 1
    error_message = str()
    if data != []:
        policy = data[0]
        description = data[1]
        source = data[2].split('\n')
        destination = data[3].split('\n')
        protocol = data[4].split('\n')
        schedule = data[5]
        if policy == "":
            error_message = f'Rule index {rule_index}: Policy template name can not be empty'
        elif description == "":
            error_message = f'Rule index {rule_index}: Policy template description can not be empty'
        elif source == ['']:
            error_message = f'Rule index {rule_index}: Source address is invalid'
        elif 'any' in source and len(source) > 1:
            error_message = f'Rule index {rule_index}: Source address is invalid'
        elif not check_list_ipaddress(source):
            error_message = f'Rule index {rule_index}: Source address is invalid'
        elif destination == ['']:
            error_message = f'Rule index {rule_index}: Destination address is invalid'
        elif 'any' in destination and len(destination) > 1:
            error_message = f'Rule index {rule_index}: Destination address is invalid'
        elif not check_list_ipaddress(destination):
            error_message = f'Rule index {rule_index}: Destination address is invalid'
        elif not check_list_protocol(protocol):
            error_message = f'Rule index {rule_index}: Protocol is invalid'
    return error_message