import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

def find_jobs():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.indeed.com/jobs?q=software%20developer&l=remote&vjk=1e9c69b0185f6d30')
    
    jobs = driver.find_elements_by_class_name('tapItem')
    
    job_list = []

    for j in jobs:
        dictionary = {}
        
        company = j.find_element_by_class_name('companyName').text
        dictionary['company'] = company
        
        position = j.find_element_by_class_name('jobTitle').text
        dictionary['position'] = position
        
        location = j.find_element_by_class_name('companyLocation').text
        dictionary['location'] = location
        
        try: 
           salary = j.find_element_by_class_name('salary-snippet-container')
           dictionary['salary'] = salary.text
        except NoSuchElementException:
            dictionary['salary'] = 'No salary listed'
            
        description = j.find_element_by_class_name('job-snippet').text
        dictionary['description'] = description
        
        dictionary['link'] = j.get_attribute('href')
        
        job_list.append(dictionary)    
        
        with open(f'jobPosts/{company.replace(" ", "")}.txt', 'w') as f:
            f.write(f"{company}\n {position}\n {location}\n {dictionary['salary']} \n {description} \n {dictionary['link']}")
            
        print(f'File saved: {company.replace(" ", "")}.txt')      

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 15
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)  