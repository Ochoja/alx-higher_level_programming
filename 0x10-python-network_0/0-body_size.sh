#!/usr/bin/bash
# A script that sends a request and display the size of the response body
curl -s -w '%{size_download}\n' -o /dev/null "$1"
