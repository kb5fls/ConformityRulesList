import argparse
import json

parser = argparse.ArgumentParser()
# note type arg, used to load json string
parser.add_argument('-l', '--list', type=json.loads)
args = parser.parse_args()
print(args.list)
