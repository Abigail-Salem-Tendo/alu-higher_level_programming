#!/bin/bash
#SEnd a get request with a custom header and displays the respnse
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
