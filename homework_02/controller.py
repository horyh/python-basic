from model import Phonebook, ContactNotFoundError, InvalidContactDataError
from view import PhonebookView


class PhonebookController:
    def __init__(self):
        self.phonebook = Phonebook()
        self.view = PhonebookView()

    def run(self):
        while True:
            action = input(
                "\nВыберите действие: [1] Показать все контакты [2] Создать контакт [3] Найти контакт [4] Изменить контакт [5] Удалить контакт [6] Выход\n")

            try:
                if action == '1':
                    self.view.show_contacts(self.phonebook.contacts)

                elif action == '2':
                    name, phone, comment = self.view.prompt_for_contact_details()
                    self.phonebook.add_contact(name, phone, comment)
                    print("Контакт добавлен.")

                elif action == '3':
                    search_term = self.view.prompt_for_search_term()
                    found_contacts = self.phonebook.find_contact(search_term)
                    self.view.show_contacts(found_contacts)

                elif action == '4':
                    contact_id = self.view.prompt_for_id()
                    name, phone, comment = self.view.prompt_for_update_details()
                    updated = self.phonebook.update_contact(contact_id, name, phone, comment)
                    print("Контакт обновлён." if updated else "Контакт не найден.")

                elif action == '5':
                    contact_id = self.view.prompt_for_id()
                    deleted = self.phonebook.delete_contact(contact_id)
                    print("Контакт удалён." if deleted else "Контакт не найден.")

                elif action == '6':
                    print("Выход из программы.")
                    break

                else:
                    print("Некорректный ввод. Попробуйте снова.")

            except (ContactNotFoundError, InvalidContactDataError) as e:
                print(f"Ошибка: {e}")