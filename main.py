from MicceduParser import *
def main():
    save_path = os.path.join(os.getcwd(), "test3.xlsx")
    MicceduParser().export_to_excel('http://indicators.miccedu.ru/monitoring/2015/', save_path)

if __name__ == "__main__":
    main()