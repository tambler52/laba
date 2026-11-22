import requests
from bs4 import BeautifulSoup

url = 'https://ticketpro.by'
response = requests.get(url)
print('статус ответа:', response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
cards = soup.find_all('a', class_='group/eventCard')
print('найдено карточек:', len(cards))

events = {}

for card in cards:
    href = card.get('href')
    if href is None or href in events:
        continue

    card_text = card.text.strip()

    price_value = None
    ot_position = card_text.find('от ')
    if ot_position != -1:
        text_after_ot = card_text[ot_position + 3:].strip()
        number_string = ''
        for character in text_after_ot:
            if character.isdigit():
                number_string = number_string + character
            elif character == ',' or character == '.':
                number_string = number_string + '.'
            else:
                if number_string != '':
                    break

        if number_string != '' and number_string != '.':
            price_value = float(number_string)

    venue_name = 'не указано'
    icon_index = -1
    for index in range(len(card_text)):
        if ord(card_text[index]) > 10000:
            icon_index = index
            extracted_venue = card_text[index + 1:].strip()
            if extracted_venue != '':
                venue_name = extracted_venue
            break

    if icon_index != -1:
        before_venue = card_text[:icon_index].strip()
    else:
        before_venue = card_text

    cut_ot = before_venue.find('от ')
    if cut_ot != -1:
        info_part = before_venue[:cut_ot].strip()
    else:
        info_part = before_venue

    date_time_value = 'не указано'
    title_value = info_part

    colon_pos = info_part.find(':')
    if colon_pos != -1 and colon_pos >= 2 and colon_pos + 2 < len(info_part):
        time_start = colon_pos - 2
        time_end = colon_pos + 3
        time_str = info_part[time_start:time_end]

        months = [
            'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
            'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
        ]
        date_start = -1
        for month_name in months:
            m_pos = info_part.lower().find(month_name)
            if m_pos != -1:
                d_pos = m_pos - 1
                while d_pos >= 0 and info_part[d_pos] == ' ':
                    d_pos = d_pos - 1
                while d_pos >= 0 and info_part[d_pos].isdigit():
                    d_pos = d_pos - 1
                date_start = d_pos + 1
                break

        if date_start != -1:
            title_candidate = info_part[:date_start].strip()
            if title_candidate != '':
                title_value = title_candidate
            date_time_value = info_part[date_start:time_end].strip()
        else:
            date_time_value = time_str.strip()

    if href.startswith('http'):
        event_url = href
    else:
        event_url = url + href

    age_value = 'не указано'
    event_response = requests.get(event_url)
    if event_response.status_code == 200:
        event_soup = BeautifulSoup(event_response.text, 'html.parser')
        age_element = event_soup.find('span', class_='text-violet-1')
        if age_element is not None:
            age_text = age_element.text.strip()
            if age_text != '':
                age_value = age_text

    events[href] = {
        'title': title_value,
        'date_time': date_time_value,
        'venue': venue_name,
        'price': price_value,
        'age': age_value,
        'link': event_url
    }

valid_prices = []
cheapest_event = None
most_expensive_event = None

for href, event_info in events.items():
    current_price = event_info['price']
    if current_price is not None:
        valid_prices.append(current_price)

        if cheapest_event is None or current_price < cheapest_event['price']:
            cheapest_event = event_info

        if most_expensive_event is None or current_price > most_expensive_event['price']:
            most_expensive_event = event_info

venue_counts = {}
for href, event_info in events.items():
    venue = event_info['venue']
    if venue != 'не указано':
        if venue in venue_counts:
            venue_counts[venue] = venue_counts[venue] + 1
        else:
            venue_counts[venue] = 1

busiest_venue = 'не определена'
busiest_venue_count = 0
for venue_name, count in venue_counts.items():
    if count > busiest_venue_count:
        busiest_venue_count = count
        busiest_venue = venue_name

if len(valid_prices) > 0:
    min_price = min(valid_prices)
    max_price = max(valid_prices)
    average_price = round(sum(valid_prices) / len(valid_prices), 2)
else:
    min_price = None
    max_price = None
    average_price = None

print('\n--- сводная статистика ---')
print(f'всего уникальных событий: {len(events)}')
print(f'минимальная стоимость билета: {min_price}')
print(f'максимальная стоимость билета: {max_price}')
print(f'средняя стоимость билета: {average_price}')
print(f'самая загруженная площадка: {busiest_venue} (мероприятий: {busiest_venue_count})')

if most_expensive_event is not None:
    print(
        f"самый дорогой билет: {most_expensive_event['price']} — "
        f"{most_expensive_event['title']} ({most_expensive_event['date_time']}, {most_expensive_event['venue']})"
    )

if cheapest_event is not None:
    print(
        f"самый дешёвый билет: {cheapest_event['price']} — "
        f"{cheapest_event['title']} ({cheapest_event['date_time']}, {cheapest_event['venue']})"
    )

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write('=== список событий ===\n')
    counter = 1
    for href, event_info in events.items():
        file.write(f"{counter}. {event_info['title']}\n")
        file.write(f"   дата и время: {event_info['date_time']}\n")
        file.write(f"   место проведения: {event_info['venue']}\n")
        file.write(f"   стоимость билета: {event_info['price']}\n")
        file.write(f"   возрастное ограничение: {event_info['age']}\n")
        counter = counter + 1

    file.write('\n=== статистика ===\n')
    file.write(f'всего уникальных событий: {len(events)}\n')
    file.write(f'минимальная стоимость билета: {min_price}\n')
    file.write(f'максимальная стоимость билета: {max_price}\n')
    file.write(f'средняя стоимость билета: {average_price}\n')
    file.write(f'самая загруженная площадка: {busiest_venue} (мероприятий: {busiest_venue_count})\n')

    if most_expensive_event is not None:
        file.write(
            f"самое дорогое мероприятие: {most_expensive_event['title']} "
            f"(цена: {most_expensive_event['price']}, дата/время: {most_expensive_event['date_time']}, "
            f"площадка: {most_expensive_event['venue']}, возраст: {most_expensive_event['age']})\n"
        )

    if cheapest_event is not None:
        file.write(
            f"самое дешёвое мероприятие: {cheapest_event['title']} "
            f"(цена: {cheapest_event['price']}, дата/время: {cheapest_event['date_time']}, "
            f"площадка: {cheapest_event['venue']}, возраст: {cheapest_event['age']})\n"
        )

print('\nданные сохранены в result.txt')