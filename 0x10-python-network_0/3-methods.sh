#!/bin/bash
#used to catch and show options
curl -sI $! | grep Allow | cut -d ' ' -f2-
