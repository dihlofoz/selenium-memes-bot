from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pathlib import Path

# Open browser
try: 
    browser = webdriver.Firefox()
    browser.get('https://www.memify.ru/')

    # Открываем страницу топ мемов
    click_top = browser.find_element(By.CSS_SELECTOR, 'a[href="/top/"]').click()
    sleep(3)

    links_to_memes = []
    requiredSize = 30
    prefix = 'https://www.memify.ru'

    # Прокручиваем страницу вниз для подгрузки новых мемов
    while len(links_to_memes) < requiredSize:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(6)

        # Ищем мемы через CSS_SELECTOR
        memes_elements = browser.find_elements(By.CSS_SELECTOR, 'a[data-selector=".meme-detail"]')
        
        # Подсчитываем мемы наглядно контролируя процесс исключая повторения
        for element in memes_elements:
            link_mem = element.get_attribute('data-src')

            if link_mem and link_mem not in links_to_memes:
                print(f'Часть ссылки на мемасик: {link_mem}')
                links_to_memes.append(link_mem.strip())
    
finally:
    browser.quit()

# Выводим полученный результат в отдельный файл
full_links = [f"{prefix}{link_mem}" for link_mem in links_to_memes]
output_path = Path('meme (отборнейший калл).txt')
with open('meme (отборнейший калл).txt', 'w') as meme_file:
    for link in full_links:
        meme_file.write(f'{link}\\\n')

print("Данные записаны в файл meme.txt.")