from io import StringIO
import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
import time

def random_user_agent(user_agent_list:str)->str:
    """
    Select a random user agent from the list of user agents
    """
    with open (user_agent_list) as f:
        lines = f.readlines()
        return random.choice(lines).strip()
    

def random_delay():
    """
    Create a random delay between 1 and 5 seconds, to simulate a human behaviour
    """
    delay_time = random.randint(1, 5)
    time.sleep(delay_time)
    


def ImportHTML(url:str, query_type:str, index:int) ->pd.DataFrame:
    """
    Import HTML table or list from a given URL and return it as a pandas DataFrame
    """
    
    headers = {'User-Agent': random_user_agent("config/usr_agnts.txt")}
    
    # fetch from url
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    html_content = response.text

    # Parse HTML with bs4
    soup = BeautifulSoup(html_content, 'html.parser')

    if query_type == "table":
        tables = soup.find_all('table')
        if index >= len(tables):
            raise IndexError(f"No table found at index {index}.")
        table = tables[index]
        df = pd.read_html( StringIO( str(table)) )[0]

    elif query_type == "list":
        lists = soup.find_all('ul')
        if index >= len(list):
            raise IndexError(f"No list found at index {index}.")
        
        list_items = lists[index].find_all('li')

        data = {'Item': [li.get_text(strip=True) for li in list_items]}
        df = pd.DataFrame(data)


    return df

