import socket
from ip2geotools.databases.noncommercial import DbIpCity

url=input("Enter the url address:")
ip=socket.gethostbyname(url)
response=response = DbIpCity.get(ip, api_key='free')
print("City:",response.city)
print("Ip Adresses:",ip)
print("Region:",response.region)
print("Country:",response.country)

