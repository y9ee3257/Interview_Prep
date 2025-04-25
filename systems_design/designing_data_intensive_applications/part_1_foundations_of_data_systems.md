# Designing Data Intensive Applications Part-1 (Foundations of Data Systems)

## Chapter-1 Reliable, Scalable, and Maintainable Applications

3 factors that influence the design of a data system

1. Reliability
2. Scalability
3. Maintainability

### Reliability

System should be Fault tolerant/resilient

3 main kinds of faults

1. Hardware Faults
    1. Faults caused by infrastructure/hardware
    2. Common practices
        1. Redundancy of hardware, so you can restore a backup quickly.
        2. Systems that can tolerate the loss of an entire machine using software fault-tolerance techniques, rolling
           upgrade.
2. Software Errors
    1. Bugs in code can bring down applications across the board.
    2. Common practices
        1. Most software errors happen because of wrong assumptions. Try to make correct assumptions.
        2. Through testing, process isolation (should not impact other systems), measuring, monitoring and analyzing
           system behaviour.
3. Human Errors
    1. Common practices
        1. Design systems in a way that minimizes opportunites for error.
        2. decouple the places where people make the most mistakes from the places where they can cause failures.
        3. Test thoroughly at all levels
        4. Allow quick and easy recovery from human errors
        5. Setup detailed and clear monitoring

### Scalability

1. Describing load
    1. Find out what best describes load on your system, called load parameters. It can be request/sec, hit rate on a
       cache, ratio of reads to writes in a database, number of simultaneous active users in a chat room.
    2. Twitter fanout example
        1. Twitter's 2 main operations
            1. Post Tweet --> 4.6k req/sec on average, 12k req/sec peak.
            2. Home timeline --> 300k req/sec
        2. Approach 1:
            1. Post Tweet --> write to the database.
            2. Home timeline --> Read data from all the people user is following.
            3. Downsides:
                1. Since Home timeline requests outnumber the post tweet requests, system is slow due to heavy reads.
        3. Approach 2:
            1. Pre-compute the Home timeline and store in cache.
            2. Post Tweet --> write to the database, update the home timeline cache for all the followers.
            3. Home timeline --> Read from cache.
            4. Downsides:
                1. Although the home timeline reads are really quick, there is one exceptional case (celebrities)
                2. If a user has 30 millions followers, when writing a post it has to update 30 million home timeline
                   cache, which takes a lot of time.
        4. Approach 3: Hybrid of 1 & 2
            1. Use Approach 2 for all use cases except celebrities. For celebrities use Approach 1.
            2. Post Tweet --> write to the database, If not celebrity, update the home timeline cache for all the
               followers.
            3. Home timeline --> Read from cache, if user follows a celebrity, fetch from database.
2. Describing Performance
    1. Once you have described the load on your system, you can investigate what happens when the load increases.
        1. When you increase a load parameter and keep the system resources unchanged, how is the performance of the
           system affected.
        2. When you increase a load parameter, how much do you need to increase the resources if you want to keep
           performance unchanged.
    2. Latency
        1. The best way to check how users are impacted is not by getting the average response time, instead by getting
           the parameters like p99, p999 etc.
        2. If you places all request in order of their response time, the middle request corresponds to p50. Let's
           assume it took 1second for the middle request, it mean that 50% of the requests responded within 1s.
        3. Similarly, p99 refers to response time it took to respond to 99 percentile of the requests, p999 refers to
           99.9 percentile request. Optimizing for anything beyond that will incur a significant operations costs.
3. Approaches for coping with load
    1. Scaling up (vertical scaling)
    2. Scaling out (horizontal scaling)

### Maintainability

Majority of the costs of a software is not in its initial development, but in its ongoing maintenance, like fixing
bugs, keeping its system operations, investigating failures, adapting to new platforms, modifying for new use case etc.

3 principles of software development for maintainability:

1. Operability
    1. Making it easy for operations team to keep the system running smoothly.
2. Simplicity
    1. Make it easy for new engineers to understand the system, by removing as much complexity as possible from the
       system.
3. Evolvability
    1. Make it easy for engineers to make changes to the system in the future, adapting it for unanticipated use cases
       as requirements change. Also known as extensibility, modifiability or plasticity

## Chapter-2 Data Models and Query Languages

### The driving forces of NoSQL

1. Need for greater scalability
2. Restrictions on schemas
3. Specialized query operations that are not well supported in relational model.
4. Free and Open source

### Data Normalization:

Avoiding data duplication is called data normalization.  
ex: Take a persons resume, a person can have only one first/last name, but can have many jobs. Saving all the job
information in the person table will duplicate the data, since other users can also have the same job. So we move the
jobs to a separate table, and use the job id's are foreign keys in users table. This avoids data duplication.

Normalizing the data also means there will be relations (one-to-many/many-to-many). Relational database handles this
very easily, but document databases does not support this well.

However, Document databases and relational databases follow a similar approach, they both save a reference to the
foreign
table in the main table. But Relational databases are more tuned towards joins.

### Schema Flexibility

It is generally regarded the Document databases does not have schema. But that is not true, as the code that reads the
data usually assumes some kind of structure.So there is an implicit schema, but only interpreted when the data is read.

***Schema-on-read*** : No schema when writing, but assumes schema on reading the data.  
***Schema-on-write*** : Schema on write like relations databases follow, the same schema is enforced in the application
as well.

Below is an example, lets assume you want to split the users fullname to first/last name.

#### Relational databases :

1. Create two new columns (firstName, lastName)
2. Update the first/last name for existing records by split the fullName.
    ```
        ALTER TABLE users ADD COLUMN first_name varchar;
        UPDATE users set first_name = split_part(fullName, ' ',1);
    ```
3. Make changes in the application to read from new columns.

#### Document Databases:

1. update the application code to read from fullName if exists, else read from firstName/lastName
   ```
       if(user && user.name && !user.firstName){
           user.firstName=user.name.split(" ")[0];
       }
   ```

### Data locality for queries

A document is usually stored as a single continuous string, encoded as JSON, XML or a binary variant. If you application
often needs access to the entire document, there is a performance advantage to this storage locality.
But if you need access to a portion of the document, you still need to fetch the entire document, which is wasteful of
resources.

Similarly, if you want to update only a portion of the document, you still need to update the entire document.

For these reasons, it is generally recommended to keep the documents fairly small and avoid writes that increases the
size of the database.

If the data is split across multiple tables, multiple index lookups are required to retrieve it all, which may require
more disk seeks and take more time.

### Convergence of Relational and Document databases:

Relational databases like PostgreSQL, MySQL, IBM DB2 all started supporting JSON documents.

Document databases like RethinkDB supports relational like joins in its query language, MongoDB drivers automatically
resolve database references.

A hybrid of relational and document models is good route for databases to take in the future.

### When to choose Relational/Document database

#### Relational Database

1. For highly interconnected data, i.e If your application uses a lot of one-to-many/many-to-many relationships
    1. Compare to Document DB: Joins can be emulated in application code by making multiple requests to the database,
       but that also moves complexity into the application and is usually slower that a join performed by specialized
       code inside the database.

#### Document Database

1. If the data in your application has a document like structure (i.e. a tree of one-to-many relationships, where
   typically the entire tree is loaded at once)
    1. Compare to Relational DB: The relational technique of shredding/splitting a document like structure into multiple
       tables can lead to cumbersome schemas and unnecessary complicated application code.
2. Schema Flexibility 