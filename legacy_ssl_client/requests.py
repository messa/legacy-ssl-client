import ssl
from urllib3.poolmanager import PoolManager
from requests import Session
from requests.adapters import HTTPAdapter

assert HTTPAdapter.init_poolmanager


class CustomSSLContextHTTPAdapter (HTTPAdapter):
    '''Transport adapter that allows us to use custom ssl_context.'''

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)


class SSLv2HTTPAdapter (CustomSSLContextHTTPAdapter):

    def __init__(self, **kwargs):
        ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ctx.options &= ~ssl.OP_NO_SSLv3
        ctx.options &= ~ssl.OP_NO_SSLv2
        super().__init__(ssl_context=ctx, **kwargs)


def sslv2_session():
    s = Session()
    s.mount('https://', SSLv2HTTPAdapter())
    return s
