#!/usr/bin/env python

from flask import Flask, jsonify, request

import launch

app = Flask(__name__)


@app.route("/", methods=['POST'])
def analyzer():
    data = request.json
    query = data.get("text", "")
    lang = data.get("lang", "en")
    top_n = int(data.get("n", 15))

    keywords = launch.extract_keyphrases(embedding_distrib=embedding_distributor, ptagger=pos_tagger,
                                         raw_text=query, N=top_n, lang=lang)

    return jsonify(keywords)


if __name__ == '__main__':
    embedding_distributor = launch.load_local_embedding_distributor()
    pos_tagger = launch.load_local_corenlp_pos_tagger()

    app.run(host='0.0.0.0', port=5000)
