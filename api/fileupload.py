import datetime, os, base64
from flask import Flask, jsonify, request, Blueprint
from dbstore import dbconf
import json
from bson import json_util


# process kill
# lsof -i tcp:3000 

file_upload = Blueprint('uploadAPI', __name__)

app = Flask(__name__)

def song_upload(val):
    try:
        # content = request.get_json()
        curs = dbconf.file_store.find().sort( [("_id", -1)] ).limit(1)
        if curs.count() > 0:
            for rec in curs:
                id_val = rec["audioFileMetadata"]["id"]
                id = id_val + 1
        else:
            id = 1
        audio_file_id = int(val["audio_file_id"])
        cursor_file_id = dbconf.file_store.find({'audioFileMetadata.audio_file_id': audio_file_id})
        if cursor_file_id.count() == 0:
            song_name = str(val['song_name'])
            duration_sec = int(val['duration_sec'])
            upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if len(song_name) != 0 and len(song_name) <= 100:
                if duration_sec >= 0:
                    msg = "Successful"
                    response = {
                        "status": 200,
                        "msg": msg,
                        "id": id,
                        "song_name": song_name,
                        "duration_sec": duration_sec,
                        "upload_time": upload_time,
                        "audio_file_id": audio_file_id
                    }
                else:
                    msg = "Duration should be positive integer number"
                    response = {
                        "status": 400,
                        "msg": msg,
                        "upload_time": upload_time
                    }
            else:
                msg = "Song name should be between 0 to 100 characters"
                response = {
                        "status": 400,
                        "msg": msg,
                        "upload_time": upload_time
                    }
        else:
            msg = "Duplicate audio id found."
            response = {
                    "status": 400,
                    "msg": msg
                }
        return response
    except Exception as e:
        print(str(e))
        response = {
                    "status": 500,
                    "msg": "Something went wrong."
                }
        return response

def podcast_upload(val):
    try:
        curs = dbconf.file_store.find().sort( [("_id", -1)] ).limit(1)
        if curs.count() > 0:
            for rec in curs:
                id_val = rec["audioFileMetadata"]["id"]
                id = id_val + 1
        else:
            id = 1
        audio_file_id = int(val["audio_file_id"])
        cursor_file_id = dbconf.file_store.find({'audioFileMetadata.audio_file_id': audio_file_id})
        if cursor_file_id.count() == 0:
            podcast_name = str(val['podcast_name'])
            duration_sec = int(val['duration_sec'])
            upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            host = str(val['host'])
            participant = val['participant']

            # print(id, podcast_name, duration_sec, upload_time, host, participant)
            if len(podcast_name) <= 100:
                if duration_sec >= 0:
                    exceed_leng = [ x for x in participant if len(x) >= 100]
                    if len(participant) <= 10 and len(exceed_leng) == 0:
                        if len(host) <= 100:
                            msg = "sucessful"
                            response = {
                                "status": 200,
                                "msg": msg, 
                                "id": id,
                                "podcast_name": podcast_name,
                                "duration_sec": duration_sec,
                                "upload_time": upload_time,
                                "host": host,
                                "participant": participant,
                                "audio_file_id": audio_file_id
                            }
                        else:
                            msg = "Host cannot be larger than 100 characters."
                            response = {
                                    "status": 400,
                                    "msg": msg,
                                    "upload_time": upload_time
                                }
                    else:
                        msg = "Each string cannot be larger than 100 characters, maximum of 10 participants possible"
                        response = {
                            "status": 400,
                            "msg": msg,
                            "upload_time": upload_time
                        }
                else:
                    msg = "Duration should be positive integer number"
                    response = {
                        "status": 400,
                        "msg": msg,
                        "upload_time": upload_time
                    }
            else:
                msg = "Name of the podcast cannot be larger than 100 characters."
                response = {
                        "status": 400,
                        "msg": msg,
                        "upload_time": upload_time
                    }
        else:
            msg = "Duplicate audio id found."
            response = {
                    "status": 400,
                    "msg": msg
                }
        return response
    except Exception as e:
        print(str(e))
        response = {
                    "status": 500,
                    "msg": "Something went wrong."
                }
        return response

def audiobook_upload(val):
    try:
        # content = request.get_json()
        curs = dbconf.file_store.find().sort( [("_id", -1)]).limit(1)
        if curs.count() > 0:
            for rec in curs:
                id_val = rec["audioFileMetadata"]["id"]
                id = id_val + 1
        else:
            id = 1
        audio_file_id = int(val["audio_file_id"])
        cursor_file_id = dbconf.file_store.find({'audioFileMetadata.audio_file_id': audio_file_id})
        if cursor_file_id.count() == 0:
            audiobook_title = str(val['audiobook_title'])
            author_title = str(val['author_title'])
            narrator = str(val['narrator'])
            duration_sec = int(val['duration_sec'])
            
            upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if len(audiobook_title) <= 100 and len(audiobook_title) != 0:
                if len(author_title) <= 100 and len(author_title) != 0:
                    if len(narrator) <=100 and len(narrator) != 0:
                        if duration_sec >= 0:
                            msg = "sucessful"
                            response = {
                                "status": 200,
                                "msg": msg,
                                "id": id,
                                "audiobook_title": audiobook_title,
                                "author_title": author_title,
                                "narrator": narrator,
                                "duration_sec": duration_sec,
                                "upload_time": upload_time,
                                "audio_file_id": audio_file_id
                            }
                        else:
                            msg = "Duration should be positive integer number"
                            response = {
                                "status": 400,
                                "msg": msg,
                                "upload_time": upload_time
                            }
                    else:
                        msg = "Narrator should be between 0 to 100 characters."
                        response = {
                                    "status": 400,
                                    "msg": msg,
                                    "upload_time": upload_time
                                }
                else:
                    msg = "Author title should be between 0 to 100 characters."
                    response = {
                                "status": 400,
                                "msg": msg,
                                "upload_time": upload_time
                            }
            else:
                msg = "Audiobook should be between 0 to 100 characters."
                response = {
                            "status": 400,
                            "msg": msg,
                            "upload_time": upload_time
                        }
        else:
            msg = "Duplicate audio id found."
            response = {
                    "status": 400,
                    "msg": msg
                }
        return response

    except Exception as e:
        print(str(e))
        msg = "Something went wrong."
        response = {
                    "status": 500,
                    "msg": msg
                }
        return response


@file_upload.route('api/_create', methods= ['POST'])
def create():
    try:
        if request.method == "POST":
            #getting all the parameters
            content = request.get_json()
            # print(content)
            audioFileType = content['audioFileType']
            #for song type
            if audioFileType.lower() == 'song':
                audioFileMetadata = "song"
                #calling the song-upload method for song type
                func_call = song_upload(content['audioFileMetadata'])
                if func_call["status"] == 200:
                    audioFileMetadata = {
                        "duration_sec": func_call["duration_sec"],
                        "id": func_call["id"],
                        "song_name": func_call['song_name'],
                        "upload_time": func_call['upload_time'],
                        "audio_file_id": func_call['audio_file_id']
                    }
                    rec = {
                        "audioFileType": audioFileType.lower(),
                        "audioFileMetadata": audioFileMetadata
                    }
                    # insert the data into collection
                    data = json.loads(json_util.dumps(rec))

                    dbconf.file_store.insert(rec)
                    
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"],
                        "record": data
                    }
                # print(response)
                elif func_call["status"] == 400:
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"]
                    }
                elif func_call["status"] == 500:
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"]
                    }

            #for podcast type
            elif audioFileType.lower() == 'podcast':
                audioFileMetadata = "podcast"
                func_call = podcast_upload(content['audioFileMetadata'])
                if func_call["status"] == 200:
                    audioFileMetadata = {
                        "podcast_name": func_call["podcast_name"],
                        "id": func_call["id"],
                        "duration_sec": func_call["duration_sec"],
                        "host": func_call['host'],
                        "upload_time": func_call['upload_time'],
                        "participant": func_call["participant"],
                        "audio_file_id": func_call['audio_file_id']
                    }
                    rec = {
                        "audioFileType": audioFileType.lower(),
                        "audioFileMetadata": audioFileMetadata
                    }
                    data = json.loads(json_util.dumps(rec))
                    dbconf.file_store.insert(rec)
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"],
                        "record": data
                    }
                    # print(response)
                elif func_call["status"] == 400:
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"]
                    }
                elif func_call["status"] == 500:
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"]
                    }

            #for audiobook type
            elif audioFileType.lower() == 'audiobook':
                audioFileMetadata = "audiobook"
                func_call = audiobook_upload(content['audioFileMetadata'])
                if func_call["status"] == 200:
                    audioFileMetadata = {
                        "audiobook_title": func_call["audiobook_title"],
                        "id": func_call["id"],
                        "duration_sec": func_call["duration_sec"],
                        "author_title": func_call['author_title'],
                        "upload_time": func_call['upload_time'],
                        "narrator": func_call["narrator"],
                        "audio_file_id": func_call['audio_file_id']
                    }
                    rec = {
                        "audioFileType": audioFileType.lower(),
                        "audioFileMetadata": audioFileMetadata
                    }
                    data = json.loads(json_util.dumps(rec))
                    dbconf.file_store.insert(rec)
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"],
                        "record": data
                    }
                    # print(response)
                elif func_call["status"] == 400:
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"]
                    }
                elif func_call["status"] == 500:
                    response = {
                        "status": func_call["status"],
                        "msg": func_call["msg"]
                    }
                # print(response)
            else:
                response = {
                    "status": 400,
                    "msg": "Bad request."
                }
        else:
            response = {
                "status": 400,
                "msg": "Bad request."
            }
        return jsonify(response)

    except Exception as e:
        print(str(e))
        response = {
                "status": 500,
                "msg": "Something went wrong."
            }
        return jsonify(response)

@file_upload.route('api/_delete/<string:audioFileType>/<int:audioFileID>', methods= ['DELETE'])
def delete_(audioFileType, audioFileID):
    try:
        if request.method == "DELETE":
            cursor = dbconf.file_store.find({"audioFileType": audioFileType.lower(), 'audioFileMetadata.audio_file_id': audioFileID})
            if cursor.count() != 0:
                dbconf.file_store.remove({"audioFileType": audioFileType.lower(), 'audioFileMetadata.audio_file_id': audioFileID})
                response = {
                        "status": 200,
                        "msg": "Sucessfull.",
                        "audioFileType": audioFileType,
                        "audioFileID": audioFileID
                    }
            else:
                response = {
                        "status": 400,
                        "msg": "audio file ID is not found.",
                        "audioFileType": audioFileType,
                        "audioFileID": audioFileID
                    }
        else:
            response = {
                "status": 400,
                "msg": "Bad request."
            }
        return jsonify(response)
    except Exception as e:
        print(str(e))
        response = {
                "status": 500,
                "msg": "Something went wrong."
            }
        return jsonify(response)

@file_upload.route('api/_update/<string:audioFileType>/<int:audioFileID>', methods= ['PUT'])
def update(audioFileType, audioFileID):
    try:
        if request.method == "PUT":
            content = request.json
            cursor = dbconf.file_store.find({"audioFileType": audioFileType.lower(), 'audioFileMetadata.audio_file_id': audioFileID})
            if cursor.count() != 0:
                #song type
                if audioFileType.lower() == 'song':
                    song_name = content["audioFileMetadata"]["song_name"]
                    duration_sec = content["audioFileMetadata"]["duration_sec"]
                    if len(song_name) != 0 and len(song_name) <= 100:
                        if duration_sec >= 0:
                            myquery = {"audioFileType": audioFileType.lower(), 'audioFileMetadata.audio_file_id': audioFileID}
                            newvalues = { "$set": { 
                                "audioFileMetadata.duration_sec": duration_sec,
                                "audioFileMetadata.song_name": song_name,
                                "audioFileMetadata.upload_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            }}
                            dbconf.file_store.update_one(myquery, newvalues)
                            response = {
                                "status": 200,
                                "msg": "Sucessfull.",
                                "audioFileType": audioFileType,
                                "audioFileID": audioFileID
                            }
                        #for duration
                        else:
                            response = {
                                "status": 400,
                                "msg": "Duration should be positive integer number",
                                "audioFileType": audioFileType,
                                "audioFileID": audioFileID
                            }
                    #for song name
                    else:
                        response = {
                                "status": 400,
                                "msg": "Song name should be between 0 to 100 characters",
                                "audioFileType": audioFileType,
                                "audioFileID": audioFileID
                            }
                
                #podcast type
                elif audioFileType.lower() == 'podcast':
                    podcast_name = content["audioFileMetadata"]["podcast_name"]
                    duration_sec = content["audioFileMetadata"]["duration_sec"]
                    host = content["audioFileMetadata"]["host"]
                    participant = content["audioFileMetadata"]["participant"]
                    if len(podcast_name) != 0 and len(podcast_name) <= 100:
                        if duration_sec >= 0:
                            exceed_leng = [ x for x in participant if len(x) >= 100]
                            if len(participant) <= 10 and len(exceed_leng) == 0:
                                if len(host) != 0 and len(host) <= 100:
                                    myquery = {"audioFileType": audioFileType.lower(), 'audioFileMetadata.audio_file_id': audioFileID}
                                    newvalues = { "$set": { 
                                        "audioFileMetadata.podcast_name": podcast_name,
                                        "audioFileMetadata.duration_sec": duration_sec,
                                        "audioFileMetadata.host": host,
                                        "audioFileMetadata.participant": participant,
                                        "audioFileMetadata.upload_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    }}
                                    dbconf.file_store.update_one(myquery, newvalues)
                                    response = {
                                        "status": 200,
                                        "msg": "Sucessfull.",
                                        "audioFileType": audioFileType,
                                        "audioFileID": audioFileID
                                    }
                                #for host
                                else:
                                    response = {
                                        "status": 400,
                                        "msg": "Host should be between 0 to 100 characters",
                                        "audioFileType": audioFileType,
                                        "audioFileID": audioFileID
                                    }
                            #participant
                            else:
                                response = {
                                        "status": 400,
                                        "msg": "Each string cannot be larger than 100 characters, maximum of 10 participants possible",
                                        "audioFileType": audioFileType,
                                        "audioFileID": audioFileID
                                }
                        #duration
                        else:
                            response = {
                                        "status": 400,
                                        "msg": "Duration should be positive integer number",
                                        "audioFileType": audioFileType,
                                        "audioFileID": audioFileID
                                }
                    #podcast_name
                    else:
                        response = {
                                        "status": 400,
                                        "msg": "Name of the podcast should be between 0 to 100 characters",
                                        "audioFileType": audioFileType,
                                        "audioFileID": audioFileID
                                }
                
                #audiobook type
                elif audioFileType.lower() == 'audiobook':
                    audiobook_title = content["audioFileMetadata"]["audiobook_title"]
                    duration_sec = content["audioFileMetadata"]["duration_sec"]
                    author_title = content["audioFileMetadata"]["author_title"]
                    narrator = content["audioFileMetadata"]["narrator"]

                    if len(audiobook_title) != 0 and len(audiobook_title) <= 100:
                        if len(author_title) != 0 and len(author_title) <= 100:
                            if len(narrator) != 0 and len(narrator) <=100:
                                if duration_sec >= 0:
                                    myquery = {"audioFileType": audioFileType.lower(), 'audioFileMetadata.audio_file_id': audioFileID}
                                    newvalues = { "$set": { 
                                                "audioFileMetadata.audiobook_title": audiobook_title,
                                                "audioFileMetadata.duration_sec": duration_sec,
                                                "audioFileMetadata.author_title": author_title,
                                                "audioFileMetadata.narrator": narrator,
                                                "audioFileMetadata.upload_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                            }}
                                    dbconf.file_store.update_one(myquery, newvalues)
                                    response = {
                                        "status": 200,
                                        "msg": "Sucessfull.",
                                        "audioFileType": audioFileType,
                                        "audioFileID": audioFileID
                                    }
                                else:
                                    response = {
                                        "status": 400,
                                        "msg": "Duration should be positive integer number",
                                        "audioFileType": audioFileType,
                                        "audioFileID": audioFileID
                                    }
                            else:
                                response = {
                                    "status": 400,
                                    "msg": "Narrator should be between 0 to 100 characters.",
                                    "audioFileType": audioFileType,
                                    "audioFileID": audioFileID
                                }
                        else:
                            response = {
                                "status": 400,
                                "msg": "Author title should be between 0 to 100 characters.",
                                "audioFileType": audioFileType,
                                "audioFileID": audioFileID
                            }
                    else:
                        response = {
                            "status": 400,
                            "msg": "Audiobook should be between 0 to 100 characters.",
                            "audioFileType": audioFileType,
                            "audioFileID": audioFileID
                        }          
            else:
                response = {
                        "status": 400,
                        "msg": "audio file ID is not found.",
                        "audioFileType": audioFileType,
                        "audioFileID": audioFileID
                    }
        else:
            response = {
                "status": 400,
                "msg": "Bad request."
            }
        return jsonify(response)
    except Exception as e:
        print(str(e))
        response = {
                "status": 500,
                "msg": "Something went wrong."
            }
        return jsonify(response)

@file_upload.route("api/_getapi/<audioFileType>", methods=["GET"], defaults={"audioFileID": None})
@file_upload.route('api/_getapi/<string:audioFileType>/<int:audioFileID>', methods= ['GET'])
def getapi(audioFileType, audioFileID):
    try:
        if request.method == 'GET':
            if audioFileID is not None:
                cursor = dbconf.file_store.find({"audioFileType": audioFileType.lower(), 'audioFileMetadata.audio_file_id': audioFileID})
                if cursor.count() != 0:
                    for rec in cursor:
                        if rec["audioFileType"] == 'song':
                            audio_file = rec["audioFileMetadata"]["song_name"]
                        if rec["audioFileType"] == 'podcast':
                            audio_file= rec["audioFileMetadata"]["podcast_name"]
                        if rec["audioFileType"] == 'audiobook':
                            audio_file= rec["audioFileMetadata"]["audiobook_title"]
                    response = {
                            "status": 200,
                            "msg": "Sucessfull.",
                            "audioFileType": audioFileType,
                            "audio_file": audio_file
                        }
                else:
                    response = {
                            "status": 400,
                            "msg": "audio file ID is not found.",
                            "audioFileType": audioFileType,
                            "audioFileID": audioFileID
                        }
            else:
                cursor = dbconf.file_store.find({"audioFileType": str(audioFileType.lower())})
                if cursor.count() != 0:
                    audio_list = []
                    for rec in cursor:
                        if rec["audioFileType"] == 'song':
                            audio_list.append(rec["audioFileMetadata"]["song_name"])
                        if rec["audioFileType"] == 'podcast':
                            audio_list.append(rec["audioFileMetadata"]["podcast_name"])
                        if rec["audioFileType"] == 'audiobook':
                            audio_list.append(rec["audioFileMetadata"]["audiobook_title"])  
                    response = {
                            "status": 200,
                            "msg": "Sucessfull.",
                            "audioFileType": audioFileType,
                            "audio_list": audio_list
                        }
                else:
                    response = {
                            "status": 400,
                            "msg": "Audio files not found.",
                            "audioFileType": audioFileType
                        }
        else:
            response = {
                "status": 400,
                "msg": "Bad request."
            }
        return jsonify(response)
    except Exception as e:
        print(str(e))
        response = {
                "status": 500,
                "msg": "Something went wrong."
            }
        return jsonify(response)

