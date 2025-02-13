from fastapi import FastAPI

from parser import parser_price, parser_body
from fastapi import APIRouter, HTTPException, status, Depends

app = FastAPI()


@app.get("/{art}", status_code=status.HTTP_201_CREATED)
async def feedback(art):
    art_price = parser_price(art)
    art_name = parser_body(art)
    try:
        name = art_name['imt_name']
    except:
        name = None

    try:
        description = art_name['description']
    except:
        description = None

    try:
        price = art_price
    except:
        price = None

    try:
        link = f'https://www.wildberries.by/catalog/{art}/detail.aspx'
    except:
        link = None

    return {
        'name': name,
        'description': description,
        'price': price,
        'link': link,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)  # hello - name file

    # reload перезапустить сервер если садержимое изменится
