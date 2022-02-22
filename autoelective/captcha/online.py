import base64
from io import BytesIO
import json
import requests
from PIL import Image

from .captcha import Captcha
from ..config import BaseConfig
from .._internal import absp
from ..exceptions import OperationFailedError, OperationTimeoutError, RecognizerError

class APIConfig(object):

    _DEFAULT_CONFIG_PATH = '../apikey.json'

    def __init__(self, path=_DEFAULT_CONFIG_PATH):
        with open(absp(path), 'r') as handle:
            self._apikey = json.load(handle)
        assert 'username' in self._apikey.keys() and 'password' in self._apikey.keys()

    @property
    def uname(self):
        return self._apikey['username']

    @property
    def pwd(self):
        return self._apikey['password']


class TTShituRecognizer(object):

    _RECOGNIZER_URL = "http://api.ttshitu.com/base64"

    def __init__(self):
        self._config = APIConfig()
        
    def recognize(self, raw):
        _typeid_ = 1003
        encode = TTShituRecognizer._to_b64(raw)
        data = {
            "username": self._config.uname, 
            "password": self._config.pwd,
            "image": encode,
            "typeid": _typeid_
        }
        try:
            result = json.loads(requests.post(TTShituRecognizer._RECOGNIZER_URL, json=data, timeout=20).text)
        except requests.Timeout:
            raise OperationTimeoutError(msg="Recognizer connection time out")
        except requests.ConnectionError:
            raise OperationFailedError(msg="Unable to coonnect to the recognizer")
        
        if result["success"]:
            return Captcha(result["data"]["result"], None, None, None, None)
        else: # fail
            raise RecognizerError(msg="Recognizer ERROR: %s" % result["message"])

    def _to_b64(raw):
        im = Image.open(BytesIO(raw))
        try:
            if im.is_animated:
                oim = im
                oim.seek(oim.n_frames-1)
                im = Image.new('RGB', oim.size)
                im.paste(oim)
        except AttributeError:
            pass
        buffer = BytesIO()
        im.convert('RGB').save(buffer, format='JPEG')
        b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return b64