<!-- TOC -->
  * [Template](#template)
    * [Questions](#questions)
    * [QPS](#qps)
    * [Peak QPS = 5*QPS](#peak-qps--5qps)
    * [Total Storage (10 years)](#total-storage-10-years)
  * [Useful Metrics](#useful-metrics)
  * [Examples](#examples)
    * [URL Shortener](#url-shortener)
    * [Dropbox](#dropbox)
<!-- TOC -->

## Template

### Questions

1. How many DAU ~ 10M
2. How many read requests per user per day
3. How much write request per user per day
4. How much data stored per user per day

### QPS

Upload requests per second
= DAU * read requests / seconds per day  
= DAU * read requests / 10^5 QPS

### Peak QPS = 5*QPS

### Total Storage (10 years)

= Write requests * data stored per user * 365 * 10

## Useful Metrics

1. Seconds per day ~ 10^5
2. Postgres DB limit QPS
    1. 600K QPS for reads
    2. For mixed reads/writes - 70K QPS
3. Dynamo DB limit QPS
    1. 100K–1M+ per table (scales automatically)
4. Each server can serve about 64,000 requests per second (RPS)
5. Storage Metrics
   1. 1 million kb = 1 GB
   
## Examples

### URL Shortener

* Questions
    * URL's shortened per day ~ 100M
    * Redirects per day ~ 10:1(read:write) ~ 10*100M = 1B req/day

* QPS
    * Write QPS = requests per day / seconds in a day
    * = 10^9/10^5 = 10^3 = 1K QPS
    * Read QPS = 10*(write QPS) = 10K QPS

* Peak QPS
    * writes = 5* write QPS = 5K requests/second
    * reads = 5* read QPS = 50K requests/second

* Storage for 10years
    * Each url take around 1kb of storage (usually less than 1kb)
    * = storage per url * url's per day * 365 * 10
    * = 1kb * 100M * 365 * 10
    * = 365 TB

### Dropbox

* Questions
    * How many DAU ~ 10M
    * How many uploads per user per day ~ 2 files per day (average 500KB-variable per file)
    * How much space allocated per user ~ 10GB per user
    * How many signed up users ~ 50M

* QPS
    * = DAU * uploads per day / seconds per day
    * = 10M * 2 / 0.1M
    * = 200 uploads/sec

* Peak QPS
    * 5*QPS = 1K uploads/sec

* Total Storage:
    * = signed up users * allocated space per user
    * = 50M * 10GB
    * = 500 PB


