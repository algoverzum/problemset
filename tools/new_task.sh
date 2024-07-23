#!/bin/bash

if [ "$1" == "" ]; then
    echo "usage: $(basename "$0") name"
    exit 0
fi

name=$1
folder=`realpath "${0%.sh}"`
fname=`basename "$0" .sh`

echo "This script will create a new empty task of name \"$name\" into the current folder."
if [ ! -f topic.yaml ]; then
    echo "FATAL ERROR: the current folder is not a topic folder."
    exit 1
fi
echo "Press enter to proceed, CTRL-C to quit..."
read x

up=$(echo "$name" | sed "s/-/ /g;s/\b\(.\)/\u\1/g")
mkdir "$name"
mkdir "$name/gen"
mkdir "$name/sol"
mkdir "$name/statement"
sed "s/__TASK_NAME__/$name/g;s/__TASK_TITLE__/$up/g" "$folder/task.yaml" > "$name/task.yaml"
grep -v "NOTE" "$folder/t.cpp" > "$name/sol/solution.cpp"
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

sed -i.bak "s/^prerequisites:$/- problem_id: $name\n  type: REQUIRED\nprerequisites:/" topic.yaml
rm topic.yaml.bak
