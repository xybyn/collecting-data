from MicceduParser import *
from MinobrParser import *


def main():
    MinobrParser().download_both_in_parallel(os.path.join(os.getcwd()))

if __name__ == "__main__":
    main()
