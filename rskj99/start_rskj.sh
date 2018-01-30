#!/bin/bash
nohup /usr/bin/python ./manage.py runserver 0.0.0.0:9000 > nohup.out 2>&1 &
