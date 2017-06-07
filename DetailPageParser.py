from urllib.request import *
from bs4 import *
from bs4.element import  Tag
from bs4.element import NavigableString
from SearchPageParser import *
import re
detail_url = 'https://library.skuniv.ac.kr/search/DetailView.ax?sid=&cid='

def getDetailPageSoup(cid) :
    return BeautifulSoup(urlopen(detail_url+cid), 'html.parser')

def getTDList(soup) :
    return soup.find_all('td')

def getContentString(tag) :
    # 태그 확인 여부
    if type(tag) is not Tag :
        if type(tag) is NavigableString:
            return str(tag).strip()
        return None

    # 태그 값 유무 확인 및 값 추출
    if tag.string is not None :
        return str(tag.string).strip()

    # 하위 태그 체크 및 값 추출
    if len(tag.contents) > 1 :
        temp_str = str()
        for idx, con in enumerate(tag.contents) :
            con_str = getContentString(con)
            if con_str is not None :
                if con_str != "":
                    temp_str += ', ' + con_str.replace('\n', '').strip()

        return temp_str.strip(',').strip()

def getHeadList(td_list):
    head_list = list()
    for td in td_list:
        try:
            if td['class'][0] == 'detailHead':
                head_str = getContentString(td)
                head_str = head_str.replace(':','').strip()
                head_list.append(head_str)
        except KeyError:
            pass
    return head_list

def getBodyList(td_list):
    body_list = list()
    for td in td_list:
        try:
            if td['class'][0] == 'detailBody':
                body_str = getContentString(td)
                body_str = re.sub(r'\s+', ' ', body_str)
                body_list.append(body_str)
        except KeyError:
            pass
    return body_list

def printTDList(td_list) :
    print(getHeadList(td_list))
    print(getBodyList(td_list))


if __name__ == '__main__':
    a_list = getAList(getSoup(list_url))
    for cid in getCidList(a_list):
        td_list = getTDList(getDetailPageSoup(cid))
        printTDList(td_list)
        print('------------------------------')