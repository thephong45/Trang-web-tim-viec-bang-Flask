import requests
import bs4
import sqlite3
import time


link = "http://www.familug.org/"
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE fami (title text, link text, label text)''')
conn.commit()


def crawl_data(lable):
    result = []
    reps = requests.Session()
    url_link = "{}search/label/{}".format(link, lable)
    while True:
        try:
            ses = reps.get(url_link)
            tree = bs4.BeautifulSoup(ses.text, 'lxml')
            result.extend(tree.find_all(attrs={'class':
                                               'post-title entry-title'}))
            next_page = tree.find(attrs={'class':
                                         'blog-pager-older-link'}).get('href')
            url_link = next_page
        except Exception:
            break
    for value in result:
        c.execute('''INSERT INTO fami VALUES (?,?,?)''',
                  (value.text, value.a.get('href'), lable))
        conn.commit()
        time.sleep(3)
    return


def main():
    lables = ['Lastest', 'Python', 'Command', 'sysadmin']
    for lable in lables:
        crawl_data(lable)
    conn.close()


if __name__ == '__main__':
    main()
