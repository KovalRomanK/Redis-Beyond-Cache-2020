import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
from flask_cors import CORS
import requests
from flask import Flask, jsonify, request
import ast
from audio_analysis import AudioAnalysis, SpotubeDownload
app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def update_product():
    val = request.get_data()
    dict_str = val.decode("UTF-8")
    values = ast.literal_eval(dict_str)
    required = ["slink", "ylink"]
    if not all(k in values for k in required):
        return 'Missing values', 400

    download = SpotubeDownload(values["ylink"], values["slink"])
    #download = SpotubeDownload(path_1, path_2)
    download.youtube_download()
    download.spotify_download()
    audio = AudioAnalysis("/root/audio_analysis/audio_dir/audio.wav", "/root/audio_analysis/video_dir/video.wav")

    val = audio.find_max_correlation()
    interval = audio.correlation_find(val)
    audio.delete_dir()
    return jsonify({"interval": interval}), 200

if __name__ == '__main__':

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5002, type=int,
                        help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
