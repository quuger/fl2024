#!/bin/bash

TEST_DIR="test-data"

GREEN='\033[32m'
RED='\033[31m'
NC='\033[0m'
SCRIPT="solution.out"

for CASE in "$TEST_DIR"/*; do
    cd "$CASE" || exit
    bash build.sh
    cd ../..
    for DIR in "$CASE"/t*; do
        cd "$DIR" || exit
        "../$SCRIPT" <in.txt >out.txt

        if diff -q out.txt ans.txt > /dev/null; then
            echo -e "${GREEN}$DIR DONE!${NC}"
        else
            echo -e "${RED}$DIR FAIL${NC}"
            diff out.txt ans.txt
        fi

        cd - > /dev/null
    done
done