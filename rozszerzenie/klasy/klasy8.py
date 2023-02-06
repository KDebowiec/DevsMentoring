# Rozważ klasę Case, która będzie inicjalizowana wraz z poniższymi danymi:
#
# first_case = {
#     ‘name’: ‘first_case’,
#     ‘created_task’: ‘2021-10-26T19:48:12+00:00’,
#     ‘end_task’: None
# }
#
# second_case = {
#     ‘name’: ‘second_case’,
#     ‘created_task’: ‘2021-09-26T19:48:12+00:00’,
#     ‘end_task’: ‘2021-10-26T19:48:12+00:00’
# }
#
# Klasa Case ma zawierać metodę retrieve_seconds, która zwracać będzie różnicę
# czasową między end_task a created_task podaną w sekundach.
#
# UWAGA
# Wartość None przypisana do klucza end_task oznacza, że task jeszcze trwa.
# Zwróć uwagę na to, iż retrieve_seconds możemy wywoływać wielokrotnie
from datetime import datetime


class Case:
    def __init__(self, name, created_task, end_task):
        self.name = name
        self.created_task = created_task
        self.end_task = end_task
        self.retrieve_seconds()

    def retrieve_seconds(self):
        start_time = datetime.strptime(self.created_task[11:19], "%H:%M:%S")
        start_day = self.created_task[0:10]
        d1 = datetime.strptime(start_day, "%Y-%m-%d")

        if self.end_task:
            end_time = datetime.strptime(self.end_task[11:19], "%H:%M:%S")
            end_day = self.end_task[0:10]
            d2 = datetime.strptime(end_day, "%Y-%m-%d")
        else:
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d/%H:%M:%S")
            end_time = datetime.strptime(date_time[11:19], "%H:%M:%S")
            self.end_task = date_time
            end_day = date_time[0:10]
            d2 = datetime.strptime(end_day, "%Y-%m-%d")

        day_difference = d2 - d1
        day_difference_in_seconds = day_difference * 86400  # 86400 - tyle sekund jest w dobie
        if day_difference == 0:
            difference = end_time - start_time
            print(difference)
            return difference
        else:
            list_of_start = self.created_task[11:19].split(':')
            start_in_seconds = int(list_of_start[0]) * 3600 + int(list_of_start[1]) * 60 + int(list_of_start[2])

            list_of_end = self.end_task[11:19].split(':')
            end_in_seconds = int(list_of_end[0]) * 3600 + int(list_of_end[1]) * 60 + int(list_of_end[2])

            print(day_difference_in_seconds.days - start_in_seconds + end_in_seconds)
            return day_difference_in_seconds.days - start_in_seconds + end_in_seconds


first_case = Case('first_case', '2021-10-26T19:48:12+00:00', None)
second_case = Case('second_case', '2021-09-26T19:48:12+00:00', '2021-10-26T19:48:12+00:00')

