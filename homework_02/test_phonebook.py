import pytest
import os
from .model import Phonebook, ContactNotFoundError, InvalidContactDataError


@pytest.fixture
def setup_phonebook():
    # Создаем временный файл для тестов
    test_filename = 'test_contacts.json'
    pb = Phonebook(test_filename)

    # Очищаем файл перед началом тестов
    pb.contacts = []
    pb.save_contacts()

    # Добавляем несколько контактов для тестирования
    pb.add_contact('John Doe', '1234567890', 'Friend')
    pb.add_contact('Jane Smith', '0987654321', 'Colleague')

    yield pb  # Возвращаем объект Phonebook для использования в тестах

    # Удаляем временный файл после тестов
    os.remove(test_filename)


def test_add_contact(setup_phonebook):
    pb = setup_phonebook
    pb.add_contact('Alice Johnson', '5555555555', 'Family')

    assert len(pb.contacts) == 3  # Проверяем, что контакт добавлен
    assert pb.contacts[-1].name == 'Alice Johnson'


def test_find_contact(setup_phonebook):
    pb = setup_phonebook

    found_contacts = pb.find_contact('Jane')

    assert len(found_contacts) == 1  # Проверяем, что найден один контакт
    assert found_contacts[0].name == 'Jane Smith'


def test_update_contact(setup_phonebook):
    pb = setup_phonebook

    updated = pb.update_contact(1, name='Johnathan Doe')

    assert updated is True  # Проверяем, что обновление прошло успешно
    assert pb.contacts[0].name == 'Johnathan Doe'


def test_delete_contact(setup_phonebook):
    pb = setup_phonebook

    deleted = pb.delete_contact(2)

    assert deleted is True  # Проверяем, что удаление прошло успешно
    assert len(pb.contacts) == 1  # Проверяем, что остался только один контакт после удаления


def test_invalid_contact_data(setup_phonebook):
    pb = setup_phonebook

    with pytest.raises(InvalidContactDataError):
        pb.add_contact('', '')  # Проверяем, что возникает ошибка при добавлении некорректного контакта


def test_contact_not_found(setup_phonebook):
    pb = setup_phonebook

    with pytest.raises(ContactNotFoundError):
        pb.update_contact(99)  # Проверяем, что возникает ошибка при обновлении несуществующего контакта