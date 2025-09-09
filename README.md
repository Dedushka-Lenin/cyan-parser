# cyan-parser

## Описание
Проект для непрерывного сбора и анализа данных о ценах недвижимости с сайта [название сайта].

## Структура проекта
- `scraper/` — код скрапера
- `flows/` — Prefect flow и деплой
- `data/` — сырые данные (csv)
- `analysis/` — анализ и визуализация результатов

## Установка
```bash
git clone https://github.com/Dedushka-Lenin/cyan-parser
cd cyan-parser
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt