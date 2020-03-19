#!/bin/sh
cd /stanford-corenlp
nohup java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos -status_port 9000 -port 9000 -timeout 15000 > /dev/null 2>&1 &
cd /app

python api.py
