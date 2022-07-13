import xml.etree.ElementTree as ET


def search_book_by_author_name(name_author):
    tree = ET.parse('C:/Users/wwwba/PycharmProjects/selenium_test/library.xml')
    root = tree.getroot()
    for child in root:
        for author in child:
            if not f'{name_author}' in author.text:
                text = "None"
            else:
                text = author.text
                print(f'{child.tag}{child.attrib} => Author: {text}')


def search_book_by_price(price_book):
    tree = ET.parse('C:/Users/wwwba/PycharmProjects/selenium_test/library.xml')
    root = tree.getroot()
    for book in root:
        for price in book:
            if not f'{price_book}' in price.text:
                text = None
            else:
                text = price.text
                print(f'{book.tag}{book.attrib} => Price: {text}')


def search_book_by_title(title_name: str):
    tree = ET.parse('C:/Users/wwwba/PycharmProjects/selenium_test/library.xml')
    root = tree.getroot()
    for book in root:
        for title in book:
            if not f'{title_name}' in title.text:
                text = None
            else:
                text = title.text
                print(f'{book.tag}{book.attrib} => Title: {text}')


def search_book_by_description(description_name: str):
    tree = ET.parse('C:/Users/wwwba/PycharmProjects/selenium_test/library.xml')
    root = tree.getroot()
    for book in root:
        for description in book:
            if not f'{description_name}' in description.text:
                text = None
            else:
                text = description.text
                print(f'{book.tag}{book.attrib} => Description: {text}')


if __name__ == "__main__":
    search_book_by_author_name('Matthew')
    search_book_by_price(4)
    search_book_by_title('XML De')
    search_book_by_description('A former architect')
