import re
import sys
import numpy
from pathlib import Path

def refactor_urls_file(filename, full_depth):

    if full_depth:
        regex =r"https?://([^\./\"\n\s]+\.?)+/?(([^/\"\n\s])+/?)*"
    else:
        regex =r"https?://([^\./\"\n\s]+\.?)+"

    r_refactor=open(filename, 'r')
    matches = [match.group() for match in re.finditer(regex, r_refactor.read(), re.MULTILINE)]
    matches = numpy.unique(matches)
    r_refactor.close
    w_refactor=open(filename, 'w')

    for line in matches:
        w_refactor.write(line +"\n")
    w_refactor.close()



def limit_urls_list(listname):
    regex =r"https?://([^\./\"\n\s]+\.?)+"
    refactored_list = []

    for element in listname:
        matches = [match.group() for match in re.finditer(regex, element, re.MULTILINE)]
        refactored_list.append(matches)
    refactored_list = numpy.unique(refactored_list)
    print(f"#REFACTORED LIST{refactored_list}")

    return refactored_list

def merge_tmp(tmp_list):
    merged_list = []

    for filename in tmp_list:
        Path("./tmp").mkdir(parents=True, exist_ok=True)
        file_tmp = open(f"./tmp/{filename}", 'r')

        for url in file_tmp:
            url = url.strip('\n')
            merged_list.append(url)
        file_tmp.close()
        merged_list = numpy.unique(merged_list)
        merged_list = numpy.ndarray.tolist(merged_list)
    return merged_list

    

    




