from fastapi import FastAPI, Query, Path, Body
from shemas import Book, Author, BookOut
from typing import List

app = FastAPI()


#
# @app.get('/')
# def home():
#     return {"key": "value"}


@app.get('/{pk}')
def get_item(pk: int, q: int = None):
    return {"key": pk, "q": q}


# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {"user": pk, "item": item}


@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    # book = item.dict()
    # book["id"] = 3
    #return Book
    return  BookOut(**item.dict(),id=5)

# @app.post('/author')
# def create_author(author: Author = Body(..., embed=True)): # добавлен ключ Author
#     return {"author": author}
#
#
# @app.get('/book')
# def get_book(q: List[str] = Query(["test", "test1"], description='Search book', deprecated=True)):
#     return q
#
#
# # Функция получает книгу по id
# @app.get('/book/{pk}')
# def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=200)):
#     return {'pk': pk, "pages": pages}

# if __name__ == "__main__":
#     uvicorn.run("main: app", port = 8000, reload = True)
