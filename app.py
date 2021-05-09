from flask import Flask, jsonify, request

from api.fileupload import file_upload

app = Flask(__name__)

app.register_blueprint(file_upload, url_prefix='/files')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug = True)


