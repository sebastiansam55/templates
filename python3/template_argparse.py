import argparse

parser = argparse.ArgumentParser(description="ArgParser Template")

parser.add_argument('required', action="store", help="Required Variable")
parser.add_argument('-v', '--verbose', dest="verbose", action="store_true", default=False, help="Verbose logging")


args = parser.parse_args()