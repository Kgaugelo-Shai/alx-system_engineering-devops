2. Secured and monitored web infrastructure

This diagram represents a design for three server web infrastructure that hosts
the website www.foobar.com. It is secured, serves encrypted traffic and is
monitered. found at this URL:
* [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure)

Elements in [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure):
 * 3 firewalls
 * 1 SSL certificate to serve www.foobar.com over HTTPS
 * 3 monitoring clients (data collector for Sumologic or other monitoring
 services)

================================================================================

**About the infrastructure:**

This distributed web infrastructure is an improvement on the three server web
infrastructure, because it has firewalls, serves encrypted traffic and also
monitoring clients.

**1. What are firewalls for?**
  - Firewalls are like security guards for your computer or network. They decide
  who gets to come in and who has to stay out. They keep an eye on all the
  traffic going in and out, making sure there is no unauthorized users.

**2. Why is the traffic served over HTTPS?**
  - HTTPS encrypts the data so nobody can spy on it while it travels between
  your computer and the website's server.

**3. What monitoring is used for?**
  - Observing and tracking various aspects of a system, network, or application
  to ensure optimal performance, availability, and security. Monitoring tools
  watch things like how much memory your computer is using, how fast your
  internet connection is, and if any unauthorized users.

**4. How the monitoring tool is collecting data?**
  - By using special software installed on computers or devices, which sends
  data to a central monitoring system.
  - Another way is by looking at the traffic flowing through the network at
  certain spots.
  - They also read through event logs created by programs to find useful data

**5. Explain what to do if you want to monitor your web server QPS**
  - Choose a monitoring tool capable of monitoring web server performance
  metrics, including QPS
  - Configure the monitoring tool to collect data on web server performance
  metrics, including QPS
  - Once the monitoring tool is set up, monitor the QPS metrics regularly to
  track the volume of queries processed by your web server over time
  - Analyze the QPS data collected by the monitoring tool to identify trends,
  patterns, and potential issues.

================================================================================

**Issues with this infrastructure:**

**1. Why terminating SSL at the load balancer level is an issue?**
  - This leaves the traffic between the load balancer and the web servers
  unenrypted.

**2. Why having only one MySQL server capable of accepting writes is an issue?**
  - This is a potentail SPOF because should the primary MySQL server fail, the
  entire system loses the ability to write, update or manipulate data.

**3. Why having servers with all the same components (database, web server and
application server) might be a problem**
  - Risk of System-wide Failures: If one server fails, it can affect all servers
  since they're identical.
  - Difficulty Scaling: It's hard to adjust for increased demand without
  overloading certain components.
  - Uniform Vulnerability: All servers are vulnerable to the same attacks,
  making it easier for hackers.
  - Resource Imbalance: Some components may not get enough resources while
  others have too much, leading to inefficiency.
  - Limited Backup Options: If one type of server fails, there aren't diverse
  backup options available.

================================================================================