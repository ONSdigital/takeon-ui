#!/bin/bash

#This script runs load test with selenium. Currently it can run upto 18 requests. Beyond this the Chrome adapter crashes.
#Before running it, set the parameters in config_test.py
for i in {1..18}; do
    now=`date`
    echo "Test: $i , Current DateTime: $now"
    python3 load_check.py &
    done
