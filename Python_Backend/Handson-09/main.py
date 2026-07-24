from fastapi import (
    FastAPI,
    Header,
    HTTPException
)

from auth import (
    create_token,
    verify_token
)

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "JWT API"
    }


@app.post("/login")
def login():

    return {
        "token": create_token()
    }


@app.get("/profile")
def profile(
    authorization: str = Header(
        default=None,
        alias="Authorization"
    )
):

    print("AUTH:", authorization)

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Token required"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )
    user = verify_token(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    return {
        "message": "Access granted",
        "user": user
    }