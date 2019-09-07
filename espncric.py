import requests
import bs4
import io
import re

data = requests.get("http://www.espncricinfo.com/ci/content/player/index.html")
mainurl = "http://www.espncricinfo.com/ci/content/player/caps.html?country="
data = bs4.BeautifulSoup(data.text,"lxml")
teams = data.select(".ciPlayersHomeCtryList")
for i in teams:
    test = i.find_all("a")
    #print(test)
for i in range(len(test)):
    url = test[i].get("href")
    url = re.split("=",url)
    url1 = mainurl + url[1] + ";class=1"
    teamname = test[i].text
    teamdata = requests.get(url1)
    teamdata = bs4.BeautifulSoup(teamdata.text,"lxml")
    playerdata = teamdata.select(".ciPlayerbycapstable")
    with io.open(teamname + ".csv" , "w" , encoding="utf8") as f1:
                f1.write("TEAMNAME,NUMBER,NAME,DEBUT_DATE \n")
                f1.close()
    for k in playerdata:
        playerstats = k.find_all("li",class_="sep")
        for m in playerstats:
            number = m.find_all("li",class_="ciPlayerserialno")
            name = m.find_all("li",class_= "ciPlayername")
            debut_date = m.find_all("li",class_= "ciPlayerplayed")
            dataline = teamname + ","  + number[0].text + name[0].text + debut_date[0].text
            with io.open(teamname + ".csv" , "a" , encoding="utf8") as f1:
                f1.write(dataline+"\n")
                f1.close()
print("done")
