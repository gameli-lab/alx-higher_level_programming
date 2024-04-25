#!/usr/bin/bash
# Body size
curl -sS "$1" -o size && stat -c %s size && rm size
