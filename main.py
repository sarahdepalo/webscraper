from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.linkedin.com/jobs/').text
print(html_text)