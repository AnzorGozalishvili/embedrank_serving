#!/usr/bin/env python

import launch

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def analyzer():
    query = request.args.get('q')
    lang = request.args.get('lang')
    top_n = int(request.args.get('n', 15))

    keywords = launch.extract_keyphrases(embedding_distributor, pos_tagger, query, top_n, lang)

    return jsonify(keywords)


if __name__ == '__main__':
    embedding_distributor = launch.load_local_embedding_distributor()
    pos_tagger = launch.load_local_corenlp_pos_tagger()

    app.run(host='0.0.0.0', port=5000)
