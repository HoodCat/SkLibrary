import SearchPageParser
import DetailPageParser
import json

if __name__ == '__main__':
    book_file = open('book_data.json', 'w')

    for cid in SearchPageParser.getCidList(
            SearchPageParser.getAList(
                SearchPageParser.getSoup(
                    SearchPageParser.list_url))):
        book_data = dict(zip(DetailPageParser
            .getHeadList(DetailPageParser.
            getTDList(DetailPageParser.getDetailPageSoup(cid))),
            DetailPageParser.getBodyList(DetailPageParser.getTDList(
                DetailPageParser.getDetailPageSoup(cid)))))

        try:
            if '서명 / 저자' in book_data.keys():
                if '/' in book_data['서명 / 저자']:
                    book_data['서명'] = book_data['서명 / 저자'].split('/')[0].strip()
                    book_data['저자'] = book_data['서명 / 저자'].split('/')[1].strip()
                    book_data.pop('서명 / 저자')
                else:
                    book_data['서명'] = book_data.pop('서명 / 저자')
        except KeyError:
            pass
        json.dump(book_data, book_file)   

    book_file.close()