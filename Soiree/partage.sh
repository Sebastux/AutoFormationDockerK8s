#!/bin/bash
# -*- coding: utf-8 -*-

rm -f /IA/*

cp ./Bind9/Dockerfile ./IA/Dockerfile_bind
cp ./mariadb/Dockerfile ./IA/Dockerfile_mariadb
cp ./nginx/Dockerfile ./IA/Dockerfile_nginx
cp ./php/Dockerfile ./IA/Dockerfile_php
cp ./docker-compose.yaml ./IA/docker-compose.yaml
