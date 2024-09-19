import json
import os

class Contact:
    def __init__(self, id, name, phone, comment=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment

class ContactNotFoundError(Exception):
    pass

class InvalidContactDataError(Exception):
    pass

class Phonebook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                try:
                    contacts_data = json.load(file)
                    self.contacts = [Contact(**data) for data in contacts_data]
                except json.JSONDecodeError:
                    print("Ошибка: Неверный формат данных в файле. Файл будет очищен.")
                    self.contacts = []
                    self.save_contacts()
        else:
            print("Файл контактов не найден. Создается новый.")

    def save_contacts(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file, ensure_ascii=False, indent=4)

    def add_contact(self, name, phone, comment=None):
        if not name or not phone:
            raise InvalidContactDataError("Имя и телефон обязательны для добавления контакта.")

        contact_id = len(self.contacts) + 1
        new_contact = Contact(contact_id, name, phone, comment)
        self.contacts.append(new_contact)
        self.save_contacts()

    def find_contact(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]

    def update_contact(self, contact_id, name=None, phone=None, comment=None):
        for contact in self.contacts:
            if contact.id == contact_id:
                if name:
                    contact.name = name
                if phone:
                    contact.phone = phone
                if comment is not None:
                    contact.comment = comment
                self.save_contacts()
                return True
        raise ContactNotFoundError(f"Контакт с ID {contact_id} не найден.")

    def delete_contact(self, contact_id):
        for i, contact in enumerate(self.contacts):
            if contact.id == contact_id:
                del self.contacts[i]
                self.save_contacts()
                return True
        raise ContactNotFoundError(f"Контакт с ID {contact_id} не найден.")
