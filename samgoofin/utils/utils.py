import requests as re




class Requests:
    def __init__(self, url):
        self.url = url
        self.get_url = re.get(self.url)



    def return_text(self):
        return self.get_url.text

    def return_statustcode(self):
        return self.get_url.status_code
    


# Clean the list to take just first 8 elem
def _clean_list(list):
    new_list = []
    length = len('<div class="P6K39c">')
    for each_text in list:
        new_list.append(each_text[length:])

    return new_list[:8]



def _clean_more_list(list):
    new_list = []

    for each_elem in list:
        new_list.append(each_elem.replace("\xa0", "").replace("</div>", ""))
    return new_list



def _to_dict(list):
    # Último fechamento
    # Variações de hoje
    # Variações do ano
    # Capitalização de mercado
    # Volume médio
    # Índice P/L
    # Rend. de dividendos
    # Bolsa principal

    infos_dict = {}


    infos_dict["Ultimo_fechamento"] = list[0]
    infos_dict["Variacao_de_hoje"] = list[1]
    infos_dict["Variacao_do_ano"] = list[2]
    #infos_dict["Capitalization"] = list[3]
    #infos_dict["Volume_medio"] = list[4]
    #infos_dict["Indice_PL"] = list[5]
    #infos_dict["Rend_dividendos"] = list[6]
    #infos_dict["Bolsa_principal"] = list[7]

    return infos_dict