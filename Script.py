import requests
import pandas as pd
from bs4 import BeautifulSoup

jobs = []
skills = []
companies = []
locations = []
times = []

for Page in range(1, 11):
    print("We are in Page:", Page)
    url = f'https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=python&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&pDate=I&sequence={Page}&startPage=1'
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    job_title_job = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in job_title_job:
        jobs.append(job.find('h2').text.strip())
        companies.append(job.find('h3', class_="joblist-comp-name").text.strip())
        locations.append(job.find('span').text.strip())
        skills.append(job.find('span', class_="srp-skills").text.strip())
        times.append(job.find('span', class_='sim-posted').text.strip())

df = pd.DataFrame({'Job': jobs, 'Company': companies, 'Location':locations,'Skills':skills,'Posted Time':times})

df.to_excel(r"C:\Users\farzaneh\Desktop\Web Scraping\Job.xlsx")


