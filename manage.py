#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qarch.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    
    import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--app=http://link.tl/21orH")

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
wait = WebDriverWait(driver, 20)

element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/a')))
element.click()
