# Practice Automation UI Tests

Набор UI-автотестов на Python для страниц упражнений с сайта [practice-automation.com](https://practice-automation.com/).

## Стек
- Python 3.12+
- [Selenium 4](https://www.selenium.dev/)
- [pytest](https://docs.pytest.org/)
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) для автоматической загрузки драйверов Chrome/Firefox

## Структура проекта
```
volgait_codex/
├── pages/          # Page Object'ы для страниц упражнений
├── tests/          # Набор тестов pytest
├── requirements.txt
└── README.md
```

## Описание сценариев

### Страница «Form Fields»
1. Заполнение всех обязательных полей формы.
2. Получение списка инструментов из секции *Automation tools* прямо через Selenium и заполнение ими поля *Message*.
3. Отправка формы и проверка всплывающего alert`а «Message received!».
4. Проверка, что после отправки все поля и выборы сброшены в исходное состояние.

### Страница «Click Events»
Тест кликает на каждую из кнопок («Cat», «Dog», «Pig», «Cow») и проверяет, что в блоке `#demo` отображается ожидаемый звук.

### Страница «Popups»
1. Alert popup: проверка текста «Hi there, pal!».
2. Confirm popup: проверка результатов «OK it is!» и «Cancel it is!» при подтверждении и отмене.
3. Prompt popup: ввод имени и проверка сообщения «Nice to meet you, …», а затем сценарий отмены с ответом «Fine, be that way…».
4. Tooltip: проверка, что после клика текст тултипа появляется и исчезает повторным кликом.

## Подготовка окружения
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

### Локальный запуск
По умолчанию используется браузер Chrome в headless-режиме. Для запуска тестов:
```bash
pytest
```

Чтобы выполнить тесты в Firefox, передайте переменную окружения:
```bash
BROWSER=firefox pytest
```

> ⚠️ Для успешного запуска требуется установленный браузер Chrome (или Firefox для соответствующего режима). Драйверы будут скачаны автоматически.

### Отчёты Allure
Allure не подключён в качестве обязательного шага, но тесты структурированы таким образом, что его легко добавить, подключив плагин `allure-pytest` и настроив генерацию отчётов в пайплайне.

## Полезные советы
- Каждый тест использует паттерн Page Object для переиспользуемости локаторов и шагов.
- Для ускорения тестов задан размер окна и headless-режим.
- В коде нет жёстких ожиданий `sleep`, вся синхронизация построена на `WebDriverWait`.
