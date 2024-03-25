1.distributed web infrastructure

This diagram represents a design for three server web infrastructure that hosts
the website www.foobar.com, found at this URL:
* [1-distributed_web_infrastructure](1-distributed_web_infrastructure)

Elements in [1-distributed_web_infrastructure](1-distributed_web_infrastructure):
 * 2 servers
 * 1 web server (Nginx)
 * 1 application server
 * 1 load-balancer (HAproxy)
 * 1 application files (your code base)
 * 1 database (MySQL)

================================================================================

**About the infrastructure:**

This distributed web infrastructure is an improvement on the one server web
infrastructure, because it reduces the traffic from the primary server by
distributing some of the load to a replica server. This is done with the help of
a load balancer.

**1. What distribution algorithm your load balancer is configured with and how
     it works?**
  - A HAproxy load balancer is best configured with a Round Robin distribution
  algorithm. In this algorithm requests are distributed evenly in a sequential
  manner to each server in the pool. The Round Robin algorithm has minimal
  overhead in terms of computational resources and management complexity, making
  it simple to deploy with a small number of servers. It also provides basic
  redundancy by distributing requests across multiple servers.

**2. Is your load-balancer enabling an Active-Active or Active-Passive setup?**
  - The load-baancer is enabling an Active-Active setup. Since the load-
  balancing algorithm is a Round Robin, therefore incoming requests are
  distributed evenly across all servers. This setup provides better resource
  utilization and scalability since all servers share the load. If one server
  fails, the others continue to handle requests.
  - In a Active-Passive setup, only one server handles incoming requests, while
  the others(passive servers) remain idle or handle backup tasks. If the active
  fails, one of the passive servers takes over to ensure continuity of service.

**3. How a database Primary-Replica (Master-Slave) cluster works?**
  - In a primary-replica configuration, there's a single primary node
  responsible for managing write operations such as inserts, updates, and
  deletes. This primary node then propagates these changes to one or more
  replica nodes, also known as slaves. The replica nodes focus on serving read
  operations, like select queries, and stay synchronized with the primary node
  to maintain data consistency.

**4. Difference Between Primary and Replica Node for Applications?**
  - Primary node: is responsible for handling write operations and maintaining
  the authoritative copy of the data. Applications typically interact with the
  primary node when performing write operations.
  - Replica node: Replica nodes serve read operations and provide redundancy and
  scalability for read-heavy workloads.

================================================================================

**Issues with this infrastructure:**

**1. SPOF (Single point of failure)**
  - if the primary database server is down, the whole system will not be able to
  make changes to the site, meaning there would be any write and update
  functionality. The replica server only has reading capabilities.

**2. Security issues**
  - There is no firewall and no HTTPS. Therefore, data and user is not enrypted
  or protected as it moves through the infrastructure. The lack of a firewall
  may lead to unauthorised users gaining access to the network.

**3. No monitoring**
  - The load-balancer is not monitored, meaning there is no way of knowing when
  there is an overload in the server.
  - The two servers are not monitored, therefore there would be no way of
  knowing the state of the performance, security or even the availability of
  certain components

================================================================================