
import urllib3 
import requests
#manage arg
import sys 
#regex
import re 
import hashlib
import format
from pathlib import Path
def crawl (url):
    try:
        response = requests.get(url)
        html = response.text
        regex =r"https?://([^\./\"\n]+\.?)+/?(([^/\"\n])+/?)*"
        matches = [match.group() for match in re.finditer(regex, html, re.MULTILINE)]
        return matches
    except:
        print(f"cannot crawl {url} \n")
        return False

def seed2temp(seed):
    temp_name = hashlib.md5(repr(seed).encode('utf-8')).hexdigest()
    visiteds = crawl(seed)

    if visiteds == False:
        return False
    else:
        Path("./tmp").mkdir(parents=True, exist_ok=True)
        temp_file = open(f"./tmp/{temp_name}", 'a')
        print(f"{format.UNDERLINE}saving links in temp file ./tmp/{temp_name}{format.END}")
        temp_file.write("\n" + seed)
        for visited in visiteds:
            print(f"just extracted {visited}\n")
            temp_file.write("\n" + visited)
        temp_file.close()
        return temp_name

        
        

    


    