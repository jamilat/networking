import sys
import re
import pyshark

cappath = sys.argv[1] # take in the string cap file name
capname = ''
# check valid input:
if re.search(r'/', cappath) and re.search(r'\.cap', cappath):
    match = re.match(r'(.*)/(.*\.cap)',cappath)
    capname = match[1]
    print(match.groups())
elif re.search(r'\.cap', cappath):
    capname = cappath
    print(cappath)
else:
    sys.exit('Input invalid: not a .cap file')

# open .cap file
cap = pyshark.LiveCapture(output_file=capname)
cap.sniff(timeout=32)
cap