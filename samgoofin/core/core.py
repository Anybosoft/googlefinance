from samgoofin.utils.utils import Requests, _clean_list, _clean_more_list, _to_dict
from bs4 import BeautifulSoup
from samgoofin.core.constant import (
    FINANCE_CLASSE,
    NAME_CLASSE,
    PERCENTAGE_CLASSE,
    PRICE_CLASSE,
    VARIACAO_DE_HOJE,
)

class SamGooFin:
    """
    Samuel Google Finance, it's a api
    That can connect you with Google finance
    And you can extract a lot in it
    
    """

    def __init__(self, url):
        self.url = url 

    
    def name(self):
        response = Requests(self.url)

        if response.return_statustcode() == 200:
            soup = BeautifulSoup(response.return_text(), "html.parser")
            
            find_name = soup.find("div", class_=NAME_CLASSE)

        return find_name.text
    

    def price(self):
        response = Requests(self.url)

        if response.return_statustcode() == 200:
            soup = BeautifulSoup(response.return_text(), "html.parser")
            
            find_name = soup.find("div", class_=PRICE_CLASSE)

        return find_name.text
    

    def how_is(self):
        response = Requests(self.url)

        if response.return_statustcode() == 200:
            soup = BeautifulSoup(response.return_text(), "html.parser")
            
            find_name = soup.find("div", class_=PERCENTAGE_CLASSE)

        return find_name.text
    

    def finance_table(self):
        response = Requests(self.url)

        if response.return_statustcode() == 200:
            soup = BeautifulSoup(response.return_text(), "html.parser")
            
            find_name = soup.find("div", class_=FINANCE_CLASSE)

        return find_name.text
    

    

    def today_infos_nm(self, to_dict_=True, cru=False):
        liststr = []
        response = Requests(self.url)

        if response.return_statustcode() == 200:
            soup = BeautifulSoup(response.return_text(), "html.parser")
            
            find_name = soup.find_all("div", class_=VARIACAO_DE_HOJE)

            for each_elem in find_name:
                liststr.append(str(each_elem))

     
            if to_dict_ and cru == False:
                tod = _to_dict(_clean_more_list(_clean_list(liststr)))
                return tod
            
            elif cru:
                return _clean_more_list(_clean_list(liststr))
    


