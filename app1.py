import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.myfitness.lv/en/club/domina/class-schedule/')

soup = BeautifulSoup(r.text, 'html.parser')

timesRow = soup.find_all('td', {'class': 'time'})
daysRow = soup.find_all('table', {'class': 'timetable-table'})
results = []

for dayRow in daysRow:
    day = dayRow.get('td', {'class': 'day'})
    # Once formatted, the data are then appended to the results list
    results.append({
        'day': day,

    })
print(dayRow)