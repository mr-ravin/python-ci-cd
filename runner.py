import argparse
parser = argparse.ArgumentParser(
                    prog='Python program with minimalistic CI/CD',
                    description='Python program with minimalistic CI/CD along with test code',
                    epilog='')
parser.add_argument('-mode', '--mode')
args = parser.parse_args()
mode = args.mode
if mode == "production":
    print("production code was running.")
else:
    print("testing code was running.")