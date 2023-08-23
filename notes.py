"""
добавление:
python notes.py add --title "Название заметки" --msg "тело заметки"

Просмотр списка заметок:
python notes.py list

Просмотр списка заметок с фильтрацией по дате:
python notes.py list --date "дд-мм-гггг дд-мм-гггг"

Удаление заметки по ID:
python notes.py delete --id ID_заметки

Небольшая инструкция по использованию:
python notes.py --help
"""

import json
import os
import argparse
from datetime import datetime

NOTES_FILE = "data/notes.json"


def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
            return notes
    return []


def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)


def add_note(title, msg):
    notes = load_notes()
    note_id = len(notes) + 1
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "message": msg,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")


def list_notes(date_start=None, date_end=None):
    notes = load_notes()
    if date_start and date_end:
        filtered_notes = [note for note in notes if string_to_date(date_start) < string_to_date(note["timestamp"].split()[0]) < string_to_date(date_end)]
    else:
        filtered_notes = notes
    for note in filtered_notes:
        print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Дата/время: {note["timestamp"]}')
        print(f'Тело заметки: {note["message"]}\n')


def delete_note(note_id):
    notes = load_notes()
    updated_notes = [note for note in notes if note["id"] != note_id]
    if len(updated_notes) < len(notes):
        save_notes(updated_notes)
        print(f"Заметка с ID {note_id} успешно удалена")
    else:
        print(f"Заметка с ID {note_id} не найдена")


def string_to_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y")


def main():
    parser = argparse.ArgumentParser(description="Управление заметками")
    parser.add_argument("command", choices=["add", "list", "delete"], help="Команда для выполнения")
    parser.add_argument("--title", help="Заголовок заметки")
    parser.add_argument("--id", help="ID заметки")
    parser.add_argument("--msg", help="Тело заметки")
    parser.add_argument("--date", help="Диапозон даты для фильтрации заметок (дд-мм-гггг дд-мм-гггг)")

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.title, args.msg)
    elif args.command == "list":
        if args.date:
            dates = args.date.split(' ')
            list_notes(dates[0], dates[1])
        else:
            list_notes()
    elif args.command == "delete":
        delete_note(int(args.id))


if __name__ == "__main__":
    main()
