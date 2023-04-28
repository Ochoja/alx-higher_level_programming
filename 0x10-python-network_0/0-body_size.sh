#!/bin/bash
# A script that display the size of the response body
curl -s -w '%{size_download}\n' -o /dev/null "$1"
