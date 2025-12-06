## Design a payment system

https://excalidraw.com/#json=QEOV5NzuI2-2XlA_VuM4b,40BawDVDW3PbcSTW1tvb8Q

FR:
1. Clients/Merchants should be able to initiate payments.
2. System should take in payment details and process the payment.
3. System should be able to provide payment status real time.


NFR:
1. CAP Theorem
    1. Although it looks like this should be consistent, we are not the one's processing
       the payments, so no preference, should be both.
2. System specific
    1. Should be secure (payment details should not be exposed)
    2. Should be durable (all transaction history should be saved)
    3. Should guarantee transaction despite the async nature.
        1. i.e. No double charges, should not charge any transaction twice
3. Read heavy (or) write heavy
    1. not heavy on both (no need to mention this in interview, this is just for practice)
4. Latency
    1. System should process the payment as soon as possible (depends on external services like master/visa)
5. Scalability
    1. Should be scalable to 10,000 TPS

BOE calculation:
1. DAU - not applicable
2. Reads/writes per min = 10,000 TPS
3. Peak QPS      = 5*TPS = 50,000 TPS
4. Data on Disc  = 1kb for each transaction = 10^4 *1kb = 10MB /sec = 10*10^5 per day = 1 million MB per day
   = 1TB per day = 365 TB per year = 3.6 PB per year


Core Entities:
1. Payment_Intent
2. Merchants
3. Transactions

API Design:
1. POST /api/v1/payment/intent --> paymentIntentId
   merchant details in the header
   {
   merchantId
   payment amount
   product details
   }
2. POST /api/v1/payment/process --> 200
   {
   payemntIntentId
   paymentMethod
   paymentDetails
   }
3. GET /api/v1/payment/status?payemdntIntentId --> Success/InProgress/Failed




![questions_payment_system.png](../images/questions_payment_system.png)




FR:
1. Clients/Merchants should be able to initiate payments.
    1. This is called payment Intent in Banking world.You first create a record for a potential transaction and use that id later on.
2. System should take in payment details and process the payment.
    1. This is going to be a separate service as it depends on payment providers like master and visa.
3. System should be able to provide payment status real time.
    1. Going to use the same service for payment intent to get the status of the transaction.


NFR:
1. CAP Theorem
    1. Although it looks like this should be consistent, we are not the one's processing
       the payments, so no preference, should be both.
2. System specific
    1. Should be secure (payment details should not be exposed)
        1. how do you verify who the request came from?
            1. One option is to have an "api-key" that belongs to the merchant, but if that is exposed, then the entire security is at risk.
            2. On top of the above, the merchant should sign the body of the request and add it to the header. This could only be decrypted by the payment system, making sure the request belongs to the merchant.
               ex:  // Example request with signature
               {
               "method": "POST",
               "path": "/payment-intents/{paymentIntentId}/transactions",
               "body": {
               // body here
               },
               "headers": {
               "Authorization": "Bearer pk_live_51NzQRtGswQnXYZ8o", // API Key
               "X-Request-Timestamp": "2023-10-15T14:22:31Z", // Timestamp
               "X-Request-Nonce": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", // Nonce
               "X-Signature": "sha256=7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069" // Hash of body
               }
               }
        2. How do you make sure the payment details are not exposed to the merchant?
            1. Provide an iframe to be used for payments in other sites. This way the merchants could not also see the payment details.
            2. Encrypt the request before sending it to the payment system, so even if the merchant is compromised, the payment details are not exposed.

    2. Should be durable (all transaction history should be saved)
        1. The payment status gets updated frequently, so we lose track of when the payment got initiated/inProgress/success/failed etc. We could create new audit tables but it involves additional overhead and the developer
           should remember to update both tables for every transaction. Also, since the audit history is ever growing, it is not wise to save it in the same database.
        2. CDC - whenever there is a change in DB, the cdc(change data capture) sends the changed information to kafka event stream which saves it to long term storage like S3.

    3. Should guarantee transaction despite the async nature. i.e. No double charges, should not charge any transaction twice.
        1. Since the payment system is asynchronous in nature, there is a high chance that some transactions are lost.
            1. Lets say, the request to payment providers (master/visa) failed for network reasons, this does not mean the transaction is failed, we need mechanism to reconcile the transactions.
            2. We could have a cron job to trigger the reconcile service which looks up the database and reconcile all the failed transactions. But, it's better to have it event driven.
            3. So the reconcile service will read data from kafka which get new events of all status, the reconcile service can batch up the failed transactions and do a retry.

3. Read heavy (or) write heavy
    1. not heavy on both (no need to mention this in interview, this is just for practice)
4. Latency
    1. System should process the payment as soon as possible (depends on external services like master/visa)
5. Scalability
    1. Should be scalable to 10,000 TPS