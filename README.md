# namegrapher
namegrapher is a Python program that makes a popularity graph of names over time




## Installation

Before you start, download the "National data" of names from [here](https://www.ssa.gov/oact/babynames/limits.html) and extract it to folder of your choice. Now, open that folder in command prompt/terminal and run
```bash
  wget https://raw.githubusercontent.com/xamyl/namegrapher/refs/heads/main/names.py
  wget https://raw.githubusercontent.com/xamyl/namegrapher/refs/heads/main/requirements.txt
```
Now, open the file in a text editor and either Ctrl+F/⌘+F "directory = Path" or locate line 98 manually. 
Now change `directory = Path(r"THISISIMPORTANTCHANGME")` into where you extracted the names and names.py (e.g `C:\Users\%USERPROFILE%\names` if you extracted it there).

Now, run
```bash
  pip install -r requirements.txt
  python names.py
```
(PS If python names.py isn't working try running `python3 names.py`)

(PPS If pip install isn't working try either `python -m pip install -r requirements.txt` OR `python3 -m pip install -r requirements.txt`)

(PPPS If you can't install matplotlib first off, Hi ubuntu user! second off run `pip3 install matplotlib`)
