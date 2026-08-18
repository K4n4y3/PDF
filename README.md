# Chat with PDFs

Streamlit-приложение для общения с содержимым PDF-файлов через LLM. Загружаете один или несколько PDF, приложение разбивает текст на чанки, строит векторное хранилище (FAISS) и отвечает на вопросы по документам с сохранением истории диалога.

## Стек

- [Streamlit](https://streamlit.io/) — веб-интерфейс
- [LangChain](https://www.langchain.com/) — оркестрация цепочки вопрос-ответ
- [OpenAI](https://platform.openai.com/) — эмбеддинги и чат-модель
- [FAISS](https://github.com/facebookresearch/faiss) — векторное хранилище
- [PyPDF2](https://pypi.org/project/PyPDF2/) — извлечение текста из PDF

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск локально

```bash
streamlit run app.py
```

После запуска откройте ссылку в браузере, введите свой OpenAI API-ключ в боковой панели, загрузите PDF-файлы, нажмите "Process" и задавайте вопросы по содержимому документов.

Ключ можно не вводить вручную каждый раз — для локальной разработки создайте файл `.env` в корне проекта:

```
OPENAI_API_KEY=your_api_key_here
```

