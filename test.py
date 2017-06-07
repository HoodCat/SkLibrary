from urllib.request import *
from bs4 import *
from bs4.element import  Tag
from bs4.element import NavigableString
lib_url = 'https://library.skuniv.ac.kr/search/DetailView.ax?sid=&cid=121428'

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
        for con in tag.contents :
            con_str = getContentString(con)
            if con_str is not None :
                print(con_str.__repr__(), con_str.isspace(), sep=':')
                if con_str.isspace() is False :
                    temp_str += con_str + ','

        return temp_str

if __name__ == '__main__':
    soup = BeautifulSoup(urlopen(lib_url), 'html.parser')
    td_list = soup.find_all('td')

    for td in td_list:
        try :
            if td['class'][0] == 'detailHead' :
                print(getContentString(td))
            elif td['class'][0] == 'detailBody':
                print(getContentString(td))

        except KeyError :
            pass