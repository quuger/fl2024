#!/bin/bash

TEST_DIR="test-data"

GREEN='\033[32m'
RED='\033[31m'
NC='\033[0m'
SCRIPT="a.out"
g++ -std=c++17 2.cpp >$SCRIPT

for DIR in "$TEST_DIR"/t*; do
    
    if [[ -f "$SCRIPT" ]]; then
        cd "$DIR" || exit

        "../../$SCRIPT" < input.txt > out.txt
        
        if diff -q out.txt ans.txt > /dev/null; then
            echo -e "${GREEN}$DIR DONE!${NC}"
        else
            echo -e "${RED}$DIR FAIL${NC}"
            diff out.txt ans.txt
        fi
        
        cd - > /dev/null
    else
        echo "$SCRIPT not found!"
        exit 1
    fi
done