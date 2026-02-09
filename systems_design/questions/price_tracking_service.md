Questions:

1. How does user get notified when a price change
    1. You can use a Cron job that looks into the database for price changes and send out notifications.
    2. Better Approach: make it event based. Use CDC (change data capture) feature in database. Any changes to db will
       be put into a stream (kafka) and will be read by a service which sends out notifications.
2. What if the prices change very frequently, are you going to send email's for every change?
    1. Ask the interviewer. It depends, some products do that, some consolidate.
3. Amazon has a limit of 1req/sec per IP address. To scrape 500Million products a day (i.e 5000 req/sec), you need 5000
   IP addresses (workers). This amount of resources allowed? If not what other options doe we have.
    1. 5000 workers is a lot and not all systems have that. If the number of products increases, so should the workers
       too, which can become very expensive.
    2. You can use the browsers extension as a worker to track the price of the product the user is viewing.
        1. Browsers allow the extension to read the current DOM. So the extension can read the price of currently
           viewing product.
4. Can we trust the Data coming from client, in the above approach? What if a user sends false information? We should
   not be sending out notifications based on false info.
    1. Since we have to rely on client for data, we add additional guard rails to make sure the data is valid.
        1. Don't rely on just one user's data, persist it to DB only if it reported by multiple users.
        2. If the price drop is significant, make you own crawler verify it.
        3. Create a new column in the Products Table called "dirty". If you have reasons to believe that a client
           request can be false, mark it as dirty, and the crawler will make a request to verify the prices.
5. The Prices table consists of a lot of granular data, how do you aggregate this information.
    1. pre-compute price aggregations by week/month/year etc.. using a scheduled cron job.
    2. Rather than running these cron jobs, we can use TimescaleDB, a time-series extension for PostgreSQL that's
       purpose-built for this type of workload. Since we're already using PostgreSQL, TimescaleDB lets us handle price
       history analytics within the same database ecosystem while getting specialized time-series performance.