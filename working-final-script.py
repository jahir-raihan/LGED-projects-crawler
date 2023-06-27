from bs4 import BeautifulSoup
import requests
import time


class StoreOldLgedData:

    def __init__(self):
        self.__all_tables = None
        self.__dic = {}

    def execute_data_aggregation(self, data):

        """Main data aggregator method"""

        __html_data = BeautifulSoup(data.text, 'html.parser')
        self.__all_tables = __html_data.find_all('table')

        # Method call to aggregate data from the tables
        self.get_broader_table_data()
        self.get_short_info_data()
        self.get_image_url()

        # Method Call to store data in database
        self.store_data()

    def get_broader_table_data(self):

        """Collects data from Table 1, called as Broader Information Table"""

        broader_table = self.__all_tables[2]
        bt_rows = broader_table.find_all('tr')[1:]

        # Storing all data in a dictionary
        for row in bt_rows:
            columns = row.find_all('td')
            self.__dic[columns[0].get_text().strip()] = columns[2].get_text().strip()

    def get_short_info_data(self):

        """Collects data from Table 2, called as At a Glance or Short Info Table, but the
            Data inside is valid."""

        short_inf_table = self.__all_tables[3]
        st_rows = short_inf_table.find_all('tr')

        # Storing all data in a dictionary
        for row in st_rows:
            columns = row.find_all('td')
            self.__dic[columns[0].get_text().strip()] = columns[1].get_text().strip()

    def get_image_url(self):

        """To get project image url, if image is given for the project"""

        image_table = self.__all_tables[0]
        url = 'https://oldweb.lged.gov.bd/' + image_table.tr.td.img['src']
        self.__dic['image'] = url

    def store_data(self):
        """This part will be handled on the backend"""
        pass

    def peak_data(self):

        """To see if the program is working or not."""

        for k, v in self.__dic.items():
            print(k, ' : ', v)


def get_all_lged_project_data(request):

    """Main driver function to crawl and collect project data from LGED website."""

    for i in range(2, 1040):  # I know it's current projects count.
        try:
            response_data = requests.get(f'https://oldweb.lged.gov.bd/ProjectHome.aspx?projectID={i}')

            store_data = StoreOldLgedData()
            store_data.execute_data_aggregation(response_data)
            store_data.peak_data()
            i += 1

            print()
            print('---------------------------')
            print()
            time.sleep(2)  # Remove this line if your internet speed is fast enough.
        except:
            pass


get_all_lged_project_data('hello')
