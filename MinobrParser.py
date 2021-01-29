from utils import *
class MinobrParser:
    def __init__(self):
        self.url_origin = "https://minobrnauki.gov.ru"
        self._url_with_links_on_archives = "https://minobrnauki.gov.ru/action/stat/highed/";

    def download_vpo1(self, vpo1_path):
        hrefs = get_hrefs(self._url_with_links_on_archives)
        file_paths_vpo1 = extract_data_from_collection(hrefs, ".*VPO.1.*(rar|zip)")
        download_files(self.url_origin, file_paths_vpo1, vpo1_path)

    def download_vpo2(self, vpo2_path):
        hrefs = get_hrefs(self._url_with_links_on_archives)
        file_paths_vpo2 = extract_data_from_collection(hrefs, ".*VPO.2.*(rar|zip)")
        download_files(self.url_origin, file_paths_vpo2, vpo2_path)

    def download_both(self, path):
        hrefs = get_hrefs(self._url_with_links_on_archives)
        file_paths_vpo1 = extract_data_from_collection(hrefs, ".*VPO.1.*(rar|zip)")
        file_paths_vpo2 = extract_data_from_collection(hrefs, ".*VPO.2.*(rar|zip)")
        download_files(self.url_origin, file_paths_vpo1, path)
        download_files(self.url_origin, file_paths_vpo2, path)

    def download_both_in_parallel(self, path):
        hrefs = get_hrefs(self._url_with_links_on_archives)
        file_paths_vpo1 = extract_data_from_collection(hrefs, ".*VPO.1.*(rar|zip)")
        file_paths_vpo2 = extract_data_from_collection(hrefs, ".*VPO.2.*(rar|zip)")
        download_files_in_parallel(self.url_origin, file_paths_vpo1, path)
        download_files_in_parallel(self.url_origin, file_paths_vpo2, path)

    def download_both_async(self, path):
        hrefs = get_hrefs(self._url_with_links_on_archives)
        file_paths_vpo1 = extract_data_from_collection(hrefs, ".*VPO.1.*(rar|zip)")
        file_paths_vpo2 = extract_data_from_collection(hrefs, ".*VPO.2.*(rar|zip)")
        download_files_async(self.url_origin, file_paths_vpo1, path)
        download_files_async(self.url_origin, file_paths_vpo2, path)