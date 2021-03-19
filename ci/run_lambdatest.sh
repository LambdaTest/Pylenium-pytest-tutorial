#!/usr/bin/env bash

# 1. Define the REMOTE URL for LambdaTest
REMOTE_URL="https://$LT_USERNAME:$LT_ACCESS_KEY@hub.lambdatest.com/wd/hub"

# 2. Define the pytest command to execute
    # You can include:
    # > filters
    # > config settings
    # > if/else conditionals
    # > and so much more!
FILTER="tests/test_one_test_against_many_browsers.py" # change/override this as needed!

# 3. Execute the command
python -m pytest $FILTER --remote_url=$REMOTE_URL -n 2
