from utils import *
from XLSParser import *
from MinobrParser import *


def main():
    archives_path = os.path.join(os.getcwd()) + "\\archives\\"
    unarchived_path = os.path.join(os.getcwd()) + "\\unarchived\\"

    # unarchive(archives_path, unarchived_path)

    # Р2_1_1 Р2_1_2(1) Р2_1_2 (4) Р2_1_3(1) Р2_12(все)
    # "2013", "2014", "2015", "2016"
    years = ["2017", "2018", "2019", "2020"]

    for year in years:
        print(year)
        XLSParser().export_year_to_json(unarchived_path + f"VPO_1_{year}/Своды ВПО-1 {year}", year,
                                        f"yearVPO{year}.json")

if __name__ == "__main__":
    main()
