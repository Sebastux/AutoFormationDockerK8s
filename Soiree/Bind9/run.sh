#!/bin/bash
# -*- coding: utf-8 -*-

docker run --name dns_vins -it --rm \
  -p 5353:53 \
  -h dns_vins \
  -v ./config/named.conf.local:/etc/bind/named.conf.local \
  -v ./config/db.saveuretvs.local:/etc/bind/db.saveuretvs.local \
  -v ./config/db.192.168.1:/etc/bind/db.192.168.1 \
  dns_vins:1.0.0



