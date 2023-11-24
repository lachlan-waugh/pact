import pytest
import requests
from pact import Consumer, Producer
from tests.config import HOST, PORT

pact = Consumer('Userconsumer').has_pact_with(
    Provider('UserProvider'),
    hostname=HOST,
    port=PORT,
    pact_dir=DIR
)

pact.start_service()
