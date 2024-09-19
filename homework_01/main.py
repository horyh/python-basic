import json
import os

def load_contacts(filename='contacts.json'):
    """Загружает контакты из файла."""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_contacts(contacts, filename='contacts.json'):
    """Сохраняет контакты в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)

def show_contacts(contacts):
    """Показывает все контакты."""
    if not contacts:
        print("Справочник пуст.")
        return
    for contact in contacts:
        print(
            f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact.get('comment', '')}")

def create_contact(contacts, name, phone, comment=None):
    """Создает новый контакт."""
    contact_id = len(contacts) + 1
    contact = {'id': contact_id, 'name': name, 'phone': phone}
    if comment:
        contact['comment'] = comment
    contacts.append(contact)
    save_contacts(contacts)
    print("Контакт добавлен.")

def find_contact(contacts, search_term):
    """Находит контакт по имени или телефону."""
    found_contacts = [c for c in contacts if
                      search_term.lower() in c['name'].lower() or search_term in c['phone']]
    if found_contacts:
        for contact in found_contacts:
            print(
                f"ID: {contact['id']}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact.get('comment', '')}")
    else:
        print("Контакт не найден.")  # Изменено сообщение

def update_contact(contacts, contact_id, name=None, phone=None, comment=None):
    """Обновляет контакт по ID."""
    for contact in contacts:
        if contact['id'] == contact_id:
            if name:
                contact['name'] = name
            if phone:
                contact['phone'] = phone
            if comment is not None:
                contact['comment'] = comment
            save_contacts(contacts)
            print("Контакт обновлён.")
            return
    print("Контакт не найден.")

def delete_contact(contacts, contact_id):
    """Удаляет контакт по ID."""
    for i, contact in enumerate(contacts):
        if contact['id'] == contact_id:
            del contacts[i]
            save_contacts(contacts)
            print("Контакт удалён.")
            return
    print("Контакт не найден.")

def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        action = input(
            "\nВыберите действие: [1] Показать все контакты [2] Создать контакт [3] Найти контакт [4] Изменить контакт [5] Удалить контакт [6] Выход\n")

        if action == '1':
            show_contacts(contacts)

        elif action == '2':
            name = input("Введите имя контакта: ")
            phone = input("Введите телефон контакта: ")
            comment = input("Введите комментарий (по желанию): ")
            create_contact(contacts, name, phone, comment)

        elif action == '3':
            search_term = input("Введите имя или телефон для поиска: ")
            find_contact(contacts, search_term)

        elif action == '4':
            contact_id = int(input("Введите ID контакта для изменения: "))
            name = input("Введите новое имя (оставьте пустым для пропуска): ")
            phone = input("Введите новый телефон (оставьте пустым для пропуска): ")
            comment = input("Введите новый комментарий (оставьте пустым для пропуска): ")
            update_contact(contacts, contact_id, name or None, phone or None, comment or None)

        elif action == '5':
            contact_id = int(input("Введите ID контакта для удаления: "))
            delete_contact(contacts, contact_id)

        elif action == '6':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()