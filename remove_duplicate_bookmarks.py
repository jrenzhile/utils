import os
import argparse


parser = argparse.ArgumentParser(description='Insert HouseID')
parser.add_argument('--oldpath', default='bookmarks_11_20_19.html',
                   help='the path to the old bookmark page')
parser.add_argument('--newpath', default='bookmarks_11_20_19_new.html',
                   help='the path to the old bookmark page')
args = parser.parse_args()

filepath = args.oldpath
filepath_new = args.newpath

fs = open(filepath_new, 'w');
url_dict = dict();
with open(filepath) as fp:
    for cur_line in fp:
        flag = 1;
        # track unique urls in the dictionary
        if "HREF=" in cur_line:
            i_start = cur_line.find('HREF=');
            i_end = cur_line.find('>', i_start)
            cur_string = cur_line[i_start+6:i_end-1]
            # remove "ADD_DATE" in the name
            if "ADD_DATE=" in cur_string:
                i_end = cur_string.find("ADD_DATE=")
                cur_string = cur_string[:i_end-2]

            # determine whether including the url or not
            if cur_string in url_dict:
                flag = 0
            else:
                url_dict[cur_string]=1;

        if flag > 0:
            fs.write(cur_line)

fs.close()
