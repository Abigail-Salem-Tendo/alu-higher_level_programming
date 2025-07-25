#!/bin/bash
#This displays all http methoeds the server will accept
curl -sI -X OPTIONS "$1" | grep -i "Allow:" | cut -d' ' -f2-
