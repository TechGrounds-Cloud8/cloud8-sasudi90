# [Subnetting]
Get to know how subnetting works and create a network architecture with this newfound knowledge. 

## Key terminology
- LAN: Stands for Local Area Network. It's a structure for organizing and protecting network communicayions for devices running within a single router. 
- subnet mask: defines the range of IP adresses that can be used within a network or subnet and seperates an IP address into two parts; network bits and host bits.
- CIDR: Classless Inter-Domain Routing. 

## Exercise
- Maak een netwerkarchitectuur die voldoet aan de volgende eisen:
  -  1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.
  - 1 private subnet dat internet toegang heeft via een NAT gateway. Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway.
  - 1 public subnet met een internet gateway. Dit subnet moet minimaal 5 hosts kunnen plaatsen (de 5 hosts is exclusief de internet gateway).
- Plaats de architectuur die je hebt gemaakt inclusief een korte uitleg in de Github repository die je met de learning coach hebt gedeeld.

### Sources
-   [LAN and CIDR](https://www.freecodecamp.org/news/what-is-a-lan-local-area-network-explained-in-plain-english/)
-   [Subnet mask](https://www.freecodecamp.org/news/subnet-mask-definition/)
-   [NAT](https://www.uturndata.com/2021/02/23/aws-quick-tips-internet-gateways-nat-gateways-and-nat-instances/#:~:text=A%20NAT%20Gateway%20is%20an,created%20in%20a%20public%20subnet.)
-   Fellow student
  

### Overcome challanges
- Looked up keywords
- Looked up subnet mask and subnetting

### Results
- Took the architecture from a cloud perspective. 
  - The cloud gives the acces to the internet, let's call that the internet gateway; the front door (with a public IP adress) of our little network. The NAT gateway would be the first subnet, given private IP 10.0.0.0 /30 because it only needs 1 host (there's a minium of 2). There's a range of 10.0.0.1 - 10.0.0.2
  - The private subnet connected to the NAT get's a private IP; 10.0.0.32 /27, with a range of 10.0.0.33-10.0.0.62 (30 hosts). A possibility would be to go a CIDR /26 with 62 hosts available depending on what the customer wants. 
  - The public subnet is given the IP 10.0.0.96 /29 with 6 hosts (>5 hosts was requirement), the range for this subnet are 10.0.0.97 - 10.0.0.102.
  - Then there's a LAN private subnet connected to the NAT subnet en public subnet. This subnet is given IP adress 10.0.0.64 /27 with a range of 10.0.0.65 - 10.0.0.94. It's either /27 with 30 hosts OR /28 with 14 hosts. 
![Architecture](../00_includes/NTW/NTW06_architecture.png)
