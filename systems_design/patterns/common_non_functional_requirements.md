<!-- TOC -->

* [Template](#template-)
    * [System Specific](#system-specific)
    * [General](#general)
* [Expanding each NFR](#expanding-each-nfr)
    * [Faster Search](#faster-search-)
    * [No Double Booking](#no-double-booking)

<!-- TOC -->

## Template

### System Specific

1. Faster Search
2. Handle surges
3. No Double booking

### General

1. CAP Theorem
    1. Availability
    2. Consistency
2. Latency (<500 ms)
3. Reads >> Writes (or) Writes >> Reads
4. Scalability
    1. Should handle high volume of traffic
5. Fault Tolerance (low priority)

## Expanding each NFR

### Faster Search

Search should be fast (<500ms). Applies to any system that has search feature.
Use Elasticsearch with CDC (change data capture)

### No Double Booking

2 step process

1. An api endpoint to hold the ticket temporarily until the payment is done.
    1. If payment is not done, the hold should automatically be removed after sometime. Use redis TTL for this
2. An api endpoint to take in the payment and reserve.

### Handling Surges

For an application like uber, use queue to take in ride requests and process them in order.

### CAP Theorem
