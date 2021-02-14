from utils import *
from XLSParser import *


def main():
    archives_path = os.path.join(os.getcwd()) + "\\archives\\"
    unarchived_path = os.path.join(os.getcwd()) + "\\unarchived\\"

    # unarchive(archives_path, unarchived_path)

    # Р2_1_1 Р2_1_2(1) Р2_1_2 (4) Р2_1_3(1) Р2_12(все)

    XLSParser().parse(unarchived_path + "/VPO-1_za_2019_g..rar/ВПО-1 2019/Выходные файлы ВПО-1 2019/t1a_.xls")


if __name__ == "__main__":
    main()
