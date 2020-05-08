#!/bin/bash


output=`python3 /home/ucare/test.py`
echo "$output"


curl -X POST --data-urlencode "payload={\"message\": \"yuhung\", \"username\": \"CONVID-19\", \"text\": \"$output in Taiwan\"}" https://hooks.slack.com/services/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



