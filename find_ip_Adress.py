import ipaddress

def is_valid_ip(ip_string):
    """
    Checks if a string is a valid IPv4 or IPv6 address.
    Returns True for a valid IP address, False otherwise.
    """
    try:
        ipaddress.ip_address(ip_string)
        return True
    except ValueError:
        return False

# --- Test cases ---
# Valid IPv4 addresses
print(f"192.168.1.1 is valid: {is_valid_ip('192.168.1.1')}")
print(f"0.0.0.0 is valid: {is_valid_ip('0.0.0.0')}")
print(f"255.255.255.255 is valid: {is_valid_ip('255.255.255.255')}")

# Invalid IPv4 addresses
print(f"256.0.0.0 is valid: {is_valid_ip('256.0.0.0')}")
print(f"192.168.1. is valid: {is_valid_ip('192.168.1.')}")
print(f"192.168.1 is valid: {is_valid_ip('192.168.1')}")
print(f"not an IP is valid: {is_valid_ip('not an IP')}")

# Valid IPv6 addresses
print(f"::1 is valid: {is_valid_ip('::1')}")
print(f"2001:0db8:85a3:0000:0000:8a2e:0370:7334 is valid: {is_valid_ip('2001:0db8:85a3:0000:0000:8a2e:0370:7334')}")

# Invalid IPv6 address
print(f"2001:0db8:85a3:0000:0000:8a2e:0370:7334:5 is valid: {is_valid_ip('2001:0db8:85a3:0000:0000:8a2e:0370:7334:5')}")
