0.Simple web stack

This diagram represents a design for a one server web infrastucture that hosts a
website that is reachable via www.foobar.com, found at this URL:
* [0-simple_web_stack](0-simple_web_stack)

Elements in [0-simple_web_stack](0-simple_web_stack]:
 * 1 server
 * 1 web server (Nginx)
 * 1 application server
 * 1 application files (your code base)
 * 1 database (MySQL)
 * 1 domain name foobar.com configured with a www record that points to
   server IP 8.8.8.8

================================================================================

**About the infrastructure:**

**1. What is a server?**
  - A computer device or program that offers a service or functionality to other
  devices or programs or devices, which are known as clients in using a network.

**2. What us the role of a domain name?**
  - The domain name represents the human-readable label used to identify a
  specific location on the internet. Domain names are mapped to IP addresses
  using the Domain Name System (DNS), so that the user can access a website
  using just the website names, instead of IP addresses.

**3. What type of DNS record is www in www.foobar.com?**
  - The "www" prefix is associated with the Address record (A record) in the DNS
  record. An A record maps a domain name to the IPv4 address of the server
  hosting the websites.

**4. What is the role of the web server?**
  - A web server is responsible for serving clients, such as web browsers, with
  web content in response to HTTP requests. It services both static and dynamic
  content, processes requests and also communicates with other components like
  servers and databases.

**5. What is the role of the application server?**
  - The application server is responsible for executing application logic and
  processing dynamic content when it requested by the clients. It interacts with
  other components like databases, code base, etc.

**6. What is the role of the database?**
  - The database stores and manages structured data used by applications.
  It provides a structured way to store, retrieve and manipulate data.

**7. What is the server using to communicate with the computer of the user
     requesting the website**
  - The server communicates with the computer requesting the website using the
  Hypertext Transfer Protocol (HTTP) over the internet. The communication
  happens using the TCP/IP (Transmission Control Protocol/Internet Protocol),
  with the client (browser) sending HTTP requests to the server, and the server
  replying with HTTP responses containing the requested data.

================================================================================

**Issues with this infrastructure:**

**1. SPOF (Single point of failure)**
  - Should the database (MySQL) is down, the entire system fails

**2. Downtime when maintenance needed**
  - There is only one server, therefore when maintenance is needed, the server
  would have to be turned off. The website will there fail.

**3. Cannot scale if too much incoming traffic**
  - There amount if incoming traffic is not being monitered, should there be an
  overload of incoming traffic, the server will eventually run out of resources,
  or start performing slow.

================================================================================