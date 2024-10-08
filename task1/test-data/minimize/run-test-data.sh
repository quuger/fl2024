#!/bin/bash

TEST_CASE="minimize"

GREEN='\033[32m'
RED='\033[31m'
NC='\033[0m'
SCRIPT="solution.out"

g++ -std=c++20 ../../machine.cpp ../../minimize_main.cpp -o "$SCRIPT"
echo "==== $TEST_CASE ===="
for DIR in ./t*; do
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