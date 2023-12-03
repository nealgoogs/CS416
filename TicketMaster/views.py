from django.shortcuts import render
import requests
from .forms import SearchForm
from datetime import datetime

def search_view(request):
    form = SearchForm(request.GET or None)
    events = []
    results_found = False
    error_message = None
    search_performed = False

    if request.method == 'GET' and form.is_valid():
        search_performed = True
        classification = form.cleaned_data['classification']
        city = form.cleaned_data['city']


        response = get_ticketmaster_events(classification, city)

        if response.status_code == 200:
            data = response.json()
            events = process_events(data.get('_embedded', {}).get('events', []))
            results_found = bool(events)
        else:
            error_message = 'Error fetching data from Ticketmaster'

    context = {
        'form': form,
        'events': events,
        'results_found': results_found,
        'error': error_message,
        'search_performed': search_performed,
    }
    return render(request, 'ticketmaster.html', context)


def get_ticketmaster_events(classification, city):
    api_key = '6z2WdN1myGH704rSkrUzrWCB0N0kN0Va'
    api_url = f'https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&classificationName={classification}&city={city}'

    response = requests.get(api_url)
    return response


def process_events(events):
    processed_events = []
    for event in events:
        venues = event.get('_embedded', {}).get('venues', [{}])
        venue = venues[0] if venues else {}
        venue_name = venue.get('name', '')
        venue_address = venue.get('address', {}).get('line1', '')

        start_date_str = event.get('dates', {}).get('start', {}).get('localDate')
        start_time_str = event.get('dates', {}).get('start', {}).get('localTime')

        # Convert date to "MM-DD-YYYY" format
        start_date_formatted = None
        if start_date_str:
            start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
            start_date_formatted = start_date_obj.strftime('%m-%d-%Y')

        # Convert time to 12-hour format
        start_time_12hr = None
        if start_time_str:
            start_time_obj = datetime.strptime(start_time_str, '%H:%M:%S')
            start_time_12hr = start_time_obj.strftime('%I:%M %p')

        if start_date_str and start_time_str:
            start_datetime_str = f"{start_date_str} {start_time_str}"
            start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M:%S')
        else:
            start_datetime = None

        processed_event = {
            'name': event.get('name'),
            'url': event.get('url'),
            'images': get_highest_quality_image(event.get('images', [])),
            'start_date': start_date_formatted,
            'start_time': start_time_12hr,
            'start_datetime': start_datetime,
            'venue_name': venue_name,
            'venue_address': venue_address,
        }
        processed_events.append(processed_event)

    processed_events.sort(key=lambda x: x['start_datetime'] if x['start_datetime'] else datetime.max)
    return processed_events


def get_highest_quality_image(images):
    if not images:
        return None
    highest_quality_image = max(images, key=lambda x: x.get('width', 0))
    return highest_quality_image.get('url')


