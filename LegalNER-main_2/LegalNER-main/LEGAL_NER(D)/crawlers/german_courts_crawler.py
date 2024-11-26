import bs4
import requests
import pandas as pd
link = 'https://www.verzeichnis-anwalt.de/gerichtsverzeichnis/'
page = requests.get(link, headers={'user-agent': 'Mozilla/5.0'}).text
parsed_doc = bs4.BeautifulSoup(page)


def get_courts_names(tag):
    if tag.parent.name=='li' and len(tag.parent.find_all('ul'))==0:
        return True
    else:
        return False

courts_names_unprocessed = parsed_doc.find('div', {'class':'courts_overview'}).find_all(get_courts_names)

# apply correct encoding to the names of the courts
courts_names = [bytes(i.text.strip(), encoding='raw_unicode_escape').decode('utf-8') for i in courts_names_unprocessed]

pd.DataFrame(courts_names, columns=['Court']).to_csv('german_courts_names.csv')

