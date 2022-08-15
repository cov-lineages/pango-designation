#!/bin/bash

if [[ $(./findDups.sh) ]]; then
    exit 1
else
    exit 0
fi
