from fastapi import FastAPI, Header, Depends
import jwt, os
from provider.db import Database
from provider.config import Credentials

app = FastAPI()
SECRET_KEY=os.environ.get('SECRET_KEY')
db = Database()

async def require_token(Authorization: str = Header()):
    """
    verifies the users access token
    """
    if Authorization is None:
        raise HTTPException(status_code=401, detail="no token")
    if not Authorization.startswith('Basic '):
        raise HTTPException(status_code=422, detail="invalid token")
    try:
        assert jwt.decode(Authorization[6:], SECRET_KEY, algorithms=['HS256']).get('username') is not None
    except: # bare except, ew
        raise HTTPException(status_code=403, detail="invalid token")


@app.get('/', status_code=200, dependencies=[Depends(require_token)])
async def hello():
    return {'hello': 'world'}


@app.get('/users', status_code=200, dependencies=[Depends(require_token)])
async def users():
    return {'result': db.get()}


@app.post('/register')
async def register(creds: Credentials):
    results = db.add(
        params.get('username'),
        params.get('password')
    )

    if result is False:
        raise HTTPException(status_code=400, detail='invalid query')
    if result is None:
        raise HTTPException(status_code=409, detail='that user already exists')

    return {
        'result': jwt.encode({'username', params.get('username')}, SECRET_KEY, algorithm='HS256')
    }


@app.post('/login', status_code=302)
async def login(creds: Credentials):
    results = db.get(
        params.get('username'),
        params.get('password')
    )

    if result is False:
        raise HTTPException(status_code=400, detail='invalid query')
    if result is None:
        raise HTTPException(status_code=409, detail='that user already exists')

    return {
        'result': jwt.encode({'username', params.get('username')}, SECRET_KEY, algorithm='HS256')
    }


@app.get('/healthcheck', status_code=200)
async def health():
    return {'status', 'ok'}
