#### 1. Search should be fast <500ms -- applies to any system that has search feature
Use Elastic Search with CDC (change data capture)
#### 2. No double booking -- applies to systems that has a payment system for reserving a ticket/home etc.. 
2 step process
1. An api endpoint to hold the ticket temporarily until the payment is done.
   1. If payment is not done, the hold should automatically be removed after sometime. Use redis TTL for this
2. An api endpoint to take in the payment and reserve.
#### Aggregation service
---
