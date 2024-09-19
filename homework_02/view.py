class PhonebookView:
    @staticmethod
    def show_contacts(contacts):
        if not contacts:
            print("Контакт не найден.")
            return
        for contact in contacts:
            print(f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Комментарий: {contact.comment or ''}")

    @staticmethod
    def prompt_for_contact_details():
        name = input("Введите имя контакта: ")
        phone = input("Введите телефон контакта: ")
        comment = input("Введите комментарий (по желанию): ")
        return name, phone, comment

    @staticmethod
    def prompt_for_search_term():
        return input("Введите имя или телефон для поиска: ")

    @staticmethod
    def prompt_for_update_details():
        name = input("Введите новое имя (оставьте пустым для пропуска): ")
        phone = input("Введите новый телефон (оставьте пустым для пропуска): ")
        comment = input("Введите новый комментарий (оставьте пустым для пропуска): ")
        return name or None, phone or None, comment or None

    @staticmethod
    def prompt_for_id():
        return int(input("Введите ID контакта: "))