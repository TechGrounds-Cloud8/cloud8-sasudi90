# Protocols
Identifying protocols 

## Key terminology
- TCP: Transmission control Protocol: to ensure reliable transmission of packets.
- UDP: User Datagram Protocol is used for  time-sensitive transmissions such as video playback. It speeds up communications by not formally establishing a connection before data is transferred. This allows data to be transferred very quickly, but it can also cause packets to become lost in transit — and create opportunities for exploitation in the form of DDoS attacks.
- fire and forget: On local networks, applications can send Fire-and-Forget messages through UDP (User Datagram Protocol). UDP is connection-less, and does not require a sync up between sender and receiver. Therefore, it is extremely efficient. However, UDP is not reliable, and carries "at most once" semantics for message delivery
- three way handshake: two computers begin by establishing a connection via an automated process called a ‘handshake.’ Only once this handshake has been completed will one computer actually transfer data packets to the other.
- HTTPS:

## Exercise
1. Identify several other protocols and their associated OSI layer. Name at least one for each layer.
2. Figure out who determines what protocols we use and what is needed to introduce your own protocol.
3. Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.

### Sources
- [TCP](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:transporting-packets/a/transmission-control-protocol--tcp)
- [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)

### Overcome challanges
[Give a short description of your challanges you encountered, and how you solved them.]

### Results
[Describe here the result of the exercise. An image can speak more than a thousand words, include one when this wisdom applies.]
