## Upload and Download files pattern

1. API GW limit of 10MB
2. Upload/Download directly from S3 using pre-signed url's
    1. Authentication of pre-signed url's
    2. Integrity of the uploaded file
        1. Fingerprinting (creating a hash of the bytes and comparing after upload)
        2. S3 callbacks after chunk upload is complete
3. Chunking while uploading/downloading
4. Faster upload/download
    1. Intelligent Compression
    2. CDN
5. Resumable uploads
    1. Tracking status of chunks uploaded

### Authentication of pre-signed url's

1. User authenticates to Server
2. Server authenticates to S3 and get pre-signed url's
3. Properties of pre-signed url's
    1. Short lived (<15 min)
    2. Size limit
    3. Headers
        1. content-type
        2. checksum (hash of file/chunk)

### Integrity check of the uploaded file

1. Before upload
    1. The S3 pre-signed url verifies the checksum header.
2. After upload
    1. After upload, S3 callbacks the server and the checksum is verified by the server with the database.

