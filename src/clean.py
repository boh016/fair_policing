import numpy as np
import pandas as pd


###############################################################################
#-------------------------stop data--------------------------------------------
# tring to identify DUI for stop data and collision data.
DUI_lst = ['CONTRABAND VISIBLE', 'ODOR OF CONTRABAND', 'DUI']

rename_dict = {
    'perceived_age':'subject_age',\
    'perceived_gender':'subject_sex',\
    'result':'arrested',\
    'reason_for_stop_detail':'stop_cause',\
    'basis_for_search':'searched',\
    'race':'subject_race',\
    'type_of_property_seized':'property_seized',\
    'contraband':'contraband_found'}


# return subset of the old stop data with only DUI related record
def old_dui(old_stop):
    copy = old_stop.copy(deep=True)
    copy = copy[~copy.search_details_description.isna()]
    copy.search_details_description = copy.search_details_description.str.upper()
    return copy[copy.search_details_description.str.contains("DUI")]

# return subset of the new stop data with only DUI related record
def new_dui(new_stop):
    copy = new_stop.copy(deep=True)
    copy.reason_for_stop_explanation = copy.reason_for_stop_explanation.str.upper()
    return copy[copy.reason_for_stop_explanation.str.contains("DUI")]

# standardize df according to the full columns
def standardize(df,cols):
    result = df.rename(rename_dict,axis=1)
    # find cols that are not in df
    cols_series = pd.Series(cols)
    not_in = cols_series[~cols_series.isin(result.columns)]
    for col in not_in:
        result[col] = np.NaN
    result = result[cols]
    return result

# clean race by Asian,pacific, black, hispanic, white, other/nan  A,P,B,H,W,O
def clean_old_race(x):
    if not isinstance(x,str):
        return np.NaN
    elif x.upper() in ['B','O','W','H']:
        return x.upper()
    elif x.upper() in 'A C D F I J K L V Z'.split():
        return 'A'
    elif x.upper() in  'G P S U'.split():
        return 'P'
    else:
        return 'O'

def clean_new_race(x):
    if x.upper() == "White".upper():
        return 'W'
    elif x.upper() == "Hispanic/Latino/a".upper():
        return 'H'
    elif x.upper() == "Black/African American".upper():
        return 'B'
    elif x.upper() == "Native American".upper():
        return 'O'
    elif x.upper() == "Middle Eastern or South Asian".upper():
        return 'A'
    elif x.upper() == "Asian".upper():
        return 'A'
    elif x.upper() == "Pacific Islander".upper():
        return 'P'
    elif not isinstance(x,str):
        return np.NaN
    else:
        return 'O'

# derive the new version service area from beat
def new_to_service(x):
    if np.isnan(x):
        return np.NaN
    else:
        return int(x//10*10)

def clean_old_service(x):
    if isinstance(x,str) and x.upper() == 'Unknown'.upper():
        return np.NaN
    else:
        return int(x)

# clean subject_age may contain NaN, so type becomes float
def clean_age(x):
    try:
        return float(x)
    except:
        return np.NaN

# clean sex based on the old version 'M','F','X',nan
def clean_sex(x):
    if not isinstance(x,str):
        return np.NaN
    elif x.upper() in ['F','FEMALE']:
        return 'F'
    elif x.upper() in ['M','MALE']:
        return 'M'
    else:
        return 'X'

def clean_time(df):
    temp = df[~pd.isnull(df.time_stop)]
    temp.time_stop = temp.time_stop.str.extract('([0-9]+:[0-9]+)')
    temp.time_stop = pd.to_datetime(temp.time_stop,errors='coerce')
    return temp

# clean old verison searched, arrested, contraband_found, and property_seized
def clean_old_post(x):
    if not isinstance(x,str):
        return np.NaN
    else:
        return x.upper()

# clean new version searched, contraband_found,property_seized based on
# https://oag.ca.gov/sites/all/files/agweb/pdfs/ripa/stop-data-reg-final-text-110717.pdf?
def clean_new_post(x):
    if not isinstance(x,str):
        return 'N'
    else:
        if x.upper() == 'NONE':
            return 'N'
        else:
            return 'Y'

old_clean = {"service_area":clean_old_service,"subject_race":clean_old_race\
,"subject_age":clean_age,"subject_sex":clean_sex,"searched":clean_old_post,\
"arrested":clean_old_post,"contraband_found":clean_old_post,"property_seized":clean_old_post}


new_clean = {"subject_race":clean_new_race\
,"subject_age":clean_age,"subject_sex":clean_sex,"searched":clean_new_post,\
"arrested":clean_new_arrest,"contraband_found":clean_new_post,"property_seized":clean_new_post}

###############################################################################
#-------------------------collision data--------------------------------------------
# return subset of the collision data with only DUI related record
def collision_dui(collision_df):
    return collision_df[collision_df.charge_desc.str.contains("DUI")]
