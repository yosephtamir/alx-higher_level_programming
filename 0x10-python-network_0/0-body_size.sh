#!/usr/bin/env bash
# Used to didplay the size of the body
curl -s $1 | wc -c
