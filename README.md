# mac-auto-typer
Auto typing with key binds for mac. 

# instructions
- clone the repository locally
- from within the directory, run `pip3 install -r requirements.txt`
- open script.py and modify:
```
# List of strings to type
strings = [
    "Hello, this is the first string.",
    "Here's the second string for you.",
    "Finally, the last string to type."
]
```
To include the strings that you need (make sure to keep the list format with the quotes for python strings)
- run `python3 script.py`
- pressing `ctrl` key will print the next line.
- pressing `esc` key will exit the script.
