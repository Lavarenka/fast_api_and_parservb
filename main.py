from fastapi import FastAPI
from parser import parser
from fastapi import APIRouter, HTTPException, status, Depends
app = FastAPI()


@app.get("/{art}" , status_code=status.HTTP_201_CREATED)
async def feedback(art):
    res = parser(art)
    return {"price": res}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)  # hello - name file
    # reload перезапустить сервер если садержимое изменится
