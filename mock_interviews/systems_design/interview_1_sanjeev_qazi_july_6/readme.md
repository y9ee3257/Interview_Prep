### Question
Design Web Crawler

### Excalidraw 

### Feedback
You don’t need to POST the base url or any URL. Your service would just write the found URLs to a queue. Some points we talked about: Have the downloader service write to cloud storage to prevent scenarios where some intermediate service crashes. Use a queue between downloader and parser. Talk about downloader going down before persisting the page to storage. Talk about GET returning an error instead of 200. retries, exponential backoff, max retries, don’t retry 400* errors, can retry 500* errors. Robots.txt BFS vs DFS pros and cons. Redis: can use SetNX for atomic update