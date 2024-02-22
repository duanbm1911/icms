from ipaddress import IPv4Network

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