#!/bin/bash
#Send a get request with a custom header and displays the response
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
