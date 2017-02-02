# zillions-of-redirects
Python script that uses a CSV to build individual 301 redirects for an entire Website

First, get a recursive list of all files in all directories, and their full paths, and save this to a CSV.

find $PWD -iname '*.asp' > 1files.csv

Add and populate a couple columns to this CSV (easiest in Excel or a similar program), to cover the current URLs and the new URLs.

Run this script in Python 3. Macs ship with Python 2.7 so you'll have to install Python 3 and then from the terminal prompt, type this:

python3 createFiles.py

That should do the trick!
