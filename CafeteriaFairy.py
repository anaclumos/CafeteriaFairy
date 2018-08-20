"""

CafeteriaFairy.py
급식요정.py

Developed by Sunghyun Cho on August 19th, 2018.

This code is under GPL 3.0 license.
Anyone can reuse this code under the following conditions:
    0. Explicitly mention "Sunghyun Cho" as the original creator.
    1. If this code is reused in any public manner, the entire project code should be disclosed.
    2. If any part of the code is changed, the difference should be explicitly mentioned.
    3. Every code derived from this code should keep the GPL 3.0 license.


"""
#----------------------------

# Set target URL to copy HTML data.
def set_target_URL(regionCode, accessCode, schoolCode, schoolName):
    return "http://"+regionCode+"/"+ accessCode+"?"+"schulCode="+schoolCode+"&insttNm="+schoolName+"&schulCrseScCode=4&schMmealScCode="+str(timePeriod)

#----------------------------

# copy HTML data from a given URL.
def get_HTML_from(url):
    print("Copying HTML data from " + url + "...")
    import requests
    dataHTML = ""
    data = requests.get(url)
    if data.status_code == 200:
        dataHTML = data.text
    print("Done.\n")
    return dataHTML

#----------------------------

# fetch code of table part from given HTML data.
def fetch_Table_From(dataHTML):
    print("Fetching table...")
    from lxml import html
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(dataHTML, "lxml")
    rows = soup.table.find_all("tr")
    print("Done.\n")
    return rows

#----------------------------

# set JSON keys to input data.
# in this case, key would be the "date," and value would be the "food info."
def set_JSON_key_with(table, dictionary):
    print("Setting JSON keys...")
    firstRow = table.pop(0)
    for h in firstRow.find_all("th"):
        temp = [h.text.strip()]
        if temp[0] != "":
            dictionary[temp[0]] = {}
    print("Done.\n")
#----------------------------

# extract data from HTML string to fill dictionary.
def extract_data_and_fill_dictionary_from(table, dictionary, keychain):
    print("Filling up dictionary...")
    for n in range(len(table)):
        th = table[n].find_all("th")
        td = table[n].find_all("td")
        ah = []
        ad = []
        for h in th:
            temph = h.text.strip()
            ah.append(temph)
        for d in td:
            tempd = d.text.strip()
            ad.append(tempd)

        if len(ah) != 1 or len(ad) != 7:
            continue
        else:
            for x in range(7):
                dictionary[keychain[x]][ah[0]] = ad[x]
    print("Done.\n")
#----------------------------

# In order to replace preformatted HTML value (which is illegible,)
# this part prettyformats food list with HTML <br/> tag.
def substitude_value_from(table, dictionary, keychain, timePeriod):
    print("Prettyformatting food data...")
    days = str(table[1]).split("</td>")
    result = []
    if timePeriod == 1:
        foodtype = "조식"
    elif timePeriod == 2:
        foodtype = "중식"
    else:
        foodtype = "석식"
    for day in days:
        oneday = day.split("<br/>")[:-1]
        for x in range(len(oneday)):
            if ">" in oneday[x]:
                oneday[x] = oneday[x][oneday[x].rfind(">") + 1:]
        if oneday != "":
            result.append(oneday)
    for x in range(7):
        dictionary[keychain[x]][foodtype] = result[x]
    print("Done.\n")

#----------------------------

# creates JSON file from dictionary, and save it to a target folder with expected file name.
def export_to_JSON_from(dictionary, expectedFileName, targetFolder):
    import os
    import json
    projectFolder = os.path.dirname(os.path.abspath(__file__))
    filename = projectFolder + "/" + targetFolder + "/" + expectedFileName+ ".json"
    print("Exporting JSON File to " + filename + "...")
    with open(filename, "w") as fp:
        fp.write(json.dumps(dictionary, indent=4, sort_keys=False, ensure_ascii=False))
    print("Done.\n")

#----------------------------

# Creates a file name with schoolname and time period.
# For example, file containing dinner info of the 34th week
# in Stanford will be named "Stanford343"
def make_file_name_with(schoolName, timePeriod):
    import datetime
    today = datetime.date.today()
    week = today.isocalendar()[1]
    year = today.year
    if week < 10:
        week = "0" + str(week)
    return schoolName + str(year) + str(week) + str(timePeriod)

#----------------------------

# School data.
regionCode = "stu.kwe.go.kr"
accessCode = "sts_sci_md01_001.do"
schoolCode = "K100000414"
schoolName = "민족사관고등학교"

#----------------------------

# Main method.
for timePeriod in range(1,4):
    FoodData = {}
    targetURL = set_target_URL(regionCode, accessCode, schoolCode, schoolName)
    dataHTML = get_HTML_from(targetURL)
    table = fetch_Table_From(dataHTML)
    set_JSON_key_with(table, FoodData)
    keychain = list(FoodData.keys())
    extract_data_and_fill_dictionary_from(table, FoodData, keychain)
    substitude_value_from(table, FoodData, keychain, timePeriod)
    expectedFileName = make_file_name_with(schoolName, timePeriod)
    export_to_JSON_from(FoodData, expectedFileName, "/FoodJSON")
