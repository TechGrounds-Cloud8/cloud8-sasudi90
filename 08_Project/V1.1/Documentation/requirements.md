# Requirements 

1. Webserver should not be accesible from the public internet
2. webserver should not have a public IP adress
3. webserver prefers a proxy between the webserver and public internet
4. if a visitor connects to the load balaner via HTTP they should be automatically upgraded to HTTPS
   - connection should be secured with at least TLS 1.2
   - webserver should have a regularly scheduled health check
     - if health check fails the server should be automatically recovered
5. when webserver is under ongoing stress an extra server should be automatically started. 
- total 'webservers' will never be more then 3 