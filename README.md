# 60lminesweeper
## what?

This is a CLI minesweeper application written in 60 LoC python. 
You can use `d row,column` to dig and `f row,column` to flag/unflag

## okay, but why?

A few days ago I had the following conversation with my friends:
- "I mean, minesweeper is easy, I can do it in 60 lines"
- "Naaaah, it'll take more lines"
- "I'll do it in 60 lines of python code, where I can only use 5 instructions per line"
- "OK, do it"

So that's why

## what are the files?

|Filename |Purpose |
--- | --- |
|main.py|the program with the most features under 60 LoC|
|main-min.py|the program with the least amount of LoC while having the functionality of the minesweeper|
|main-readable.py|main.py but readable and commented|
|main-min-readable.py|main-min.py but readable and commented|

## what are the criteria?

This is arbitrary, but the criteria is the following:
- under 60 LoC
- no base64 packed code
- no eval() or exec()
- no reading other files for code
- no importing other libraries, no `import X` or `from X import Y`
- maximum 5 instructions per line, meaning only 4 `;` per line
- features:
   - be able to dig
   - be able to flag
   - can die or win
   - display map, but only display digged fields
