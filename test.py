import re

x = "{'hostnames': [{'name': 'localhost', 'type': 'PTR'}], 'addresses': {'ipv4': '127.0.0.1'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'localhost-response'}, 'tcp': {80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'Apache httpd', 'version': '2.4.46', 'extrainfo': '(Debian)', 'conf': '10', 'cpe': 'cpe:/a:apache:http_server:2.4.46'}}}"




#t = "\"productId\":\"111111\""
m = re.match("'ipv4': '(\d+.\d+.\d+.\d+)'", x)
if m:
    print(m.group(1))
