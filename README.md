# The muezzin - المؤذن


### publish_podcasts
1. Reading the file by its exact path in the local folder .
2. Creating metadata information.
3. Building a dedicated json.
4. Sending to Kafka.


### 2. processing
1. Single-valued unique identifier calculation
2. Sending parts of the document:
    * All metadata information is sent to the index in elasticsearch,
      to enable efficient searches and analysis. 
    * The actual contents of the file are stored in monogodb.
