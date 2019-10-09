# PyCrawl
## A python web crawler.
To see usage, run    
```
python3 launcher.py
```
The script create a temp file  in the ./tmp folder for each seed.
Each temp file contains the links that are extracted from the seed that it refers to.
The name of the temp file is calculated hashing the seed url.
Finally, the temp files are merged in the original seed file
