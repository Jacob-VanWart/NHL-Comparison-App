import requests
from bs4 import BeautifulSoup
from PlayerAssign import PlayerAssign

def NHL_Comparison_Offline(Player1,Player2):
    name = []
    last1=""
    last2=""
    wiki = "http://www.cbssports.com/nhl/stats/playersort/nhl/year-2016-season-regularseason-category-points?print_rows=9999"
    page = requests.get(wiki)

    soup = BeautifulSoup(page.text, "html.parser")
    NhlTable = soup.find("table", "data")

    NhlTable_trs = NhlTable.find_all('tr')[2:-1]

    for n in range(len(NhlTable_trs)):
        player = NhlTable_trs[n].find_all('td')
        name.append(player[0])
        name[n] = PlayerAssign(player[0], player[1], player[2], player[3], player[4], player[5], player[6], player[7],
                               player[8], player[9], player[10], player[11], player[12], player[13], player[14], player[15],
                               player[16], player[17], player[18], )


    for i in range(len(name)):
        if Player1.lower() == name[i].name.lower() or Player1.lower() == name[i].name.split()[1].lower():
            num1=i
        if Player2.lower() == name[i].name.lower() or Player2.lower() == name[i].name.split()[1].lower():
            num2=i

    return name[num1],name[num2]


