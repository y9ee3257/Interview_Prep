# Design Google Docs

## FR

Focussed only on collaborative editing features, could also expand this to other file system features like
uploading/synching content like in dropbox question)

1. create/upload new documents
2. Collaborative editing
    1. Make Edits to the document
    2. view/edit document from multiple users
3. cursor or position of the users is visible

## NFR
check properties for each FR to list down the NFR
1. Documents should be durable (create/upload new documents)
   1. Once the edit is done, it should never be lost.
2. Low Latency Edits < 200ms (Collaborative Editing)
3. Syncing content, Eventual Consistency on the documents (Collaborative Editing)
4. Handle millions of users at a time to use the system 
5. 100 concurrent max on a single document.
 