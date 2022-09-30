#!/bin/python3
import sys
from requests_futures.sessions import FuturesSession

PISTON_URL = 'http://127.0.0.1:2000/api/v2/execute'
FILE_NAME = sys.argv[1]
[_, LANGUAGE] = sys.argv[1].split('.')
SOURCE_CODE_FILE = open(FILE_NAME)
SOURCE_CODE = SOURCE_CODE_FILE.read()
SOURCE_CODE_FILE.close()
NO_REQUESTS = int(sys.argv[2]) if len(sys.argv) >= 3 else 16
VERSION = sys.argv[3] if len(sys.argv) >= 4 else '*'
RUNTIME = sys.argv[4] if len(sys.argv) >= 5 else None

session = FuturesSession()
futures = [session.post(PISTON_URL, json={
    'language': LANGUAGE,
    'version': VERSION,
    'runtime': RUNTIME,
    'files': [{ 'content': SOURCE_CODE }]
}) for i in range(NO_REQUESTS)]

