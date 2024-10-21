#!/bin/bash

TEST_DIR="test-data"

for CASE in "$TEST_DIR"/*; do
    cd "$CASE" || exit
    bash run-test-data.sh
    cd - > /dev/null
done