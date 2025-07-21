#!/bin/bash
#This script sends a get request to the url and displays the body
curl -sL -o body.txt -w "%{http_code}" "$1" | tail -c 3 | grep -q "200" && cat body.txt
