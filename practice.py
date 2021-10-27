from bs4 import BeautifulSoup

# 'r' tells python to read that file only
with open('index.html', 'r') as html_file: 
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml') #lxml is the parser installed earlier
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')

    