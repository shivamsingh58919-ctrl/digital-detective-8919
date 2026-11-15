# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 is to explore computer networking fundamentals:
- Explain core networking classifications (LAN, MAN, WAN) and foundational concepts (DNS, router, protocol, packet switching, client-server model).
- Observe and document network connectivity tests (`ping`) and DNS lookups (`nslookup`/`dig`) using privacy-safe terminal outputs.
- Detail the end-to-end communication lifecycle that unfolds from the moment a user enters a URL into a web browser until the webpage renders on screen.

## 2. Work completed
- Compiled an eight-part network concepts reference table with clear, original explanations and real-world examples.
- Documented privacy-safe diagnostic command outputs for network connectivity and DNS resolution targeting `example.com`.
- Answered theoretical questions analyzing ICMP connectivity testing, DNS record resolution, and browser navigation mechanisms.
- Authored a comprehensive 7-step narrative tracing the client-server interaction through DNS, TCP/IP, routing, HTTP/HTTPS protocols, and DOM rendering.

---

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Concrete Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A high-speed network that interconnects computers and devices within a confined geographic area, such as a single residence, school computer laboratory, or office suite. | A home Wi-Fi network connecting a laptop, smartphone, smart TV, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A communication network spanning a broader geographic region than a LAN, typically encompassing a municipality, whole town, or sprawling university campus. | A university fiber backbone connecting academic departments and libraries across a city campus. |
| **WAN (Wide Area Network)** | A telecommunications network spanning expansive geographical boundaries, linking cities, states, countries, or the entire globe. | The global Internet; or an international financial banking network (such as SWIFT). |
| **DNS (Domain Name System)** | The distributed, hierarchical directory system that translates human-memorable domain names into computer-routable numerical IP addresses. | Translating `github.com` into its destination IP address (`140.82.112.3`). |
| **Router** | A dedicated networking device that connects multiple disparate networks together, reading packet header IP addresses and directing them along optimal routes. | A home Wi-Fi router that forwards data packets between internal household devices and the Internet Service Provider (ISP). |
| **Protocol** | A standardized set of syntactic and semantic rules governing how independent network entities format, transmit, synchronize, and acknowledge data. | **HTTP / HTTPS** for web communication, **TCP/IP** for transmission and routing, and **SSH** for secure remote shell access. |
| **Packet switching** | A transmission architecture where data messages are broken down into small units called packets, each routed independently across shared network links and reassembled at destination. | Streaming a YouTube video where media chunks travel through diverse internet router paths and buffer smoothly at the client. |
| **Client-server** | A distributed computing model where requester machines (clients) initiate requests for services or resources, and centralized host machines (servers) fulfill those requests. | A web browser (client) requesting a web document from an Apache or Nginx web server (server). |

---

### Task 7.2 — Observe network information

#### 1. Connectivity Test Observation (`ping`)
```text
$ ping -c 4 example.com
PING example.com (93.184.215.14): 56 data bytes
64 bytes from 93.184.215.14: icmp_seq=0 ttl=56 time=14.210 ms
64 bytes from 93.184.215.14: icmp_seq=1 ttl=56 time=13.845 ms
64 bytes from 93.184.215.14: icmp_seq=2 ttl=56 time=14.002 ms
64 bytes from 93.184.215.14: icmp_seq=3 ttl=56 time=13.918 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 13.845/13.994/14.210/0.138 ms
```

#### 2. DNS Lookup Observation (`nslookup`)
```text
$ nslookup example.com
Server:		[redacted-local-dns]
Address:	[redacted-dns-ip]#53

Non-authoritative answer:
Name:	example.com
Address: 93.184.215.14
Name:	example.com
Address: 2606:2800:21f:cb07:6820:80da:af6b:8b2c
```

#### Analytical Answers:
- **What a connectivity test helps you check:**
  A connectivity test (using ICMP echo requests) verifies whether a target host is active, reachable across intermediate gateways, measures network latency (round-trip transit time), and identifies packet loss or network congestion along the route.
- **What information a DNS lookup displays:**
  A DNS lookup reveals the authoritative IP addresses (IPv4 `A` records and IPv6 `AAAA` records) linked to a domain name, the DNS server answering the query, response latency, and any associated canonical names (CNAMEs).
- **The role of DNS when entering a website name in a browser:**
  Computers and internet routers cannot route network packets using human-language domain names like `example.com`. When a user types a URL, DNS translates the name into the numerical IP address required by the transport and network layer protocols (TCP/IP) to establish a socket connection.

---

### Task 7.3 — What happens when you open a website?
Tracing the end-to-end communication workflow in 7 structured steps:

1. **User Request & Client Initiation:** The user types `https://example.com` into the client (web browser) and hits Enter. The client parses the URL into protocol (`https://`), domain name (`example.com`), and path (`/`).
2. **DNS Resolution:** The client checks its internal cache and operating system DNS resolver cache. If uncached, it queries a recursive DNS server, which queries root, Top-Level Domain (TLD), and authoritative nameservers to resolve `example.com` to its IP address (`93.184.215.14`).
3. **TCP Connection & TLS Handshake:** The client initiates a Transmission Control Protocol (TCP) three-way handshake (SYN, SYN-ACK, ACK) with the server IP on port 443. For HTTPS, a TLS cryptographic handshake follows to establish session keys and mutual encryption.
4. **Packet-Switched Routing:** The connection packets are divided into standardized IP packets. The local router reads the destination IP in each packet header and forwards them hop-by-hop across intermediate ISP internet routers using packet switching.
5. **Client HTTP Request:** Over the established secure socket, the client sends an HTTP GET request protocol message specifying the requested document, accepted content types, and user-agent metadata.
6. **Server Processing & HTTP Response:** The destination web server receives the request, processes it, retrieves the resource, and transmits an HTTP response packet stream starting with status code `200 OK` followed by the HTML payload bytes.
7. **Client Rendering & Visual Presentation:** The client browser receives the data packets, reassembles them, parses the HTML into the Document Object Model (DOM), requests linked CSS stylesheets and scripts, and renders the interactive webpage on screen for the user.

---

## 3. Commands / tools used
- `ping -c 4 example.com`: Evaluated network connectivity, packet loss, and round-trip latency.
- `nslookup example.com`: Queried domain name server records for IPv4 and IPv6 addresses.
- Redaction tools to ensure zero personal IP addresses or local network SSIDs were exposed.

## 4. My understanding
Computer networking is fundamentally an interconnected hierarchy of standardized protocols working in concert. The separation of concerns between DNS (naming), IP (addressing and packet-switched routing), TCP (reliable transport), and HTTP/HTTPS (application content delivery) enables billions of heterogeneous computing devices worldwide to communicate seamlessly and securely.

## 5. Difficulties faced
Distinguishing between non-authoritative DNS answers from caching resolvers versus direct authoritative nameserver responses.

## 6. How I resolved them
Analyzed DNS query flags and verified that local resolvers return cached responses marked "Non-authoritative answer" unless querying the domain's authoritative registrar directly.

## 7. Evidence / files
- Complete network study: `mission-07-networking/README.md`
- Diagnostic logs: Sanitized `ping` and `nslookup` output tables.

## 8. Commit details
- Staged file: `mission-07-networking/README.md`
- Commit message: `Explain networking concepts and website communication`
- Verification: Confirmed via `git status` and `git log -1`.
