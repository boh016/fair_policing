import numpy as np
import pandas as pd


###############################################################################
#-------------------------stop data--------------------------------------------
# tring to identify DUI for stop data and collision data.
DUI_lst = ['CONTRABAND VISIBLE', 'ODOR OF CONTRABAND', 'DUI']

# return subset of the old stop data with only DUI related record
def old_dui(old_stop):
    copy = old_stop.copy(deep=True)
    copy = copy[~copy.search_details_description.isna()]
    copy.search_details_description = copy.search_details_description.str.upper()
    return copy[(copy.search_details_description.str.contains(DUI_lst[0]))|\
    (copy.search_details_description.str.contains(DUI_lst[1]))|\
    (copy.search_details_description.str.contains(DUI_lst[2]))]


def new_dui(new_stop):
    
