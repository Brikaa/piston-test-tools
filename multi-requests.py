#!/bin/python3
import sys
from requests_futures.sessions import FuturesSession

PISTON_URL = 'http://127.0.0.1:2000/api/v2/execute'
LANGUAGE = sys.argv[1]
SOURCE_CODE_FILE = open(sys.argv[2])
SOURCE_CODE = SOURCE_CODE_FILE.read()
SOURCE_CODE_FILE.close()
VERSION = sys.argv[3] if len(sys.argv) >= 4 else '*'
RUNTIME = sys.argv[4] if len(sys.argv) >= 5 else None

session = FuturesSession()
futures = [session.post(PISTON_URL, json={
    'language': LANGUAGE,
    'version': VERSION,
    'runtime': RUNTIME,
    'files': [{ 'content': SOURCE_CODE }]
}) for i in range(30)]

print(*[future.result().json() for future in futures], sep='\n')
