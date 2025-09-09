# cyan-parser

## Описание
Проект для непрерывного сбора и анализа данных о ценах недвижимости с сайта [название сайта].

## Структура проекта
- `scraper/` — код скрапера
- `data/` — база данных
- `analysis/` — анализ и визуализация результатов
- `db/` — модуль работы с бд

## Установка
```bash
git clone https://github.com/Dedushka-Lenin/cyan-parser
cd cyan-parser
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Настройка
В файле `app/core/config.py` укажите переменную URL

1. Перейдите на сайт циан выберете город и при необходимости регион, а токже прочую интерисующую вас информацию. Затем перейти на вторую страницу поиска
2. Полученная ссылка будет примерно такой `https://www.cian.ru/cat.php?deal_type=sale&district%5B0%5D=335&engine_version=2&offer_type=flat&region=1&p=2`
3. Ваша задача найти &p=2 и удалить из ссылки. После чего запишите оставшееся в переменную URL

Запустите `db.py` для создания бд и таблиц в ней если ещё не созданно


## Работа программы 
- `app/scraper/scraper.py` — Запуск преведет к началу парсинга по выбронной вами ссылке и записи в бд
- `app/analysis/analysis.py` — Запустите для получения графиков и сводки


