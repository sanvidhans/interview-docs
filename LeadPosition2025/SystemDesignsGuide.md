High System Design Guide

High Level System Designs Concepts

1. Functional Requirements
- users can signup & login
- users can bya subscription
- users can search videos and pay/pause a video


2. Non-Functional Requirements
- secure system with authentication/authorization
- low latency for videos
- scalable system


Step 1: Fundamentals
- Serverless vs Serverful
- Horizontal vs Vertical Scaling
- What are threads?
- What are pages?
- How does the internet work?


Step 2: Database
- SQL vs NoSQL DBs
- In-Memory DBs
- Data Replication & Migration
- Data Partitioning
- Sharding

Step 3: Consistency vs Availability
- Data Consistency & Its Levels
- Isolation & Its Levels
- CAP Theorem


Step 4: Cache
- What is Cache? (Redis, Memcached)
- Write Policies: write back, through & around
- Replacement Policies: LFU, LRU, Segmented LRU etc.
- Content Delivery Networks (CDNs)


Step 5: Networking
- TCP vs UDP
- What is HTTP(1,2,3) & HTTPS
- Web Sockets
- WebRTC & Video Streaming


Step 6: Load Balancers
- Load Balancing Algorithms (Stateless & Stateful)
- Concistent Hashing
- Proxy & Reverse Proxy
- Rate Limiting


Step 7: Message Queues
- Asynchronous Processing (Kafka, RabbitMQ)
- Publisher-Subscriber Model


Step 8: Monoliths vs Microservices
- Why Microservices?
- Concept of `Single Point of Failure`
- Avoiding Cascading Failures
- Containerization (Docker)
- Migrating to Microservices


Step 9: Monitoring & Logging
- Logging events & monitoring metrics
- Anomaly Detection

Step 10: Security
- Token for auth
- SSO & OAuth
- Access Control List & Rule Engines
- Encryption


Step 11: System Design Tradeoffs
- Push vs Pull architecture
- Consistency vs Availability
- SQL vs NoSQL DBs
- Memory vs Latency
- Throughput vs latency
- Accuracy vs Latency


Step 12: Practice, Practice, Practice
1. Youtube
2. Twitter
3. WhatsApp
4. Uber
5. Amazon
6. Dropbox/Google Drive
7. Netflix
8. Instagram
9. Zoom
10. Booking.com/Aribnb


Low Level System Design Guide

Step 1: Object Oriented Programming
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
- SOLID Principles


Step 2: Design Patterns
- Creational (Singleton, Factory etc)
- Structural (Proxy, Bridge etc.)
- Behavioral (Strategy, Command, Observer etc.)


Step 3: Concurrency & Thread safety
- Thread safe injection
- Locking mechanism
- Producer-consumer
- Race conditions & synchronization


Step 4: UML Diagrams

Step 5: APIs
- API Design
- Req/Res Object modeling
- Versioning & Extensibility
- Clean Code Principles: DRY, SRP etc
- Avoiding God Classes


Step 6: Common LLD Problems
1. Design a Tic
- 
