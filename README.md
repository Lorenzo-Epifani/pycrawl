# PyCrawl
## A python web spider.
To see usage, run    
```
python3 launcher.py
```
The script create a temp file  in the ./tmp folder for each seed.   
The name of the temp file is calculated hashing the seed url.   
Each temp file contains in the first line, the seed itself, followed      
by the links that are extracted from.   
Finally, the temp files are merged in the original seed file    

MWE

```
python3 launcher.py
```

If the spider is stalling, press ctrl+c to move to the next url.


TODO: interrups for server error