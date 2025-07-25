#!/bin/bash
#this script takes a url sends a POST and displays the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
