import crawl
import sys
import numpy
from refactor_urls import limit_urls_list
from refactor_urls import refactor_urls_file
from refactor_urls import merge_tmp

import format
import random
#TODO 
#manage a timer that closes connections that doesn t respond
#implement full depth search
#delete temp files
full_depth = False

if len(sys.argv) == 1:
    print('\nUsage\n\n')
    print(f'{format.BOLD}python3 launcher.py{format.END} ' +
          f'{format.UNDERLINE}seeds-filename.txt{format.END} ' +
          f'{format.BOLD}[--full_depth]{format.END}\n\n')
    print('\n"--full_depth" is under development. A "tmp" folder must exist in the root folder of the script ')
    
else:
    SEEDS_FILENAME= sys.argv[1]
    
    for arg in sys.argv:
        if arg == "--full_depth":
            full_depth=True
        if arg == "opt2":
            pass

    refactor_urls_file(SEEDS_FILENAME, full_depth)        
    read_seeds=open(SEEDS_FILENAME, 'r')
    to_merge = []
    count=0
    
    for seed in read_seeds:
        count +=1
        print(f"visiting seed #{count}\n")
        seed = seed.strip('\n')
        tmp_filename=crawl.seed2temp(seed)

        if tmp_filename == False:
            print('CRAWL_ERROR--bad url')
            continue
        else:
            to_merge.append(tmp_filename)

    print(f'{format.BOLD}\n\n{format.END}')
    print(f'{format.UNDERLINE}Merging temp files{format.END}')            
    tmp_merged_list=merge_tmp(to_merge)
    read_seeds.close()

    append_seeds = open(SEEDS_FILENAME, 'a')
    print(f'{format.BOLD}\n\n{format.END}')
    print(f'{format.UNDERLINE}Saving in--->{SEEDS_FILENAME}{format.END}')            
    for element in tmp_merged_list:
        append_seeds.write(element + "\n")
    append_seeds.close()

    print(f'{format.BOLD}\n\n{format.END}')
    print(f'{format.UNDERLINE}Refactoring url list{format.END}')
    refactor_urls_file(SEEDS_FILENAME,full_depth)

    print(f'{format.BOLD}\n\n{format.END}')
    print(f'{format.BOLD}Crawl cycle terminated{format.END}')
