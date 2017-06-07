from bs4 import *
from urllib.request import *

from bs4 import Tag

list_url = 'https://library.skuniv.ac.kr/search/Search.Result.ax?sid=1&mf=true&f=%28CLASSID%3A%281+OR+2+OR+3%29%29&page=1&pageSize=100&s=S_PYB&st=DESC'

def getSoup(url):
    return BeautifulSoup(urlopen(url), 'html.parser')

def getAList(soup):
    if type(soup) is not BeautifulSoup:
        return None
    return soup.find_all('a')

def getCid(script):
    if type(script) is not Tag:
        return None
    href = script['href']
    start_bracket = href.index('(')
    end_bracket = href.index(')')
    return href[start_bracket+1: end_bracket]

def getCidList(a_list) :
    cid_list = list()
    for a in a_list :
        try:
            if isTitleLink(a):
                cid_list.append(getCid(a))
        except KeyError as e:
            pass
    return cid_list

def isTitleLink(a) :
    return a.string != None and a.parent['class'][0] == 'body'

if __name__ == '__main__':
    a_list = getAList(getSoup(list_url))
    print(getCidList(a_list))
    # for a in a_list:
    #     try:
    #         if isTitleLink(a):
    #             print(getCid(a))
    #     except KeyError as e:
    #         pass
