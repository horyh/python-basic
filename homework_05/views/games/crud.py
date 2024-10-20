from views.games.schemas import Game
from views.games.utils import read_csv, write_csv, add_csv, get_new_id
from pydantic import ValidationError, PositiveInt


class GamesStorage:

    @staticmethod
    def validation(record):
        Game(**record)

    @staticmethod
    def get_all_records():
        return read_csv()

    @staticmethod
    def get_record_by_id(id):
        records = read_csv()
        return next((record for record in records if int(record["id"]) == id), None)

    @staticmethod
    def add_record(name: str, genre: str, cost: int):
        records = GamesStorage.get_all_records()
        id = get_new_id(records)
        # Валидация данных
        try:
            new_record = Game(id=id, name=name, genre=genre, cost=cost)
            add_csv(new_record.model_dump())
            return new_record
        except ValidationError as e:
            return {"error": e.errors()}

    @staticmethod
    def delete_record(id: PositiveInt):
        records = read_csv()
        record = next((record for record in records if int(record["id"]) == id), None)
        if not record:
            return {"message": "Запись не найдена", "record_id": id}
        records = [record for record in records if int(record["id"]) != id]
        write_csv(records)
        return {"message": "Запись успешно удалена", "record_id": id}

    @staticmethod
    def edit_record(id: int, name: str, genre: str, cost: int):
        records = read_csv()
        record = next((record for record in records if int(record["id"]) == id), None)

        if not record:
            return {"message": "Запись не найдена", "record_id": id}

        if name:
            record["name"] = name
        if genre:
            record["genre"] = genre
        if cost:
            record["city"] = cost

        try:
            GamesStorage.validation(record)
            write_csv(records)
            return {"message": "Запись успешно отредактирована", "record": record}
        except ValidationError as e:
            return {"error": e.errors()}