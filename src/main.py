from fastapi import FastAPI, Request, Response


app = FastAPI()


@app.post("/")
async def index(request: Request) -> Response:

    body = await request.body()

    return Response(
        content=body,
        media_type="application/json",
        status_code=200
    )
