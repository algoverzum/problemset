#!/bin/bash
# should be called from the root of the repo

cd topics
for dir in */
do
    if [ -d "$dir" ]; then
        cd "$dir"
        for subdir in */
        do
            if [ -d "$subdir" ]; then
                cd "$subdir"
                echo "$subdir"
                task-maker-rust 
                cd ..
            fi
        done
        cd ..
    fi
done
cd ..

