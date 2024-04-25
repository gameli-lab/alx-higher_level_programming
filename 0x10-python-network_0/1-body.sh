#!/bin/bash
# Body status
curl -s -o /dev/null -w ${http-status} "$1"
