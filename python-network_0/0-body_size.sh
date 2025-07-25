#!/bin/bash
#This script gets the size of the response body in bytes from a given url
curl -s "$1" -o /dev/null -w "%{size_download}\n"
