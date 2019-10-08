import crawl
import sys
import numpy
from refactor_urls import refactor_urls_list
from refactor_urls import refactor_urls_file
#TODO 
#manage a timer that closes connections that doesn t respond
#implement full depth search

if len(sys.argv) == 1:
    print('\nUsage:\n\narg1:seed files\narg2(optional): --safe')
else:
    SEEDS_FILENAME= sys.argv[1]
    for arg in sys.argv:
        if arg == "--safe":
            safe=True
        if arg == "opt2":
            pass
        
    if safe:
        refactor_urls_file(SEEDS_FILENAME)
        
    r_seeds=open(SEEDS_FILENAME, 'r')
    results = []
    count=0
    for seed in r_seeds:
        count +=1
        print(f"visiting seed #{count}\n")
        seed = seed.strip('\n')
        visiteds= crawl.crawl(seed)
        for visited in visiteds:
            print(f"just extracted {visited}\n")
            results.append(visited)

    results = refactor_urls_list(results)
    r_seeds.close()
    a_seeds=open(SEEDS_FILENAME, 'a')
    for element in results:
        a_seeds.write(element + "\n")

    a_seeds.close()
