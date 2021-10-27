from bs4 import BeautifulSoup
import requests
import time

print('What job do you want to search for?')
job_title = input('>')
print('What location? Enter a city, zipcode, or type remote for remote opportunities.')
location = input('>')

def find_jobs():
    html_text = requests.get(f"https://www.indeed.com/jobs?q={job_title}&l={location}&vjk=9c3ed7a8865a901f").text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('a', class_ = 'tapItem')

    for index, job in enumerate(jobs): 
        jobs_container = job.find('table', class_= 'jobCardShelfContainer')
        last_active = jobs_container.find('span', class_='date').text
        if not '30+' in last_active: #removes all jobs posted 30+ day ago
            job_snippet = jobs_container.find('div', class_='job-snippet')
            description = job_snippet.find('li').text
            
            position = job.find('h2', class_ = 'jobTitle').text
            company_info = job.find('div', class_='company_location')
            company_name = company_info.find('span', class_='companyName').text
            company_location = company_info.find('div', class_='companyLocation').text

            more_info = job['href']
            
            with open(f'jobPosts/{index}.txt', 'w') as f: #creates a txt file for each jobposting iteration. 'w' is permission to 'write' a file. 
                f.write(f'Position: {position.strip()} \n')
                f.write(f'Company: {company_name.strip()} \n')
                f.write(f'Location: {company_location.strip()} \n')
                f.write(f'Short Description: {description.strip()} \n')
                f.write(f'More Info: https://www.indeed.com{more_info} \n')
                f.write(f'{last_active.strip()}')
                
            print(f'File saved: {index}')
            
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60) #run every 10 minutes