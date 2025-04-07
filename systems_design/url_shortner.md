### What is URL Shortening
A URL shortening service is an online tool that converts long URLs into shorter, more manageable versions. This shortened URL redirects to the original, longer URL when accessed. Common services include Bitly, TinyURL, and Google's now-discontinued goo.gl.

### Why We Need URL Shortening:
1. **Simplicity:** Long URLs can be cumbersome to share, especially in contexts with character limits (e.g., Twitter).
2. **Improved Aesthetics:** Shortened URLs are cleaner and easier to share or print.
3. **Space Conservation:** Some platforms limit the number of characters per message (e.g., SMS, tweets). Shortening helps fit more content.
4. **Analytics:** Many URL shortening services provide analytics such as click tracking, location of visitors, and referral sources.
5. **Link Management:** They allow better management of links, such as changing the destination URL or customizing the shortened link (e.g., branding).
6. **Security:** Shorteners can mask sensitive URLs, though this can sometimes be exploited for malicious purposes.
7. **Convenience:** Easier to remember and type, especially in presentations or non-digital media.


### Requirements
1. Implement 2 function 
   1. encode
   2. decode
2. short url should be unique
3. User should be able to specify a custom short url
4. Capture analytics data
   1. time of the request
   2. how many request etc..


### Implementation:
1. A naive approach would be to use a counter for every entry. 
   1. Upsides:
      1. No collisions
   2. Downside:
      1. Predictable
      2. When the counter increases the url size also increases making it no longer a short url
2. Sofisticated implementation would be to use a base 64 system