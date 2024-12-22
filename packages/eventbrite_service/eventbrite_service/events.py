import requests
import json
import time
import random
import eventbrite_service.config as config
from bs4 import BeautifulSoup
from loguru import logger
from selenium  import webdriver
from selenium.webdriver.chrome.options import Options


def get_future_event_ids(organizer_url: str) -> list[str]:
    """ Get event ids for future events

    Args:
        organizer_url (str): URL of the organizer's eventbrite page

    Returns:
        list[str]: List of unique event ids
    """

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(organizer_url)
    driver.implicitly_wait(10)

    rendered_html = driver.page_source

    soup = BeautifulSoup(rendered_html, 'html.parser')
    driver.quit()

    parent_divs = soup.find_all('div', attrs={config.parent_div_attr_key: config.parent_div_attr_val})
    event_ids = set()

    for div in parent_divs:
        a_elements = div.find_all('a', href=True, attrs={config.a_tag_attr_key: True})
        for a_element in a_elements:
            event_id = a_element['data-event-id']
            event_ids.add(event_id)

    # Convert the set to a list
    unique_event_ids = list(event_ids)

    return unique_event_ids

def get_event_details(event_id: str) -> dict:
    """Get event details for a given event id

    Args:
        event_id (str): Event id for evenbrite event

    Returns:
        dict: Dictionary containing event details based on eventbrite API response
    """

    url = f"{config.eventbrite_api_base_url}events/{event_id}/"
    headers = {"Authorization": f"Bearer {config.secret_token}"}

    jitter = random.uniform(1,9)
    time.sleep(jitter)

    response = requests.get(url, headers=headers)
    dict_response = json.loads(response.text)

    return dict_response


# Example usage
organizer_url = config.nyc_organizers["dj_john_john"]
event_ids = get_future_event_ids(organizer_url)
print(event_ids)

for event_id in event_ids:
    print(get_event_details(event_id))

