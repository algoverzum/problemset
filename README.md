# planets-problemset

### Autoformating and precommit setup guide

- Install pre-commit, black and clang-format. These are the tools used for autoformating in the project.
```bash
pip install pre-commit
pip install black
pip install clang-format
```

- Set up precommit hooks
```bash
pre-commit install
```

### Autoformat usage guide

Black and clang-format automatically checks added python and c++ files before each commit and formats them if they do not fit the formating requirements. In this case the formated files need to be added and commited again.
<br>
To avoid having to do each commit twice, run the format.py python script in the root directory, which runs formating on all .py and .cpp files in the repository.
Alternatively you can setup VSCode to automatically format files according to black and clang-format. For black, you need to download an extension
```
extension id: ms-python.black-formatter
```
<br>

If you want to run formating on a specific file, you can use these commands

- Black:
```bash
python -m black myfilename.py
```
- clang-format
```bash
clang-format -i myfilename.cpp
```