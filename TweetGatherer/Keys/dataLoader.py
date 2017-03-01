import json

import data


def get_keys():
    try:
        with open('Keys/key.json') as f:
            data.key = json.load(f)
    except IOError as e:
        print "Unable to open key file"  # Does not exist OR no read permissions


def get_file_tracker_data():
    try:
        with open('fileTrackerData.json') as f:
            data.fileTrackerData= json.load(f)
    except IOError as e:
        print "Unable to open fileTrackerData file"  # Does not exist OR no read permissions
        update_file_tracker_data(0, 0)


def update_file_tracker_data(tweetNum, fileNum):
    data.fileTrackerData['tweetNum'] = tweetNum
    data.fileTrackerData['fileNum'] = fileNum
    out_file = open("fileTrackerData.json", "w")
    json.dump(data.fileTrackerData, out_file, indent=4)
    out_file.close()

