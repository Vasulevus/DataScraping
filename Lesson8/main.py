from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json


def parser():
    driver = webdriver.Chrome()
    maxpage = 3

    wait = WebDriverWait(driver,30)
    results = []
    for page in range(1,maxpage):
        driver.get('https://jobs.marksandspencer.com/job-search?page=' + str(page) + '&radius=')
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ais-Hits-item')))
        jobs = driver.find_elements(By.CLASS_NAME,'ais-Hits-item')
        for job in jobs:
            url = job.find_element(By.TAG_NAME,'a').get_attribute('href')
            title = job.find_element(By.TAG_NAME, 'h3').text
            results.append({
                'title': title,
                'url': url
            })

    driver.quit()

    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)


if __name__ == '__main__':
    parser()