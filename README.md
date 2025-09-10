# The muezzin - المؤذن


## services

### 1. Publish podcasts
1. Reading the file by its exact path in the local folder .
2. Creating metadata information.
3. Building a dedicated json.
4. Sending to Kafka with topic podcasts.


### 2. Processing
1. Single-valued unique identifier calculation
2. Sending parts of the document:
    * All metadata information is sent to the index in elasticsearch,
      to enable efficient searches and analysis. 
    * The actual contents of the file are stored in mongodb (in bytes).
    * The unique identifier of each file sent to new topic in kafka,
      with topic ids.

### 3. Extract text
1. Listening to topic ids in kafka.
2. Extracts bytes of file from mongodb for each id received.
3. Converts the bytes to an audio file.
4. Calculate a transcription for the received content.
5. Updates the content transcript in the Elasticsearch metadata repository.
6. Decrypting file encoding
7. Content classification and risk calculation
   * For the calculation,
     two encrypted files are used and they are decrypted.
     The risk_score function checks them against the text of the podcast,
     with one file representing the most dangerous words and another file representing less dangerous words.
     The function gives double weight to the word from the list that is more dangerous and returns the final score of each text.
     The danger_percentages function then calculates the risk percentage according to the score.
     It divides it by the number of words in the text and then multiplies it by 100 to get the percentage of dangerous messages in the textת
     and returns a risk level according to the percentage of appearances in the text,
     where the higher the percentage of appearances,
     the higher the risk percentage. The risk_level function segments into levels of danger.
     The calculation it makes means that a podcast with less than 10 percent risk is not considered dangerous,
     a podcast between 10-30 is considered to be at medium risk,
     and more than that already represents a high risk.

### 4. data_retrieval
1. Query builder for Elasticsearch
2. Provides 2 endpoint the first to receive all podcasts from Elastic.
   to get detailed information about all podcasts,
   the second one is to get all the podcasts classified as bds

### remark
The process of inserting metadata into elasticsearch and files into mongodb
is done in a separate service from the transcription of the file,
so that it is possible to send the basic information,
which is the metadata and the file itself quickly,
and give the heavy process of transcribing from the audio to another service,
which will update the information when it is ready.
Despite this, the classification of the text and the calculation of the risk are done in this serverת
and not in another service, both because it is an easy calculation that will not require the input of the text into elasticsearchת
and also because I want to bring the text ready with the calculations on it ready to work straight away.

## utils
In utils there are classes that are used by several services to avoid duplicating code.
All services take from there.

### 1.configurations
1. Connecting to the elastic.
2. Connecting pub to kafka.
3. Connecting sub to kafka.
4. Connecting to mongodb.

### 2.dals
1. Data access layer for mongodb
2. Data access layer for elasticsearch

### 3.logger
Writes logs for Elastic

To run, run ".\scripts\commands.bat in terminal".


