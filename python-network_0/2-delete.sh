#!/bin/bash
#this script sends a delete request to the url passed as the first argument 
curl -s -X DELETE "$1"
