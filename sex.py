import streamlit as st
from pathlib import Path

# Настройка страницы
st.set_page_config(
    page_title="Заметки Ани и Гриши",
    layout="wide"
)

# Функция для загрузки и сохранения текста
def load_text(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""

def save_text(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

# Создаем файлы, если их нет
Path("ani_notes.txt").touch(exist_ok=True)
Path("grisha_notes.txt").touch(exist_ok=True)

# Заголовок приложения
st.title("Совместные заметки Ани и Гриши 📝")

# Создаем две колонки
col1, col2 = st.columns(2)

# Колонка Ани
with col1:
    st.header("Заметки Ани")
    ani_text = load_text("ani_notes.txt")
    edited_ani = st.text_area("Редактируйте заметки Ани:", ani_text, height=300, key="ani_text_area")
    if st.button("Сохранить заметки Ани", key="ani_save"):
        save_text("ani_notes.txt", edited_ani)
        st.success("Заметки Ани сохранены!")

# Колонка Гриши
with col2:
    st.header("Заметки Гриши")
    grisha_text = load_text("grisha_notes.txt")
    edited_grisha = st.text_area("Редактируйте заметки Гриши:", grisha_text, height=300, key="grisha_text_area")
    if st.button("Сохранить заметки Гриши", key="grisha_save"):
        save_text("grisha_notes.txt", edited_grisha)
        st.success("Заметки Гриши сохранены!")

# Добавляем разделитель для визуального разделения
st.markdown("---")