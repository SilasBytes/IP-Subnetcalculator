import ipaddress

class InvalidIPError(Exception):
   pass
try:
    netadd=input("Enter network address: ")
    submask=input("Enter subnet mask: ")
    
    netarr=netadd.split('.')
    if netadd.isnumeric==False or int(netarr[0]) > 255 or int(netarr[1]) > 255 or int(netarr[2]) > 255 or int(netarr[3]) > 255:
        raise InvalidIPError

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
    vhost=pow(2,32-int(nprefix)) - 2
    fhost=str(nhost[0])
    lhost=str(nhost[len(nhost)-1])

    print("Network address: "+ nadd + "/" + nprefix)
    print("Broadcast address: " + nbroad)
    print("Possible subnets: ")
    for i in nsubnet:
        print(i)
    print("Number of Hosts:",vhost)
    print("Host Range: " + fhost + " - " + lhost)
except InvalidIPError:
    print("Invalid IP address")