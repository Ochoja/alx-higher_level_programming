#!/bin/bash
# Script that displays all HTTP methods accepted by a server
curl -s -i -L -X OPTIONS "$1" | grep "allow" | tr -d "allow: " | sed 's/, */, /g'
