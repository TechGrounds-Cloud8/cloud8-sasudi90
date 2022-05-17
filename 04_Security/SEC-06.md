# [Public key infrastructure]
Study public key infrastructure; components, deployment, certificates. 

## Key terminology
- public key infrastructure: set of roles, policies, hardware, software and procedures needed to create, manage, distribute, use, store and revoke digital certificates and manage public-key encryption.
- CIA triangle:
  - Confidentality: designed to prevent sensitive information from unauthorized access attempts
  - integrity: maintaining cosistency, accuracy and trustworthiness of data over an entire lifecycle
  - availability: data should be consistently and readily accessible for authorized parties
- Certificate Authority: stores, issues and signs the digital certificates
- Registration authority: verifies the identity of entities requesting their digital to be stored at the CA.
- **self-signed certificate** is a digital certificate that’s not signed by a publicly trusted Certificate Authority (CA). Self-signed certificates are considered different from traditional CA certificates that are signed and issued by a CA because self-signed certificates are created, issued, and signed by the company or developer who is responsible for the website or software associated with the certificate.
-  x.509: standard format for public key certificates, digital documents that securely associate cryptographic key pairs with identities such as websites, individuals, or organizations.

## Exercise
1. Create a self-signed certificate on your VM.
2. Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).
3. Find the list of trusted certificate roots on your system (bonus points if you also find it in your VM).

### Sources
- [PKI](https://www.globalsign.com/nl-nl/blog/informatiebeveiliging-eenvoudig-als-pki)
- [CIA](https://www.techtarget.com/whatis/definition/Confidentiality-integrity-and-availability-CIA#:~:text=Confidentiality%2C%20integrity%20and%20availability%2C%20also,with%20the%20Central%20Intelligence%20Agency.)
- [Create self signed certificates](https://websiteforstudents.com/how-to-create-self-signed-certificates-on-ubuntu-linux/)
- [Find certificates in Ubuntu](https://ubuntu.com/server/docs/security-certificates#:~:text=The%20default%20location%20to%20install,%2Fssl%2Fcerts%2Fcacert.)

### Overcome challenges
- Looked up what PKI is and it's entities
- Looked up how to create self signed certificates

### Results
1. Self signed certificate
   - ![](../00_includes/SEC/SEC06selfSignedCert1.png)
   - ![](../00_includes/SEC/SEC06selfSignedCert2.png)
   - ![](../00_includes/SEC/SEC06selfSignedCert3.png)
2. - ![](../00_includes/SEC/SEC06INGcert.png)
   - ![](../00_includes/SEC/SEC06INGcert1.png)
   - ![](../00_includes/SEC/SEC06INGcert2.png)
3. Screenshot certificates own machine
   - ![](../00_includes/SEC/SEC06eigencerts.png)
4. Screenshot certificates VM, found it in /etc/ssl/certs
   - ![](../00_includes/SEC/SEC06VMcerts.png)