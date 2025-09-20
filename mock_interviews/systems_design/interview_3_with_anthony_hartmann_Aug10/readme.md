### Question
Design Uber

### Excalidraw 
https://excalidraw.com/#json=906iYFLE1_YrEUuUshikb,f-4fO0Ef3A1qr8Kau3QW3g

### Feedback
Ravi did pretty well in this interview. I think he was able to discuss some reasonable approaches, and did a good job of laying out and ideating on the basic ideas of the system. I thought his concept of storing and passing location data, though, could have used some work. He suggested a redis cache, which is a good choice for storing lots of small k/v pairs. However, it's not a good choice for needing more complex queries, hence his concept of getting substring-based geohashes probably would need to be reconsidered. For an example of a more optimal solution, I would consider a big data warehouse (e.g. aws redshift, bigquery) indexed by geohash. Similarly, I think for the more on-demand location (driver to customer, driver to restauraunt), we can probably using a streaming protocol or a websocket, rather than making RESTful requests. Otherwise, Ravi did quite well, and I enjoyed talking with him. Thanks for taking the time to interview, and feel free to reach out to anthonyhartmann395@gmail.com with any further questions or concerns