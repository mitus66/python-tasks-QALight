'''
Завдання 1: Клас Event
Розробіть клас Event, який представлятиме окрему подію з вашого JSON-файлу. Клас повинен включати атрибути для зберігання даних про подію (наприклад, serial, name, event_type, time_start, time_stop, venue_serial, description, website_url, speakers, categories) і методи для роботи з цими даними.

Завдання 2: Клас Venue
Створіть клас Venue для представлення місця проведення події. Цей клас повинен включати атрибути, такі як serial, name та category. Додайте методи, які дозволять отримувати детальну інформацію про місце проведення.

Завдання 3: Клас Speaker
Визначте клас Speaker для зберігання інформації про доповідачів. Клас повинен містити атрибути для serial, name, photo, url, position, affiliation, twitter, bio та методи для доступу до цієї інформації.

Будівля 4: Агрегація даних
Реалізуйте клас Conference, який агрегуватиме події (Event), місця проведення (Venue) та доповідачів (Speaker). Цей клас повинен дозволити додавати та видаляти події, місця проведення та доповідачів, а також надавати методи для фільтрації подій за різними параметрами, наприклад, за датою, категорією чи доповідачем.

Завдання 5: Пошук та сортування подій
Додайте до класу Conference методи пошуку подій за ключовими словами в назві або описі та сортування подій за часом початку. Ці методи повинні допомогти користувачеві знаходити події, які його цікавлять, та переглядати їх у хронологічному порядку.

Завдання 6: Інтерфейс користувача
Розробіть простий текстовий інтерфейс користувача (або CLI), який використовує клас Conference для надання користувачеві інформації про конференції. Інтерфейс повинен дозволяти користувачеві вибирати події для перегляду детальної інформації, фільтрувати події за датою або категорією та шукати події за ключовими словами.

py_fest.json py_fest.json4 квітня 2024, 11:32 AM

'''

# TODO: fix bugs
import json
import datetime

with open("py_fest1.json", "r") as f:
    # Read the contents of the file
    data = f.read()

json_data = json.loads(data)

# Access data based on the structure of your JSON file
if isinstance(json_data, dict):
    name = json_data["name"]
    age = json_data["age"]
    # Access other key-value pairs as needed


class Event:
    def __init__(self, data):
        self.serial = data["serial"]
        self.name = data["name"]
        self.event_type = data["event_type"]
        self.time_start = datetime.datetime.strptime(data["time_start"], "%Y-%m-%d %H:%M:%S")
        self.time_stop = datetime.datetime.strptime(data["time_stop"], "%Y-%m-%d %H:%M:%S")
        self.venue_serial = data["venue_serial"]
        self.description = data["description"]
        self.website_url = data["website_url"]
        self.speakers = data["speakers"]
        self.categories = data["categories"]

    def get_speaker_names(self):
        speaker_names = []
        for speaker_id in self.speakers:
            speaker_name = get_speaker_name(speaker_id)  # Function to get speaker name from speaker_id
            speaker_names.append(speaker_name)
        return speaker_names

    def get_speaker_details(self, speaker_id):
        speaker_details = get_speaker_details(speaker_id)  # Function to get speaker details from speaker_id
        return speaker_details

    def get_venue_details(self):
        venue_details = get_venue_details(self.venue_serial)  # Function to get venue details from venue_serial
        return venue_details

# Функції `get_speaker_name`, `get_speaker_details` та `get_venue_details`
#  будуть реалізовані  в наступних завданнях
#  (з урахуванням класів `Speaker` та `Venue`).


class Venue:
    def __init__(self, data):
        self.serial = data["serial"]
        self.name = data["name"]
        self.category = data["category"]

    def get_description(self):
        # Функція для отримання опису місця проведення (з JSON-файлу або API)
        #  Ця функція буде реалізована пізніше,
        #  оскільки опис місця проведення не представлений
        #  безпосередньо в наданому JSON-файлі.
        #  Вона може отримувати опис з іншого джерела,
        #  наприклад, з JSON-об'єкта місця проведення
        #  або за допомогою API.
        return "Опис місця проведення буде доступним згодом."


class Speaker:
    def __init__(self, data):
        self.serial = data["serial"]
        self.name = data["name"]
        self.photo = data["photo"]
        self.url = data["url"]
        self.position = data["position"]
        self.affiliation = data["affiliation"]
        self.twitter = data["twitter"]
        self.bio = data["bio"]

    def get_social_media_links(self):
        social_media_links = []
        if self.twitter:
            twitter_link = f"https://twitter.com/{self.twitter}"
            social_media_links.append(twitter_link)
        # Додати посилання на інші соціальні мережі (за потребою)
        return social_media_links


class Conference:
    def __init__(self):
        self.events = []
        self.venues = []
        self.speakers = []

    def add_event(self, event):
        if isinstance(event, Event):
            self.events.append(event)
        else:
            raise TypeError("Event must be an object of type Event")

    def remove_event(self, serial):
        for event in self.events:
            if event.serial == serial:
                self.events.remove(event)
                return
        raise ValueError(f"Event with serial {serial} not found")

    def add_venue(self, venue):
        if isinstance(venue, Venue):
            self.venues.append(venue)
        else:
            raise TypeError("Venue must be an object of type Venue")

    def remove_venue(self, serial):
        for venue in self.venues:
            if venue.serial == serial:
                self.venues.remove(venue)
                return
        raise ValueError(f"Venue with serial {serial} not found")

    def add_speaker(self, speaker):
        if isinstance(speaker, Speaker):
            self.speakers.append(speaker)
        else:
            raise TypeError("Speaker must be an object of type Speaker")

    def remove_speaker(self, serial):
        for speaker in self.speakers:
            if speaker.serial == serial:
                self.speakers.remove(speaker)
                return
        raise ValueError(f"Speaker with serial {serial} not found")

    def get_events_by_date(self, date):
        if isinstance(date, datetime.date):
            events_on_date = []
            for event in self.events:
                if event.time_start.date() == date:
                    events_on_date.append(event)
            return events_on_date
        else:
            raise TypeError("Date must be an object of type datetime.date")

    def get_events_by_category(self, category):
        if isinstance(category, str):
            events_in_category = []
            for event in self.events:
                if category in event.categories:
                    events_in_category.append(event)
            return events_in_category
        else:
            raise TypeError("Category must be a string")

    def search_events(self, keyword):
        if isinstance(keyword, str):
            matching_events = []
            for event in self.events:
                if keyword.lower() in event.name.lower() or keyword.lower() in event.description.lower():
                    matching_events.append(event)
            return matching_events
        else:
            raise TypeError("Keyword must be a string")

    def sort_events_by_start_time(self):
        self.events.sort(key=lambda event: event.time_start)


def main():
    # Створення екземпляра класу Conference
    conference = Conference()

    # Завантаження даних з JSON-файлів (припустимо, що JSON-файли доступні)
    load_events_from_json(conference)
    load_venues_from_json(conference)
    load_speakers_from_json(conference)

    # Цикл головного меню
    while True:
        print("\n**Меню конференції**")
        print("1. Переглянути список подій")
        print("2. Переглянути детальну інформацію про подію")
        print("3. Фільтрувати події за датою")
        print("4. Фільтрувати події за категорією")
        print("5. Шукати події")
        print("6. Вийти")

        choice = input("Введіть свій вибір: ")

        if choice == "1":
            show_events(conference)
        elif choice == "2":
            view_event_details(conference)
        elif choice == "3":
            filter_events_by_date(conference)
        elif choice == "4":
            filter_events_by_category(conference)
        elif choice == "5":
            search_events(conference)
        elif choice == "6":
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


def show_events(conference):
    # Виведення списку подій
    if not conference.events:
        print("Немає запланованих подій.")
        return

    print("\n**Список подій**")
    for index, event in enumerate(conference.events):
        print(f"{index + 1}. {event.name} ({event.time_start.strftime('%d.%m.%Y %H:%M')})")


def view_event_details(conference):
    # Перегляд детальної інформації про подію
    event_index = get_event_index_from_user(conference)
    if event_index is None:
        return

    event = conference.events[event_index]
    print("\n**Детальна інформація про подію**")
    print(f"Назва: {event.name}")
    print(f"Дата та час: {event.time_start.strftime('%d.%m.%Y %H:%M')} - {event.time_stop.strftime('%H:%M')}")
    print(f"Місце проведення: {event.get_venue_details().name}")
    print(f"Опис: {event.description}")
    print(f"Доповідачі: {', '.join([speaker.name for speaker in event.get_speaker_names()])}")
    print(f"Веб-сайт: {event.website_url}")


def filter_events_by_date(conference):
    # Фільтрація подій за датою
    try:
        date = datetime.datetime.strptime(input("Введіть дату (YYYY-MM-DD): "), "%Y-%m-%d").date()
    except ValueError:
        print("Неправильний формат дати.")
        return

    filtered_events = conference.get_events_by_date(date)
    if not filtered_events:
        print(f"На {date.strftime('%d.%m.%Y')} подій не знайдено.")
    else:
        print(f"\n**Події на {date.strftime('%d.%m.%Y')}:")
        for event in filtered_events:
            print(f"- {event.name}")


def filter_events_by_category(conference):
    # Фільтрація подій за категорією
    category = input("Введіть категорію: ")

    filtered_events = conference.get_events_by_category(category)
    if not filtered_events:
        print(f"Подій у категорії '{category}' не знайдено.")
    else:
        print(f"\n**Події в категорії '{category}':")
        for event in filtered_events:
            print(f"- {event.name}")


def search_events(conference):
    # ... (existing code)
    keyword = input("Введіть ключове слово: ")

    matching_events = conference.search_events(keyword)  # Call search method

    if not matching_events:
        print(f"Подій за ключовим словом '{keyword}' не знайдено.")
    else:
        print(f"\n**Результати пошуку за '{keyword}':")
        for event in matching_events:
            print(f"- {event.name}")

## Мені дуже сподобалась ідея подавати data на інпут, так (майже?) ніхто крім вас не зробив. Дякую. усміхаюсь

