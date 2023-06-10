import ipaddress

netadd=input("Enter network address: ")
submask=input("Enter subnet mask: ")

if '/' in submask:
    fullIP=(netadd+submask)
else:
    fullIP=(netadd+"/"+submask)

net=ipaddress.ip_network(fullIP,strict=False)
nadd=str(net.network_address)
nprefix=str(net.prefixlen)
nbroad=str(net.broadcast_address)
nsubnet=list(net.subnets())
nhost=list(net.hosts())

subarr=[]
for i in nsubnet:
    subarr.append(i)

fhost=str(nhost[0])
lhost=str(nhost[len(nhost)-1])

print("Network address: "+ nadd + "/" + nprefix)
print("Broadcast address: " + nbroad)
print("Possible subnets: ")
for i in nsubnet:
    print(i)
print("Host Range: " + fhost + " - " + lhost)
