from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json


def parse():
    driver = webdriver.Chrome()
    maxpage = 3

    wait = WebDriverWait(driver,10)
    result = []
    for page in range(1,maxpage):
        driver.get('https://jobs.aon.com/jobs?page={page}')
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'job-title-link')))
        jobs = driver.find_elements(By.CLASS_NAME,'job-title-link')
        for job in jobs:
            url = job.get_attribute('href')
            title = job.find_element(By.TAG_NAME, 'span').text
            result.append({
                'url': url,
                'title': title
            })

    driver.quit()

    with open('result.json', 'w') as f:
        json.dump(result, f, indent=4)



if __name__ == '__main__':
    parse()