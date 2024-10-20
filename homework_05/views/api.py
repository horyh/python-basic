from fastapi import APIRouter
from views.games.crud import GamesStorage

api_router = APIRouter(prefix='/api', tags=['api'])


@api_router.post(
    "/add-record-query",
    summary="Добавление новой записи через Query String",
    description="Добавляет новую запись в CSV файл через Query String.",
)
def add_record_query(name: str, genre: str, cost: int):
    new_record = GamesStorage.add_record(name, genre, cost)
    if "error" in new_record:
        return {"message": "Данные не прошли валидацию!", "record": new_record}
    return {"message": "Запись успешно добавлена!", "record": new_record}


@api_router.delete(
    "/delete-record-query",
    summary="Удаление записи через Query String",
    description="Удаляет запись из CSV файла через Query String.",
)
def delete_record_query(record_id: int):
    message = GamesStorage.delete_record(id=record_id)
    return message


@api_router.patch(
    "/edit-record-query",
    summary="Редактирование записи через Query String",
    description="Редактирует запись в CSV файле через Query String.",
)
def edit_record_query(
    record_id: int, name: str = None, genre: str = None, cost: int = None
):
    message = GamesStorage.edit_record(record_id, name, genre, cost)
    return message