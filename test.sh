#!/bin/bash
# Runs unit tests on the whole project

# this could fail if the DB already exists, so we set -e after this line
# ./scripts/create_test_db.sh

# stops the script if any of the commands fail
set -e

pwd

export PYTHONPATH=$PWD
export FLASK_APP=app
export FLASK_DEBUG=1
source env/bin/activate

# Load test ENV variables
# source .env.test

# nosetests --exe -w app --logging-level=INFO -v

# ls app/sparkyApiV2/tests/ -1
# ls app/services/tests/ -1
## IF you want to run individual test suites
nosetests -v --logging-level=INFO -x app/tests/course_api_test.py
# nosetests -v --logging-level=INFO -x app/services/tests/
# nosetests -v --logging-level=INFO -x app/billing/tests/
    
