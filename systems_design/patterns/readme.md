| #  | System Design Problem           | Pattern                                        |
|----|---------------------------------|------------------------------------------------|
| 1  | Design Bit.ly                   |                                                |
| 2  | Design Rate Limiter             |                                                |
| 3  | Design Web Crawler              |                                                |
| 4  | Design a Distributed Cache      |                                                |
|    |                                 |                                                |
| 5  | Design Dropbox                  | File Storage                                   |
| 6  | Design Google Docs              | File Storage                                   |
| 7  | Design YouTube                  | File Storage                                   |
|    |                                 |                                                |
| 8  | Design Local Delivery Service   | Geo Hashing                                    |
| 9  | Design Yelp                     | Geo Hashing                                    |
| 10 | Design Uber                     | Geo Hashing                                    |
| 11 | Design Tinder                   | Geo Hashing                                    |
|    |                                 |                                                |
| 12 | Design WhatsApp                 | Real time updates                              |
| 13 | Design FB Live Comments         | Real time updates                              |
| 14 | Design Online Auction           | Real time updates, Dealing with Contention     |
|    |                                 |                                                |
| 15 | Design Ticketmaster             | Dealing with Contention, Online Booking System |
|    |                                 |                                                |
| 16 | Design Instagram                | Fanout on write, File Storage                  |
| 17 | Design FB News Feed             | Fanout on write, File Storage                  |
|    |                                 |                                                |
| 18 | Design Ad Click Aggregator      |                                                |
| 19 | Design News Aggregator          |                                                |
|    |                                 |                                                |
| 20 | Design FB Post Search           |                                                |
| 21 | Design YouTube Top K            |                                                |
|    |                                 |                                                |
| 22 | Design Robinhood                |                                                |
| 23 | Design a Price Tracking Service |                                                |
|    |                                 |                                                |
| 24 | Design LeetCode                 |                                                |
| 25 | Design Strava                   |                                                |
| 26 | Design a Job Scheduler          |                                                |
| 27 | Design a Payment System         |                                                |

### File Storage

Generic Topics to talk about:

1. how do you upload/download files
2. How do you upload large files
3. How does pre-signed url's work
    1. API GW limit of 10mb, so using pre-signed urls to upload.
    2. Authentication on pre-signed url's
4. Resumable uploads/downloads
5. How does chunking work
    1. How do you track status of chunks uploaded
        1. S3 callback to update the status in DB
    2. How do you verify the integrity of chunks
        1. Fingerprinting (creating a hash of the bytes and comparing after upload)

#### NFR

1. System Specific
    1. Should be able to upload large files (50 GB) -- (Dropbox)
    2. Data Integrity is high -- (Dropbox)
        1. The uploads/downloads can be paused/resumed etc. but eventually the data integrity should be high.
2. CAP Theorem
    1. Availability >> Consistency
        1. Upload/Download : It is okay to have eventual consistency in uploads/downloads. This happens pretty often,
           the uploads are paused due to network issues and resumed later. -- (Dropbox)
        2. Sync Service: It is okay for users to see the files after few minutes of upload. -- (Dropbox)
3. Latency
    1. Downloading and uploading should be fast (optimized) -- (Dropbox)
        1. Compress and Uncompress chunks intelligently (text files etc.., jpeg/png are already compressed well)
        2. Use CDN
4. Scalability
5. Fault Tolerance
    1. Resumable uploads/downloads when the system goes offline -- (Dropbox)
6. Read vs Write

#### Other Commonalities

1. Pre signed URL's
    1. API endpoints should be designed with this in mind.