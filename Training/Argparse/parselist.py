# Author: Phil Salem
# Date: 10/12/2022

# importing argparse module
import argparse


# create a keyvalue class
class keyvalue(argparse.Action):
    # Constructor calling
    def __call__(self, parser, namespace,
                 values, option_string=None):
        setattr(namespace, self.dest, dict())

        for value in values:
            # split it into key and value
            key, value = value.split('=')
            # assign into dictionary
            getattr(namespace, self.dest)[key] = value


# creating parser object
parser = argparse.ArgumentParser()

# adding an arguments
parser.add_argument('--kwargs',
                    nargs='*',
                    action=keyvalue)

# parsing arguments
args = parser.parse_args()

# show the dictionary
print(args.kwargs)