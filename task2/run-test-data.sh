#!/bin/bash

TEST_DIR="test-data"

GREEN='\033[32m'
RED='\033[31m'
NC='\033[0m'

PYTHON_SCRIPT="2.py"

for DIR in "$TEST_DIR"/t*; do
    
    if [[ -f "$PYTHON_SCRIPT" ]]; then
        cd "$DIR" || exit

        > out.txt

        for test_file in tests/*; do
            python3 "../../$PYTHON_SCRIPT" < "$test_file" >> out.txt
        done

        if diff -q out.txt ans.txt > /dev/null; then
            echo -e "${GREEN}$DIR DONE!${NC}"
        else
            echo -e "${RED}$DIR FAIL${NC}"
            diff out.txt ans.txt
        fi
        
        cd - > /dev/null
    else
        echo "$PYTHON_SCRIPT not found!"
        exit 1
    fi
done