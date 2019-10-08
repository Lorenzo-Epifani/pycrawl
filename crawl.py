
import urllib3 
import requests
#manage arg
import sys 
#regex
import re 
from pprint import pprint

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

    