#!/bin/sh
# run stanford corenlp server on back process
cd /stanford-corenlp
nohup java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos -status_port 9000 -port 9000 -timeout 15000 > /dev/null 2>&1 &
cd /app

# run flask api
python api.py
