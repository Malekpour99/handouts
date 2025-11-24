# Interview Questions

## Table of Contents

- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Network](#network)
    - [TCP Vs. UDP](#tcp-vs-udp)
    - [3-Way Handshake](#3-way-handshake)
    - [4-Way Handshake](#4-way-handshake)
    - [TLS Handshake](#tls-handshake)
      - [Diffie-Hellman Key Exchange](#diffie-hellman-key-exchange)
    - [What happens when you type-in "www.google.com" in your browser?](#what-happens-when-you-type-in-wwwgooglecom-in-your-browser)
    - [HTTP Request Methods](#http-request-methods)
    - [How to rate-limit/throttle network requests on Linux server?](#how-to-rate-limitthrottle-network-requests-on-linux-server)
    - [You are suddenly informed that our website is down; how would you resolve this issue?](#you-are-suddenly-informed-that-our-website-is-down-how-would-you-resolve-this-issue)

## Network

### TCP Vs. UDP

**TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** are both transport-layer protocols, but they serve very different purposes depending on the application’s requirements.

1. Reliability & Delivery Guarantees:

   - TCP is connection-oriented. It ensures reliable delivery by using acknowledgments (ACKs), retransmissions, and sequencing. This means data arrives in order and without duplication. It’s great for applications where correctness is critical — e.g., web traffic (HTTP/HTTPS), file transfers, database replication.
   - UDP is connectionless. It does not guarantee delivery, ordering, or error correction beyond basic checksums. This makes it faster but unreliable. If packets are lost or arrive out of order, the application itself must handle that logic (if it cares).

2. Performance & Overhead:

   - TCP has more overhead due to connection setup (3-way handshake), state management, congestion control, and flow control. It prioritizes reliability over speed.
   - UDP is lightweight, with very little overhead. There’s no connection handshake, which makes it suitable for low-latency and high-throughput scenarios.

3. Use Cases:

   - TCP: Web browsers, APIs over HTTP(S), SSH, FTP — basically anywhere where consistency and data integrity are essential.
   - UDP: Real-time streaming, gaming, VoIP, DNS — where speed and low latency are more important than reliability, and occasional packet loss is tolerable.

4. Network Behavior:

   - TCP adapts to network conditions with congestion control (e.g., slow start, AIMD).
   - UDP just keeps sending — it doesn’t care if the network is congested. That’s why protocols like QUIC were introduced: to bring TCP-like reliability over UDP while maintaining low latency.

---

### 3-Way Handshake

The 3-way handshake is how TCP establishes a reliable, connection-oriented communication channel between two endpoints before exchanging data.

1. **SYN (synchronize)**

   - The client sends a packet with the SYN flag set and an initial sequence number (ISN_c).
   - This tells the server: “I want to start a connection, and here’s my starting sequence number.”

2. **SYN-ACK (synchronize + acknowledgment)**

   - The server responds with a packet that has both the SYN and ACK flags set.
   - It includes its own initial sequence number (ISN_s) and acknowledges the client’s ISN by setting ACK = ISN_c + 1.
   - This says: “I got your request, here’s my sequence number, and I acknowledge yours.”

3. **ACK (acknowledgment)**

   - The client sends back a final packet with the ACK flag set, acknowledging the server’s ISN (ACK = ISN_s + 1).
   - At this point, both sides have exchanged sequence numbers and acknowledgments. The connection is established.

---

### 4-Way Handshake

The 4-way handshake is the process TCP uses to gracefully terminate a connection. Unlike setup, teardown requires four steps because TCP connections are full-duplex — each side must close its half of the connection independently.

1. **FIN (finish) from client → server**

   - The client sends a FIN packet, indicating it has no more data to send.
   - The client enters the FIN_WAIT_1 state.

2. **ACK from server → client**

   - The server acknowledges the FIN with an ACK, meaning: “I know you’re done sending.”
   - The server can still send data back if it has some left.
   - The client enters the FIN_WAIT_2 state.

3. **FIN from server → client**

   - Once the server has finished sending its remaining data, it sends its own FIN.
   - This tells the client: “I’m also done sending.”
   - The server enters the LAST_ACK state.

4. **ACK from client → server**

   - The client responds with a final ACK, confirming the server’s FIN.
   - At this point:
     - The server transitions to the CLOSED state.
     - The client enters the TIME_WAIT state (usually 2×MSL — maximum segment lifetime), to ensure delayed packets are handled properly before fully closing.

---

### TLS Handshake

The TLS handshake establishes a secure channel between client and server by agreeing on encryption keys and verifying identities. The exact flow depends on TLS version (1.2 vs 1.3).

1. TLS 1.2 Handshake (traditional)

   - ClientHello

     - Client sends: **supported TLS version**, **list of cipher suites**, **random nonce**.
       - The `cipher suite` is a set of _algorithms_ that specifies details such as which _shared encryption keys_, or _session keys_, will be used for that particular session.
     - Says: “Here’s what I support.”

   - ServerHello

     - Server responds with **chosen TLS version, cipher suite, its random nonce, and its certificate (X.509 cert containing public key)**.
     - The certificate is signed by a trusted **Certificate Authority (CA)**.
     - The client validates the cert (domain name match, CA chain, expiration).

   - Key Exchange

     - If `RSA`: Client generates a random premaster secret, encrypts it with server’s public key, and sends it.
     - If `ECDHE` (more common today): Client and server perform a `Diffie-Hellman` key exchange to generate a shared secret.
     - Both sides now derive a session key from this secret + nonces.

   - Finished Messages

     - Client and server each send a “Finished” message encrypted with the new session key, proving encryption works.
     - From this point forward, all communication is encrypted.

2. TLS 1.3 Handshake (modern, what Google uses today)

- TLS 1.3 is faster and more secure:

  - Combines steps → handshake typically requires 1 round-trip (1-RTT) instead of 2.
  - Always uses forward-secret key exchange (ECDHE) — no more static RSA.
  - Encrypts more of the handshake itself for privacy.
  - Supports 0-RTT resumption: if you’ve connected before, you can start sending encrypted data immediately.

#### Diffie-Hellman Key Exchange

- Further study link: [Diffie-Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- `p` -> a prime number
- `g` -> a primitive root of `p`
- In modular arithmetic, a number `g` is a _primitive root modulo_ `n`, if every number `a` `coprime` to `n` is `congruent` to a power of `g` modulo `n`. for example 3 is a primitive root modulo of 7. [Primitive Root Modulo](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)
- In number theory, two integers `a` and `b` are `coprime`, `relatively prime` or `mutually prime` if the **only positive integer that is a divisor of both of them** is **`1`**. (`GCD - Greatest Common Divisor = 1`) [Coprime Integers](https://en.wikipedia.org/wiki/Coprime_integers)
- In abstract algebra, a `congruence relation` (or simply `congruence`) is an equivalence relation on an algebraic structure (such as a group, ring, or vector space) that is compatible with the structure in the sense that algebraic operations done with equivalent elements will yield equivalent elements. (e.g. if `a > b` then `a * n > b * n` where `n > 0`) [Congruence Relation](https://en.wikipedia.org/wiki/Congruence_relation)

![Diffie-Hellman Key Exchange](./images/Block-diagram-of-the-Diffie-Hellman-algorithm.png)

---

### What happens when you type-in "www.google.com" in your browser?

1. Browser Processing

   - The browser checks if it already has a cached mapping of google.com → IP address (in browser cache, OS cache, or DNS cache).
   - If cached, it uses it. Otherwise, it initiates a DNS lookup.

2. DNS Resolution

   - The browser/OS queries the configured DNS resolver (e.g., from ISP, or Google’s 8.8.8.8).
   - The resolver may return the IP from its cache, or it recursively queries:
   - Root DNS servers → TLD servers (.com) → Google’s authoritative DNS servers.
   - Eventually, the resolver returns the IP address of google.com (actually, a set of IPs, often load-balanced).

3. TCP Connection Establishment

   - With the IP in hand, the browser opens a TCP connection to the server (default port 80 for HTTP or 443 for HTTPS).
   - This involves the 3-way handshake (SYN → SYN-ACK → ACK).

4. TLS Handshake (if HTTPS, which Google always is)

   - The browser and server perform a TLS handshake:
   - Negotiate protocol version & cipher suites.
   - Exchange certificates (Google presents its SSL/TLS cert, which the browser validates against trusted Certificate Authorities).
   - Derive session keys for encrypted communication.
   - From now on, data is encrypted.

5. HTTP Request

   - The browser sends an HTTP GET request for / (the homepage) with headers (Host: google.com, User-Agent, etc.).
   - This is transmitted over the secure TCP+TLS connection.

6. Server Processing

   - Google’s load balancer receives the request (possibly via anycast IP).
   - The request may go through reverse proxies, caching layers (Google Frontend, CDNs), and eventually reach Google’s web servers.
   - The server generates or retrieves the response (HTML, JSON, or redirect).

7. HTTP Response

   - The server sends back an HTTP response (status code, headers, and body).
   - For Google, often it’s a redirect (302 to a localized domain like google.az) or directly the search page.

8. Browser Rendering

   - The browser parses the HTML:
   - Builds the DOM tree.
   - Fetches linked resources (CSS, JS, images). Each may trigger additional DNS lookups, TCP/TLS handshakes, and HTTP requests.
   - Executes JS, applies styles, and paints pixels on the screen.
   - This may involve parallel connections and caching strategies (HTTP/2 multiplexing, compression, etc.).

9. User Sees Page

   - Finally, the rendered page appears in the browser window.

---

### HTTP Request Methods

- **GET**

  - Retrieves a resource.
  - Should not modify server state.
  - Safe, idempotent.

- **POST**

  - Submits data to the server, often creating a new resource.
  - Not idempotent.

- **PUT**

  - Replaces an existing resource with the provided data.
  - Idempotent (sending the same request twice results in the same final state).

- **PATCH**

  - Partially updates a resource.
  - Not always idempotent (depends on implementation).

- **DELETE**

  - Removes a resource.
  - Idempotent (deleting the same resource twice still results in it being gone).

- **HEAD**

  - Same as GET, but returns only headers (no body).
  - Useful for checking metadata (e.g., resource existence, content length).

- **OPTIONS**

  - Returns supported methods for a resource.
  - Common in CORS preflight requests in browsers.

- **TRACE**

  - Echoes the received request, mainly for debugging. Rarely used (and often disabled for security).

- **CONNECT**

  - Establishes a tunnel to the server, often used for HTTPS via proxy.

---

### How to rate-limit/throttle network requests on Linux server?

1. **Kernel-level (Linux networking stack)**

Option A: **Using `iptables` with `hashlimit`**

The `hashlimit` module lets you limit requests per IP or globally.

```sh
sudo iptables -A INPUT -p tcp --dport 80 -m hashlimit \
  --hashlimit 10/sec --hashlimit-burst 20 \
  --hashlimit-mode srcip --hashlimit-name http_limit \
  -j ACCEPT

# Drop the rest
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
```

- `--hashlimit 10/sec`: max 10 requests per second.
- `--hashlimit-burst 20`: allow small bursts.
- `--hashlimit-mode srcip`: per client IP.

Option B: **Using `tc` (traffic control)**

`tc` can shape and throttle traffic at the interface level.

Example: limit to 100 requests/sec globally:

```sh
sudo tc qdisc add dev eth0 root handle 1: htb default 30
sudo tc class add dev eth0 parent 1: classid 1:1 htb rate 100rps
```

- This is more advanced, used when you want bandwidth or packet rate limits.

2. **Proxy-level**

If you’re running your app behind `Nginx` or other proxy apps like `HAProxy`, you can configure rate limiting easily:

```nginx
http {
    limit_req_zone $binary_remote_addr zone=one:10m rate=5r/s;

    server {
        listen 80;

        location / {
            limit_req zone=one burst=10 nodelay;
            proxy_pass http://127.0.0.1:8000;
        }
    }
}
```

- `rate=5r/s`: max 5 requests/sec per IP.
- `burst=10`: allow short bursts.

3. **Application-level**

- `Token bucket / leaky bucket algorithm` (common in Go/Python apps). [Token Bucket vs. Leaky Bucket Algorithm](https://www.geeksforgeeks.org/system-design/token-bucket-vs-leaky-bucket-algorithm-system-design/)
- `Middleware` (e.g., Django Rest Framework throttle, Go middleware).

This gives the most flexibility (per user, per token, etc.), but costs CPU since requests already reach your app.

---

### You are suddenly informed that our website is down; how would you resolve this issue?

My main and first goal is to find the source of this solution and reduce my area of investigation to that source. Then after resolving the issue, my main goal is to make sure this incident won't happen again; I can do so by creating new tests or taking other required preventing actions.

- First I check the traffic to make sure I can reach my website services (by using commands like `dig`, `curl` and `ping`)
- Check for the health and status of my servers (nodes), databases, engines and applications.
- Check for unusual resource or storage usage.
- Check from inside my services to make sure they can see other services and their connection is not lost.
- Check my application logs (`critical`, `error` levels)
- After finding the source of failure, I rollback its relevant changes ASAP.
- Then I make sure our services are stable.
- Now I create tests and take action to fix the service and make sure this won't happen again.

---
