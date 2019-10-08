
import urllib3 
import requests
#manage arg
import sys 
#regex
import re 
from pprint import pprint

def crawl (url):
    response = requests.get(url)
    html = response.text
    regex =r"https?://([^\./\"\n]+\.?)+/?(([^/\"\n])+/?)*"
    matches = [match.group() for match in re.finditer(regex, html, re.MULTILINE)]
    return matches