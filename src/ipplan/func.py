import ipaddress

def ip_address_verify(subnet):
    try:
        ipaddress.IPv4Network(subnet)
        return True
    except:
        return False