#!/usr/bin/env bash

EXPERIMENT_UUID=$1
OUTPUT_PATH="results/$EXPERIMENT_UUID"

mkdir -p "$OUTPUT_PATH"

while read -r container; do
  docker cp "$container:/python-docker/out" "$OUTPUT_PATH"
  mv "$OUTPUT_PATH/out" "$OUTPUT_PATH/$container"
done < <(docker ps -a | grep "data-farmer-experiment-$EXPERIMENT_UUID" | awk '{print $1}')
