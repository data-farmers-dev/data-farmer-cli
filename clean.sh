#!/bin/bash

docker ps -a | grep data-farmer-experiment | awk '{print $1}' | xargs docker rm -f

docker images | grep data-farmer-experiment | awk '{print $3}' | xargs docker image rm

docker images | grep none | awk '{print $3}' | xargs docker image rm
