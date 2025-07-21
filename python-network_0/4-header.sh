#!/bin/bash
#Send a get request with a custom header and displays the response
curl -v -X GET -H "X-HolbertonSchool-User-Id: 98" 0.0.0.0:5000/route_5
