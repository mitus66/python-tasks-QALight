'''
Завдання:
Уявіть, що ви працюєте з великим лог-файлом веб-сервера. Ваше завдання — розробити генератор Python, який читає файл рядково і фільтрує логи, залишаючи лише записи, які відносяться до певної дати. Записи лога мають бути представлені у форматі, де кожен рядок містить дату, час, IP-адресу, метод запиту (GET, POST тощо), URL та статус відповіді.

Вимоги:
Функція генератора повинна брати шлях до файлу та дату, за якою потрібно фільтрувати записи.
Генератор повинен обробляти файл рядково, що дозволяє працювати з файлами, розмір яких перевищує доступну оперативну пам'ять.
Ви повинні використовувати мінімальну кількість пам'яті для виконання завдання.

Приклад даних лога:
2023-01-01 12:00:00 192.168.1.1 GET /index.html 200
2023-01-01 12:05:00 192.168.1.2 POST /submit-form 404
2023-01-02 13:00:00 192.168.1.3 GET /about.html 200

Приклад використання генератора:
logfile_path = 'path_to_log_file.log'
filter_date = '2023-01-01'
filtered_logs = log_filter(logfile_path, filter_date)
for line in filtered_logs:
     print(line)

Очікуваний висновок:
2023-01-01 12:00:00 192.168.1.1 GET /index.html 200
2023-01-01 12:05:00 192.168.1.2 POST /submit-form 404
'''

import re


def log_filter(logfile_path, filter_date):
    date_regex = re.compile(rf"^{filter_date} \d{{2}}:\d{{2}}:\d{{2}}")

    with open(logfile_path, 'r') as logfile:
        for line in logfile:
            if date_regex.match(line):
                yield line


# Приклад використання
logfile_path = 'path_to_log_file.log'
filter_date = '2023-01-01'
filtered_logs = log_filter(logfile_path, filter_date)

for line in filtered_logs:
    print(line)

## Зразкове рішення, дякую)