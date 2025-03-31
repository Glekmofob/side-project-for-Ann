import streamlit as st
from datetime import date
import json
from pathlib import Path
import os

# Настройка страницы
st.set_page_config(
    page_title="Ежедневные заметки Ани и Гриши",
    layout="wide"
)

# Функции для работы с данными
def get_data_path(user, selected_date):
    """Возвращает путь к файлу с заметками для указанного пользователя и даты"""
    return f"notes/{user}/{selected_date}.json"

def load_notes(user, selected_date):
    """Загружает заметки для указанного пользователя и даты"""
    path = get_data_path(user, selected_date)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file).get("notes", "")
    except (FileNotFoundError, json.JSONDecodeError):
        return ""

def save_notes(user, selected_date, notes):
    """Сохраняет заметки для указанного пользователя и даты"""
    Path(f"notes/{user}").mkdir(parents=True, exist_ok=True)
    path = get_data_path(user, selected_date)
    with open(path, "w", encoding="utf-8") as file:
        json.dump({"date": str(selected_date), "notes": notes}, file, ensure_ascii=False)

def init_storage():
    """Инициализирует хранилище данных"""
    os.makedirs("notes/Аня", exist_ok=True)
    os.makedirs("notes/Гриша", exist_ok=True)

# Инициализация хранилища
init_storage()

# Боковое меню для выбора страницы
page = st.sidebar.radio("Выберите страницу:", ("Аня", "Гриша"))

# Выбор даты в календаре
selected_date = st.sidebar.date_input(
    "Выберите дату:",
    date.today(),
    min_value=date(2020, 1, 1),
    max_value=date(2030, 12, 31)
)

# Заголовок с указанием даты
st.title(f"Заметки {page} на {selected_date.strftime('%d.%m.%Y')}")

# Основное содержимое страницы
notes = load_notes(page, selected_date)
edited_notes = st.text_area(
    "Редактируйте свои заметки:",
    notes,
    height=400,
    key=f"editor_{page}_{selected_date}"
)

if st.button(f"Сохранить заметки ({page})"):
    save_notes(page, selected_date, edited_notes)
    st.success("Заметки успешно сохранены!")
