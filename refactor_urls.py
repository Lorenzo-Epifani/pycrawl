import re
import sys
import numpy

def refactor_urls_file(filename):
    r_refactor=open(filename, 'r')
    regex =r"https?://([^\./\"\n\s]+\.?)+/?(([^/\"\n\s])+/?)*"
    matches = [match.group() for match in re.finditer(regex, r_refactor.read(), re.MULTILINE)]
    matches = numpy.unique(matches)
    r_refactor.close
    w_refactor=open(filename, 'w')

    for line in matches:
        w_refactor.write(line +"\n")
    w_refactor.close()

def refactor_urls_list(listname):
    regex =r"https?://([^\./\"\n\s]+\.?)+"
    refactored_list = []

    for element in listname:
        matches = [match.group() for match in re.finditer(regex, element, re.MULTILINE)]
        refactored_list.append(matches)
    refactored_list = numpy.unique(refactored_list)
    print(f"#REFACTORED LIST{refactored_list}")

    return refactored_list
    




