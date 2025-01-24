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





# issues and fixes :D

If python names.py isn't working try running `python3 names.py`

If pip install isn't working try either `python -m pip install -r requirements.txt` OR `python3 -m pip install -r requirements.txt`[^1]

If you are on Ubuntu and pip install -r requirements.txt returns an error run `pip3 install matplotlib`[^2]

If wget returns "wget: command not found" run `sudo apt install wget` for linux or download it from [here](https://gnuwin32.sourceforge.net/packages/wget.htm) for windows

If wget says that requirements.txt/names.py already exists, check your [file manager](https://letmegooglethat.com/?q=what+is+a+file+management+tool) for existing files called that.

[^1] If that still returns an error, [make sure you have python installed](https://ispythoninstalled.vercel.app)

[^2] You should probably run `rm -rf requirements.txt` to save space

