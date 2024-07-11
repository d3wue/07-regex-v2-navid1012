import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here
reg1 = re.compile("^(([0-1]?[0-9]?[0-9]?|2?[0-5]?[0-5]?)\.){3}(([0-1][0-9]?[0-9]?|2[0-5]?[0-5]?)\.){1}$")

IPv4 = reg1.match("240.0.0.200")
print(IPv4)

IPv4 = reg1.match("192.256.1.1")
print(IPv4)

IPv4_2 = reg1.match("224.0.0.202")
print(IPv4_2)





# IPv6 Code , um matches zu finden 
#reg2 = re.compile("^([a-f0-9]{4}:){7}([a-f0-9]{4})$")

#ipv6Counter = 0
#for ip in ipAddresses:
 #   m = reg2.match(ip)
  #  if m != None:
   #     ipv6Counter += 1

#print(f"Valid IPv6 Addresses: {ipv6Counter}")