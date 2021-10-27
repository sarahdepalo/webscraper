from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.indeed.com/jobs?q=software%20developer&l=Remote&vjk=9c3ed7a8865a901f").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('a', class_ = 'tapItem')


for job in jobs:
    jobs_container = job.find('table', class_= 'jobCardShelfContainer')
    last_active = jobs_container.find('span', class_='date').text
    if not '30+' in last_active: #removes all jobs posted 30+ day ago
        job_snippet = jobs_container.find('div', class_='job-snippet')
        description = job_snippet.find('li').text
        
        job_title = job.find('h2', class_ = 'jobTitle').text
        company_info = job.find('div', class_='company_location')
        company_name = company_info.find('span', class_='companyName').text
        company_location = company_info.find('div', class_='companyLocation').text

        more_info = job['href']
        
        print(f'Position: {job_title.strip()}')
        print(f'Company: {company_name.strip()}')
        print(f'Location: {company_location.strip()}')
        print(f'Short Description: {description.strip()}')
        print(f'More Info: https://www.indeed.com{more_info}')
        print(f'{last_active.strip()}')
        
        print('')
    


