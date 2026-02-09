1. Tracking files changed on server
    1. Poll DB frequently for files that changed after the last checkpoint.
    2. Use Event Bus like Kafka to append the files changed.
       1. This can be used for restoring versions, just by reading the queue again from beginning. 
2. Tracking files changed on local
    1. Use File watcher to track file changes.
    2. Local DB to persist the information
3. Reconciliation
    1. Server and local can go out of sync sometimes. Once a week, compare all files in the DB to local.