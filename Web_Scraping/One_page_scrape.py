from bs4 import BeautifulSoup
import requests

url = "https://cs619finalproject.com/urdu-health-recommender-system-uhrs-test-phase-srs-design-phase-and-source-code-final-deliverable/"
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text, 'lxml')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
