#!/usr/bash
# Used to didplay the size of the body
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
