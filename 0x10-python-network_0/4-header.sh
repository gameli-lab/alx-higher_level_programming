#!/bin/bash
# GET Header
header="X-School-User-Id:98"; curl -X GET -H "${header}" $1 
