#!/usr/bin/bash

cd /opt/api/binet-fibonacci && source test-api/bin/activate
export FLASK_APP=binet-fibonacci.py
flask run -h 0.0.0.0 -p 6765
