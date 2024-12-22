1. Configure organizer eventbrite urls to parse
2. Collect events as list of urls or id's (parse event ids from urls)
   - Search for div with class `eds-show-up-mn organizer-profile__event-renderer__grid`
   - Take nested <a> elements and copy href url
   - Parse href url for eid, between `tickets-` and `?aff`
Iterate over multiple to events to:
3. Get event object of eid with EventBrite API: `https://www.eventbriteapi.com/v3/events/<eid>`
   - Collect `venue_id`
   - collect `start_time and end time`
   - collect `summary`
   - collect `name`
4. Get venue object
    - Collect `venue` metadata

