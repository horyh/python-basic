from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from views.games.crud import GamesStorage

view_router = APIRouter(tags=['views'])
templates = Jinja2Templates(directory="templates")

@view_router.get(
    "/record/{record_id}",
    response_class=HTMLResponse,
    summary="Получение записи по ID",
    description="Возвращает запись из CSV файла по указанному ID в формате HTML.",
)
def get_record(request: Request, record_id: int):
    record = GamesStorage.get_record_by_id(record_id)
    context = {"request": request, "record": record}
    return templates.TemplateResponse("record_by_id.html", context)


@view_router.get(
    "/records",
    response_class=HTMLResponse,
    summary="Получение всех записей игр",
    description="Возвращает все записи из CSV файла в формате HTML.",
)
def get_records(request: Request):
    records = GamesStorage.get_all_records()
    context = {"request": request, "records": records}
    return templates.TemplateResponse("records_list.html", context)


@view_router.post(
    "/add-record",
    response_class=HTMLResponse,
    summary="Добавление новой записи",
    description="""
    Добавляет новую запись в CSV файл и возвращает обновленный
    список записей в формате HTML.""",
)
def add_record(
    request: Request, name: str = Form(...), genre: str = Form(...), cost: int = Form(...)
):
    record = GamesStorage.add_record(name, genre, cost)
    records = GamesStorage.get_all_records()
    if "error" in record:
        target = record["error"][0]["input"]
        error = record["error"][0]["msg"]
        message = f"Error! Validation error, {target} - {error}"
    else:
        message = "Запись успешно добавлена!"
    context = {
        "request": request,
        "records": records,
        "message": message,
    }
    return templates.TemplateResponse("records_list.html", context)