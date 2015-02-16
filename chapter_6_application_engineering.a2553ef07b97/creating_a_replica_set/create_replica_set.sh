#!/usr/bin/env bash

mkdir -p /data/nameFind1 /data/nameFind2 /data/nameFind3
mongod --replSet nameFind --logpath "1.log" --dbpath /data/nameFind1 --port 37017 --oplogSize 64 --fork --smallfiles
mongod --replSet nameFind --logpath "2.log" --dbpath /data/nameFind2 --port 37018 --oplogSize 64 --smallfiles --fork
mongod --replSet nameFind --logpath "3.log" --dbpath /data/nameFind3 --port 37019 --oplogSize 64 --smallfiles --fork
