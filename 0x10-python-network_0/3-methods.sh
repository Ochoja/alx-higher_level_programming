#!/bin/bash
# Script that displays all HTTP methods accepted by a server
curl -s -i -L -X OPTIONS "$1"
