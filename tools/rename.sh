#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage: $(basename "$0") [-f] old_name new_name"
    exit 1
fi

# Initialize variables
force=false
old_name=""
new_name=""

# Parse arguments dynamically
for arg in "$@"; do
    if [ "$arg" == "-f" ]; then
        force=true
    elif [ -z "$old_name" ]; then
        old_name="$arg"
    elif [ -z "$new_name" ]; then
        new_name="$arg"
    else
        echo "ERROR: Too many arguments. Usage: $(basename "$0") [-f] old_name new_name"
        exit 1
    fi
done

# Ensure both old_name and new_name are provided
if [ -z "$old_name" ] || [ -z "$new_name" ]; then
    echo "ERROR: Both old_name and new_name must be provided."
    echo "Usage: $(basename "$0") [-f] old_name new_name"
    exit 1
fi

# Ensure the old_name is a directory in the current working directory
if [ ! -d "$old_name" ]; then
    echo "ERROR: Task directory \"$old_name\" does not exist in the current working directory."
    exit 1
fi

# Check for duplication of the new_name
folder=$(realpath "${0%/*}")
existing_task=$(find "$folder/../topics" -maxdepth 2 -type d -name "$new_name" 2>/dev/null)
if [ "$existing_task" != "" ]; then
    echo "WARNING: A task with the name \"$new_name\" already exists in the following location(s):"
    echo "$existing_task"
    if [ "$force" == false ]; then
        echo "If you want to rename the task anyway, please use the -f option."
        exit 1
    fi
    echo "Continuing due to -f option..."
fi

# Rename the task directory
mv "$old_name" "$new_name"

# Compute titles
old_title=$(echo "$old_name" | sed "s/-/ /g;s/\b\(.\)/\u\1/g")
new_title=$(echo "$new_name" | sed "s/-/ /g;s/\b\(.\)/\u\1/g")

# Update task.yaml
if [ -f "$new_name/task.yaml" ]; then
    sed -i "s/^name: $old_name$/name: $new_name/" "$new_name/task.yaml"
    sed -i "s/^title: $old_title$/title: $new_title/" "$new_name/task.yaml"
    sed -i "s/^  hu: $old_title$/  hu: $new_title/" "$new_name/task.yaml"
fi

# Update topic.yaml
if [ -f "$new_name/../topic.yaml" ]; then
    sed -i "s/^  - problem_id: $old_name$/  - problem_id: $new_name/" "$new_name/../topic.yaml"
fi

# Update the title in statement.en.md
if [ -f "$new_name/statement/statement.en.md" ]; then
    current_title=$(head -n 1 "$new_name/statement/statement.en.md" | sed 's/^## //')
    if [ "$current_title" == "$old_title" ]; then
        sed -i "1s/.*/## $new_title/" "$new_name/statement/statement.en.md"
    fi
fi

# Update the title in statement.hu.md
if [ -f "$new_name/statement/statement.hu.md" ]; then
    current_title=$(head -n 1 "$new_name/statement/statement.hu.md" | sed 's/^## //')
    if [ "$current_title" == "$old_title" ]; then
        sed -i "1s/.*/## $new_title/" "$new_name/statement/statement.hu.md"
    fi
fi

# Update the usage line in generator.py
if [ -f "$new_name/gen/generator.py" ]; then
    sed -i "s/Generator for \"$old_name\"/Generator for \"$new_name\"/" "$new_name/gen/generator.py"
fi

echo "Task \"$old_name\" has been successfully renamed to \"$new_name\"."
echo "Please check and rename the Hungarian translation manually if needed."