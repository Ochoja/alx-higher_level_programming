#!/usr/bin/bash
# A script that sends a request to a URL and display the size of the response body
curl -s -w '%{size_download}\n' -o /dev/null "$1"
