#!/bin/bash
# -*- coding: utf-8 -*-

clear

docker image prune -af

docker build -t webmin-test:1.0.0 .
