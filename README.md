# Audio-FIle-Server
## - Codebase Setup
### Steps:
1. clone the code from git:

        git clone https://github.com/subhendu01/Audio-FIle-Server.git 
2. Go to the project directory:

        cd Audio-FIle-Server
3. Install all the libraries 
4. Install Mongodb
        
        pip install pymongo
5. Start the server
    
        python app.py
6. Now you can open browser and go to <b>localhost:3000/</b>, you will get "Server started" message.

## - Steps to Test API:

    The response of the methods will be :
        - Action is successful: 200 OK
        - The request is invalid: 400 bad request
        - Any error: 500 internal server error

### 1. Create API

        url = http://localhost:3000/files/api/_create 
        method = POST
        content-type = application/json

- song

    - request-body

            {
                "audioFileType": <String data>,
                "audioFileMetadata": {
                    "song_name": <String data>,
                    "duration_sec": <int data>,
                    "audio_file_id": <int data>
                }
            }
    - example

            {
                "audioFileType": "song",
                "audioFileMetadata": {
                    "song_name": "song 123",
                    "duration_sec": 200,
                    "audio_file_id": 1240
                }
            }

- podcast

    - request-body

            {
                "audioFileType": <String data>,
                "audioFileMetadata":{
                    "podcast_name": <String data>,
                    "duration_sec": <int data>,
                    "host": <String data>,
                    "participant": <List string data>,
                    "audio_file_id": <int data>
                }
            }
    - example

            {
                "audioFileType": "podcast",
                "audioFileMetadata": {
                    "podcast_name": "podcast for life",
                    "duration_sec": 400,
                    "host": "aa bb cc dd ee ff gg hh",
                    "participant": ["aaa", "bbb", "ccc", "ddd"],
                    "audio_file_id": 1241
                }
            }

- audiobook

    - request-body

            {
                "audioFileType": <String data>,
                "audioFileMetadata":
                {
                    "audiobook_title": <String data>,
                    "author_title": <String data>,
                    "narrator": <String data>,
                    "duration_sec": <int data>,
                    "audio_file_id": <int data>
                }
            }
    - example

            {
                "audioFileType": "audiobook",
                "audioFileMetadata":
                {
                    "audiobook_title": "Audiobook title",
                    "author_title": "Sekhar's life",
                    "narrator": "Subhendu Sekhar",
                    "duration_sec": 1480,
                    "audio_file_id": 1242
                }
            }

### 2. Delete API

        url = localhost:3000/files/api/_delete/<audioFileType>/<audioFileID>
        url-example = localhost:3000/files/api/_delete/song/1234 (for audio type 'song')
        method = DELETE
        content-type = application/json

- For deleting record 
    * audioFileType (song, podcast and audiobook)
    * audioFileID (Unique audio file id) 

### 3. Update API

    url = localhost:3000/files/api/_update/<audioFileType>/<audioFileID>
    method = PUT
    content-type = application/json

- song

    - request-body

            {
                "audioFileType": <String data>,
                "audioFileMetadata": {
                    "song_name": <String data>,
                    "duration_sec": <int data>,
                    "audio_file_id": <int data>
                }
            }
    - example

            {
                "audioFileType": "song",
                "audioFileMetadata": {
                    "song_name": "song 123",
                    "duration_sec": 200,
                    "audio_file_id": 1240
                }
            }

- podcast

    - request-body

            {
                "audioFileType": <String data>,
                "audioFileMetadata":{
                    "podcast_name": <String data>,
                    "duration_sec": <int data>,
                    "host": <String data>,
                    "participant": <List string data>,
                    "audio_file_id": <int data>
                }
            }

    - example

            {
                "audioFileType": "podcast",
                "audioFileMetadata": {
                    "podcast_name": "podcast for life",
                    "duration_sec": 400,
                    "host": "aa bb cc dd ee ff gg hh",
                    "participant": ["aaa", "bbb", "ccc", "ddd"],
                    "audio_file_id": 1241
                }
            }

- audiobook

    - request-body

            {
                "audioFileType": <String data>,
                "audioFileMetadata":
                {
                    "audiobook_title": <String data>,
                    "author_title": <String data>,
                    "narrator": <String data>,
                    "duration_sec": <int data>,
                    "audio_file_id": <int data>
                }
            }
    - example

            {
                "audioFileType": "audiobook",
                "audioFileMetadata":
                {
                    "audiobook_title": "Audiobook title",
                    "author_title": "Sekhar's life",
                    "narrator": "Subhendu Sekhar",
                    "duration_sec": 1480,
                    "audio_file_id": 1242
                }
            }

### 4. Get API

    * audioFileType (song, podcast and audiobook)
    * audioFileID (Unique audio file id)

    There are 2 types of url
        1. localhost:3000/files/api/_getapi/<audioFileType>/<audioFileID>
        2. localhost:3000/files/api/_getapi/<audioFileType>
    
    Example:
        1. localhost:3000/files/api/_getapi/audiobook/1237
        2. localhost:3000/files/api/_getapi/audiobook

    