<!-- TOC -->
  * [Template](#template)
  * [Expanding each NFR](#expanding-each-nfr)
    * [CAP Theorem](#cap-theorem)
      * [Availability](#availability)
      * [Consistency](#consistency)
      * [Latency](#latency)
      * [Scalability](#scalability)
      * [Reads >> Writes (or) Writes >> Reads](#reads--writes-or-writes--reads)
      * [Fault Tolerance](#fault-tolerance)
<!-- TOC -->

## Template

1. CAP Theorem
    1. Availability
    2. Consistency
2. Latency (<500 ms)
3. Reads >> Writes (or) Writes >> Reads
4. Scalability
5. Fault Tolerance (low priority)

## Expanding each NFR

### CAP Theorem

#### Availability

#### Consistency

1. No Double Booking (2 step process)
    1. An api endpoint to hold the ticket temporarily until the payment is done.
    2. If payment is not done, the hold should automatically be removed after sometime. Use redis TTL for this
2. An api endpoint to take in the payment and reserve.

#### Latency

1. Faster Search
    1. Search should be fast (<500ms). Applies to any system that has search feature. Use Elasticsearch with CDC (
       change data capture)
2. Caching
3. CDN
#### Scalability

#### Reads >> Writes (or) Writes >> Reads

#### Fault Tolerance

1. Handling Surges
    1. For an application like uber, use queue to take in ride requests and process them in order.
