#!/bin/bash
#used to catch and show options
curl -sI $1 | grep Allow | cut -d ' ' -f2-
