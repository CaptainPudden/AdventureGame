import requests
from pprint import pprint
from bs4 import BeautifulSoup
from savefile import save_dict

"""
pip install requests 
pip install bs4
"""

TEST = 'https://www.dandwiki.com/wiki/5e_SRD:Races'
HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
}



def get_page(url):
  """ returns a bs4 object from url """
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  return soup
  
def get_2nd_table(content):
  """ returns a list of tuples from the 2nd table """
  stuff = {}
  table = content.find_all('table')[1]
  rows = table.find_all('tr')
  for row in rows:
    children = row.findChildren()
    try:
      stuff.update({children[0].text.strip(): children[2].text.strip()})
    except IndexError:
      pass
  return stuff
  
def save_it(url, filename):
  """ saves """
  content = get_page(url)
  table = get_2nd_table(content)
  save_dict(filename, table)
  
if __name__ == '__main__':
  save_it('https://www.dandwiki.com/wiki/5e_SRD:Races', 'races.json')
  save_it('https://www.dandwiki.com/wiki/5e_SRD:Classes', 'classes.json')
  
  