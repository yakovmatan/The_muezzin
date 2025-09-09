# The muezzin - المؤذن


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

### remark
The process of inserting metadata into elasticsearch and files into mongodb
is done in a separate service from the transcription of the file,
so that it is possible to send the basic information,
which is the metadata and the file itself quickly,
and give the heavy process of transcribing from the audio to another service,
which will update the information when it is ready.

To run, run ".\scripts\commands.bat in terminal".
