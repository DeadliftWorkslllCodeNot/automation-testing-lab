# Лабораторная работа № 5

Автоматизация тестирования SauceDemo с pytest, Playwright и GitHub Actions.

## Установка и запуск

Требуется Python 3.12 и доступ к https://www.saucedemo.com/.

Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v test_login.py
```

Linux или macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install --with-deps chromium
python -m pytest -v test_login.py
```

Для просмотра браузера используйте `--headed --slowmo 700`.

Для сохранения результатов

```bash
python -m pytest -v test_login.py --screenshot on --full-page-screenshot --tracing retain-on-failure --output test-results --junitxml=reports/results.xml --html=reports/report.html --self-contained-html
```

## Проверки

1. Видимость формы авторизации.
2. Успешный вход и открытие каталога.
3. Добавление Backpack и счётчик корзины 1.
4. Открытие корзины и название Sauce Labs Backpack.
5. Сообщение об ошибке при неверном пароле.

Каждый тест получает отдельную страницу и контекст браузера через фикстуру
`page`. Учётные данные standard_user / secret_sauce опубликованы на учебном
сайте SauceDemo.

## Демонстрация неуспешной проверки

В `test_successful_login` временно замените ожидаемый адрес
`https://www.saucedemo.com/inventory.html` на
`https://www.saucedemo.com/incorrect.html` и выполните полный набор.
Ожидается `1 failed, 4 passed`. После возврата правильного URL ожидается
`5 passed`. Исправленная версия является итоговой.

## Непрерывная интеграция

`.github/workflows/tests.yml` запускается при `push`, `pull_request` и
`workflow_dispatch`. Runner Ubuntu устанавливает Python 3.12, зависимости и
Chromium, запускает все пять тестов и сохраняет HTML, JUnit XML, снимки и
трассу неуспешного теста в артефакте GitHub Actions.

Репозиторий: https://github.com/DeadliftWorkslllCodeNot/automation-testing-lab

История запусков: https://github.com/DeadliftWorkslllCodeNot/automation-testing-lab/actions

При изменении кода GitHub автоматически проверяет все пять сценариев.
Файл test_login.py в основной ветке содержит исправленный URL inventory.html.

## Сетевые настройки

На обычном компьютере дополнительные настройки не требуются.
`conftest.py` также поддерживает явно заданные переменные
`PLAYWRIGHT_PROXY_SERVER` и `PLAYWRIGHT_BROWSER_HOME` для среды с управляемым
прокси и отдельным хранилищем доверенных сертификатов.
Проверка TLS остаётся включённой.
