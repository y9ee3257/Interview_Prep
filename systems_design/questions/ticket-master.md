# Design Ticket Master

## FR

1. Search events
2. view event
3. Book event

## NFR

### System Specific:

1. No double booking

### General:

1. CAP Theorem
    1. High availability for search/viewing events
    2. High consistency for booking tickets
2. Latency
    1. Faster search (<500ms)
3. Reads >> Writes
4. Scalability
    1. Should handle peak loads

## Scale of the System: (should reevaluate)
### Questions:
1. DAU ~ 100M
2. Read Requests per user ~ 5
3. Write Requests per user ~ 1
4. Data captured per booking ~ 10kb

QPS --> 5*100M /day = 5*10^8/10^5 = 5000 QPS  
Peak QPS --> 5*QPS = 25000 QPS  

storage --> 10kb *100M = 1000GB = 1TB per day.  
= 3650 TB for 10 years  
= 3.6 PB  


## Entities:

1. Events
2. Performers
3. Venues
4. Tickets
5. Users

## API Endpoints:

1. Search Events
   ```
      User auth in header   
      GET /api/v1/search?text --> List<Partial<Events>>
   ```

2. View Event
   ```
      User auth in header   
      GET /api/v1/view?event_id --> EventDetails
   ```

3. Book Event (Reserve)
   ```
      User auth in header   
      POST /api/v1/reserve   
      {  
        eventId,  
        seat numbers  
      }
   ```

4. Book Event (Payment) --> Ticket Confirmation
   ```
      User auth in header  
      POST /api/v1/book  
      {  
        ticket details,  
        payment details  
      }  
   ```

## Explanation

### NFR:

## System Specific:

1. No double booking
    1. Use 2 step process to book the tickets. 1st one to reserve and the second one to book (after payment is done)
    2. Use Cache to lookup for seats that are reserved. Use TTL to remove from the lock automatically.

## General:

1. CAP Theorem
    1. High availability for search/viewing events
        1. horizontally scale the search and event details service
    2. High consistency for booking tickets
        1. similar to no double booking above
2. Latency
    1. Faster search (<500ms)
        1. Use ElasticSearch with Change Data Capture (CDC). ES is efficient in looking up data.
3. Reads >> Writes
    1. Use Cache and CDN for event picture etc.
4. Scalability
    1. Should handle peak loads
        1. Add a queue in front of the booking service, this makes sure that there is fewer collisions happen and fewer
           transactions are cancelled.
           Also, the load on the system will be reduced during major events like (taylor swift concert)

## Excalidraw
https://excalidraw.com/#json=5MjENrlq1WTnGk7aZVnRL,iF7Kbcbo0cHoCjl2b-zwdQ
https://excalidraw.com/#json=VnUdGKIJ3tRbktIS-tthJ,xB26bVt4Ws7Laux6bBoEvg