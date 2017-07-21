#!/usr/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root!"
	exit 1
fi

chmod -R g+w /opt/api/binet-fibonacci

sudo -u test-api -H bash -c \
	"cd /opt/api/binet-fibonacci && virtualenv test-api; \
	source test-api/bin/activate; \
	pip install --upgrade pip; \
	pip install Flask; \
	export FLASK_APP=binet-fibonacci.py"

systemctl enable binet-fibonacci.service
systemctl start binet-fibonacci.service

