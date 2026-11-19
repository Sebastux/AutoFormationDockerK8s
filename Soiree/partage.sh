#!/bin/bash
# -*- coding: utf-8 -*-

rm -vf ./IA/*

cp -v ./Bind9/Dockerfile ./IA/Dockerfile_bind
cp -v ./mariadb/Dockerfile ./IA/Dockerfile_mariadb
cp -v ./nginx/Dockerfile ./IA/Dockerfile_nginx
cp -v ./php/Dockerfile ./IA/Dockerfile_php
cp -v ./phpmyadmin/Dockerfile ./IA/Dockerfile_phpmyadmin
cp -v ./docker-compose.yaml ./IA/docker-compose.yaml
cp -v ./docker-compose_DB.yaml ./IA/docker-compose_DB.yaml





