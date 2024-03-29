# TF-IDF

## О сути

Это приложение для анализа загруженного текстового файла и вычисления показателей TF и IDF для каждого слова.

Текстовый файл считается корпусом документов, в котором документы разделены символом переноса строки.

База данных не используется.

## Запуск

Команды для запуска для Ubuntu. В других операционных системах команды могут отличаться.

```bash
git clone https://github.com/sitdoff/text-analysis-tf-idf.git
cd text-analysis-tf-idf
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 text_analysis/manage.py runserver
```

По умолчанию проект будет доступен по адресу http://localhost:8000

## Как это выглядит

<details>
    <summary>Форма загрузка файла</summary>

![Иллюстрация к проекту](https://github.com/sitdoff/text-analysis-tf-idf/raw/main/images/2024-03-28_08-22.png)

</details>

<details>
    <summary>Отчет</summary>

![Иллюстрация к проекту](https://github.com/sitdoff/text-analysis-tf-idf/raw/main/images/2024-03-28_08-21.png)

</details>
