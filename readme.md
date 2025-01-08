# Проект автотеста сайта "Регард"
___
### Используемый стек:  
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" width="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original-wordmark.svg" height="40" width="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40" />
<img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/Vyroum/Vyroum/refs/heads/main/icons/icons8-telegram.svg" width="40" height="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" width="40" height="40"/>
          
## Что тестируется
- Открытие веб-сайта
- Поиск товара через поиск
- Валидация поискового результата
- Добавление товара в корзину
- Валидация наличия товара в корзине

___ 

### Запуск проекта автотеста в Jenkins:
1. Откройте [проект](https://jenkins.autotests.cloud/job/C17-vyroum-homework14/)
2. Выберите ``Build with parameters``
3. Измените параметры, если требуется
4. Нажмите ``Build``
5. После сборки, результат работы можно увидеть в ``Allure Report``

>**Доступные параметры**:
>- Chrome версии 122.0
>- Chrome версии 125.0

### Запуск проекта автотеста локально:
1. В коде файла ``test_main_page.py`` убрать передачу параметра ``browser_set``
2. Запустить через терминал, использую команду ``pytest tests``
3. Сгенерировать отчёт, используя команду ``allure serve allure serve .\tests\test_main_page.py``
___
## Пример отчёта в Allure

### Общий отчёт о пройденном тесте
<img src="https://github.com/Vyroum/Vyroum/blob/main/icons/Screenshot_1.png" width="630" height="320"/>

### Детальный отчёт о пройденном тесте

<img src="https://github.com/Vyroum/Vyroum/blob/main/icons/Screenshot_3.png" width="630" height="320"/>

### Видеопрохождение теста

<img src="https://github.com/Vyroum/Vyroum/blob/main/icons/5d0f6222e058a005354e5f9b95638274.gif" width="630" height="320"/>

### Отчёт о прохождении теста в Telegram

<img src="https://github.com/Vyroum/Vyroum/blob/main/icons/Screenshot_2.png" width="630" height="320"/>