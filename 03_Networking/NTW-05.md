# [IP adresses]
Different kind of IP adresses and how it is written. 

## Key terminology
- IP adresses: An IP address is a unique sequence of numbers assigned to a device that's written in a certain format. It globally identifies every device in the interconnected network, like internet house adress. 
- Public IP: Is given by your home router by your Internet Service Provider, primary IP adress
- Private IP: Each device connected to concerning router gets a private IP adress, this adress alone cannot access the internet directly. 
- IPv4:: It's a 32-bit address, decimal numbers are converted to binary, and it's made up of 4 blocks – with each block being separated by a dot. 
- IPv6:  IPv6 uses hexadecimal, alphanumeric characters - meaning it contains numbers and letters. It's a 128-bit address.
- NAT: Network Address Translation is a process in which one or more local IP address is translated into one or more Global IP address and vice versa in order to provide Internet access to the local hosts.
- Static adress: permanent IP adress and are often used by DNS servers.
- Dynamic adress: ISP gives out a different forever changing IP adress


## Exercise
1. Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi. 
2. Zijn de adressen hetzelfde of niet? Leg uit waarom.
3. Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.
4. Zijn de adressen hetzelfde of niet? Leg uit waarom.
5. Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan? 
6. Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?

### Sources
- [IP adresses](https://www.freecodecamp.org/news/ipv4-vs-ipv6-what-is-the-difference-between-ip-addressing-schemes/)
- [NAT](https://www.geeksforgeeks.org/network-address-translation-nat/)
- [Changing your IP adress](https://www.cnet.com/tech/services-and-software/how-to-change-your-ip-address-4-easy-ways/)

### Overcome challenges
- Looked up key terms
- Looked for a way to change my IP adresses or what the outcome could be

### Results
1. 2. Public IP for today is 87.214.6.89. Public IP adresses are given bij my   ISP   and is dynamic. The public IP of these devices are the same because it is connected to the same network device.
3. 4.   Sudi-PC 192.168.1.211 
        A52-van-Aurel 192.168.1.25 
        These devices are connected to the home router and got individually private address from the build-in DHCP server. Conversion of these private to public adresses are don by a build in NAT in the router.
4. Changing the IP adress of my devices can not be done manually, as it is not possible to be altered in my router settings. My cellphone only had the option to go DHCP or static, there was no option to alter or switch it to an other private IP inside the circle of connected devices. In theory: changing your IP address will temporarily disrupt whatever internet-connected services or programs you're using on your device. There's no harm done, but it's going to have the same effect as if you'd momentarily lost your Wi-Fi. The router probably automatically sets it back to the original private IP

