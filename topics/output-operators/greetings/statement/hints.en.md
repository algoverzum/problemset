### Hint 1
To print text to the output, we need to put it between double quotes. For example: `cout << "some text;"`. But we cannot have a line break inside the double quotes, so we need to use a special *escape sequence* to print the line break, which is `\n`. Did you know that a line break is simply a character itself? We just use `\n` to represent this character in the program code. So, for example the `cout << "banana\nbanana";` command prints the two banana words on two separate lines.

### Hint 2
We need to print the text "Tutu Goro" in the first line, and "Tutu Nini" in the second. We can use two `cout <<` statements to achive this. Don't forget the semicolon (`;`) at the and of each statement.

### Hint 3
    cout << "Tutu Goro\n";
    cout << "Tutu Nini\n";
