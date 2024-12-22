from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("EVENTBRITE_API_KEY")
secret_token = os.getenv("EVENTBRITE_PRIVATE_TOKEN")

parent_div_attr_key = "data-testid"
parent_div_attr_val = "organizer-profile__future-events"
a_tag_attr_key = "data-event-id"
eventbrite_api_base_url = "https://www.eventbriteapi.com/v3/"

nyc_organizers = {
    "bachatamania": "https://www.eventbrite.com/o/bachatamania-97398257463",
    "empire_mambo": "https://www.eventbrite.com/o/empire-dance-studio-nyc-90490307953",
    "dj_john_john": "https://www.eventbrite.com/o/dj-john-john-12626967351"
}

reoccurring_events = {
    "taj_mondays": "https://www.eventbrite.com/e/latin-mondays-at-taj-lounge-fall-specials-2024-tickets-472995290647",
    "solas_thursdays": "https://www.eventbrite.com/e/passion-thursdays-at-solas-bar-east-village-tickets-976971376687"
}

taj_event_example = {
    "logo_id": "698243869",
    "organizer_id": "7821988305",
    "venue_id": "126117629",
    "category_id": "110",
    "subcategory_id": "10999",
    "organization_id": "131815173167",
}
"226274179"
"126117629"