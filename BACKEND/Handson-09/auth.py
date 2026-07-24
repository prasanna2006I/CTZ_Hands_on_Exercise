from jose import jwt, JWTError

SECRET = "secret123"


def create_token():

    return jwt.encode(
        {
            "user": "admin"
        },
        SECRET,
        algorithm="HS256"
    )


def verify_token(
    token: str
):
    try:

        payload = jwt.decode(
            token,
            SECRET,
            algorithms=["HS256"]
        )
        return payload
    except JWTError:

        return None