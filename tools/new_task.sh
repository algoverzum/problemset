#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "usage: $(basename "$0") [-f] name"
    exit 0
fi

force=false
name=""

for arg in "$@"; do
    if [ "$arg" == "-f" ]; then
        force=true
    else
        name="$arg"
    fi
done

if [ "$name" == "" ]; then
    echo "FATAL ERROR: Task name is required."
    echo "usage: $(basename "$0") [-f] name"
    exit 1
fi

folder=$(realpath "${0%.sh}")
fname=$(basename "$0" .sh)

existing_task=$(find "$folder/../../topics" -maxdepth 2 -type d -name "$name" 2>/dev/null)
if [ "$existing_task" != "" ]; then
    echo "WARNING: A task with the name \"$name\" already exists in the following location(s):"
    echo "$existing_task"
    if [ "$force" == false ]; then
        echo "If you want to create the task anyway, please use the -f option."
        exit 1
    fi
    echo "Continuing due to -f option..."
fi

echo "This script will create a new empty task of name \"$name\" into the current folder."
if [ ! -f topic.yaml ]; then
    echo "FATAL ERROR: the current folder is not a topic folder."
    exit 1
fi
echo "Press enter to proceed, CTRL-C to quit..."
read x

up=$(echo "$name" | sed "s/-/ /g;s/\b\(.\)/\u\1/g")
mkdir "$name"
mkdir "$name/att"
mkdir "$name/gen"
mkdir "$name/sol"
mkdir "$name/statement"
sed "s/__TASK_NAME__/$name/g;s/__TASK_TITLE__/$up/g" "$folder/task.yaml" > "$name/task.yaml"
grep -v "NOTE" "$folder/t.cpp" > "$name/sol/solution.cpp"
grep -v "NOTE" "$folder/t.py" > "$name/sol/solution_py.py"
cp "$folder/statement.tex" "$name/statement/"
sed "s/__TASK_TITLE__/$up/g" "$folder/statement.en.md" > "$name/statement/statement.en.md"
cp "$folder/hints.en.yaml" "$name/statement/"
sed "s/__TASK_TITLE__/$up/g" "$folder/statement.hu.md" > "$name/statement/statement.hu.md"
cp "$folder/hints.hu.yaml" "$name/statement/"
cat <<EOF > "$name/statement/input0.txt"
5
EOF
echo 42 > "$name/statement/output0.txt"
sed "s/__TASK_NAME__/$name/g" "$folder/generator.py" > "$name/gen/generator.py"
sed "s/__TASK_NAME__/$name/g" "$folder/GEN" > "$name/gen/GEN"
cp "$folder"/{limits.py,validator.py} "$name/gen/"
chmod a+x "$name/gen/generator.py"
ln -s "../statement/input0.txt" "$name/att/input0.txt"
ln -s "../statement/output0.txt" "$name/att/output0.txt"

sed -i.bak "/^prerequisites:/i\  - problem_id: $name\n    type: REQUIRED" topic.yaml
rm topic.yaml.bak
