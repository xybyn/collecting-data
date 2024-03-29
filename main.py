from GovEduParser import *
from XLSParserSPO import XLSParserSPO
from XLSParserVPO import XLSParser


def main():
    archives_path = os.path.join(os.getcwd()) + "\\archives\\"
    gov_path = os.path.join(os.getcwd()) + "\\gov\\"
    gov_unarch_path = os.path.join(os.getcwd()) + "\\gov_unarch\\"
    unarchived_path = os.path.join(os.getcwd()) + "\\unarchived\\"

    # unarchive(archives_path, unarchived_path)

    # Р2_1_1 Р2_1_2(1) Р2_1_2 (4) Р2_1_3(1) Р2_12(все)
    # "2013", "2014", "2015", "2016"
    #years = ["2013", "2014", "2015"]
    years = ["2015"]

    for year in years:
         print(year)
         XLSParserSPO().export_year_to_json_old(gov_path + f"{year}\\Своды СПО-1 {year}\\Государственные", year,
                                                os.path.join(os.getcwd()) + f"\\{year}-spo\\" + f"yearVPO{year}")

    #for year in years:
     # print(year)
      #XLSParser().export_year_to_json_old(unarchived_path + f"VPO_1_{year}/Своды ВПО-1 {year}", year,
                                     # os.path.join(os.getcwd()) + f"\\{year}-vpo\\" + f"yearVPO{year}-new")

    # unarchive(gov_path + f"folder {12}\\", gov_unarch_path)


if __name__ == "__main__":
    main()
