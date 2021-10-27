from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.indeed.com/jobs?q=software%20developer&l=Remote&vjk=9c3ed7a8865a901f").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'slider_container')


for job in jobs:
    job_title = job.find('h2', class_ = 'jobTitle').text
    company_info = job.find('div', class_='company_location')
    company_name = company_info.find('span', class_='companyName').text
    company_location = company_info.find('div', class_='companyLocation').text
    
    jobs_container = job.find('table', class_= 'jobCardShelfContainer')
    job_snippet = jobs_container.find('div', class_='job-snippet')
    description = job_snippet.find('li').text
    last_active = jobs_container.find('span', class_='date').text
    
    print(f'''
    Position: {job_title}
    Company Name: {company_name}
    Location: {company_location}
    Short Description: 
    {description}
    {last_active}
    ''')
    
    print('')
    


