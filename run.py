import sys
import json
import os
import shutil
import re
import pandas as pd

sys.path.insert(0, 'src')
import fetch
import clean

STOP_PARAMS = 'config/stop-params.json'
#not yet implemented
COLLISION_PARAMS = 'config/collision-params.json'

STOP_PROC_PARAMS = 'config/stop-process-params.json'
# not yet implemented
COLLISION_PROC_PARAMS = 'config/collision-process-params.json'


TEST_STOP_PARAMS = 'config/test-stop-params.json'
# not yet implemented
TEST_COLLISION_PARAMS = 'config/test-collision-params.json'


def load_params(fp):
    with open(fp) as fh:
        param = json.load(fh)
    return param

# fetch raw stop data into temp
def get_stop(years,out):
    for y in years:
        if y < 2018:
            data = fetch.fetch_old(y)
            data.to_csv(out+"raw_stop_"+str(y)+".csv")
        else:
            data = fetch.fetch_new(y)
            data.to_csv(out+"raw_stop_"+str(y)+".csv")
    return

def get_collision():
    return

# find raw data in temp, clean it and write to out
def process_stop(cols,out):
    f_lst = os.listdir("./data/temp")
    for f in f_lst:
        if "raw_stop" in f:
            data = pd.read.csv("./data/temp/"+f)
            data = clean.standardize(data,cols)
            year = ''
            for i in f:
                if i.isdigit():
                year += i
            year = int(year)
            if year < 2018:
                for c in clean.old_clean.keys():
                    data[c] = data[c].apply(clean.old_clean[c])
                data.to_csv(out+"proc_stop_"+str(year)+".csv")
            else:
                for c in clean.new_clean.keys():
                    data[c] = data[c].apply(clean.new_clean[c])
                data.to_csv(out+"proc_stop_"+str(year)+".csv")
    return

def process_collision():
    return



def main(targets):

    # make the clean target
    if 'clean' in targets:
        if os.path.isdir("./data"):
            shutil.rmtree('./data/temp',ignore_errors=True)
            shutil.rmtree('./data/out',ignore_errors=True)
            shutil.rmtree('./data/test',ignore_errors=True)

            os.mkdir("./data/temp")
            os.mkdir('./data/out')
            os.mkdir('./data/test')
        else:
            os.mkdir("./data")
            os.mkdir("./data/temp")
            os.mkdir('./data/out')
            os.mkdir('./data/test')

    if 'stop_data' in targets:
        cfg = load_params(STOP_PARAMS)
        get_stop(**cfg)

# not yet implemented
    if 'collision_data' in targets:
        cfg = load_params(COLLISION_PARAMS)
        get_collision(**cfg)

    if 'process_stop' in targets:
        cfg = load_params(STOP_PROC_PARAMS)
        process_stop(**cfg)

# not yet implemented
    if 'process_collision' in targets:
        cfg = load_params(COLLISION_PROC_PARAMS)
        process_collision(**cfg)


    if 'stop-test' in targets:
        cfg = load_params(TEST_STOP_PARAMS)
        get_stop(**cfg)

#    if 'test-project' in targets:
#        if os.path.isdir("./data"):
#            shutil.rmtree('./data/temp',ignore_errors=True)
#            shutil.rmtree('./data/out',ignore_errors=True)
#            shutil.rmtree('./data/test',ignore_errors=True)
#
#            os.mkdir("./data/temp")
#            os.mkdir('./data/out')
#            os.mkdir('./data/test')
#        else:
#            os.mkdir("./data")
#            os.mkdir("./data/temp")
#            os.mkdir('./data/out')
#            os.mkdir('./data/test')
#        data_cfg = load_params(TEST_PARAMS)
#        get_data(**data_cfg)
#        clean_cfg = load_params(PROCESS_PARAMS)
#        process_data(**clean_cfg)
#        analysis_cfg = load_params(ANALYSIS_PARAMS)
#        output_analysis(**analysis_cfg)

    return


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
