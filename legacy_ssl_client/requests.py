from logging import getLogger
import ssl
from urllib3.poolmanager import PoolManager
from requests import Session
from requests.adapters import HTTPAdapter

assert HTTPAdapter.init_poolmanager


logger = getLogger(__name__)


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
        if hasattr(ssl, 'TLSVersion'):
            #ctx.minimum_version = ssl.TLSVersion.SSLv3 # SSLv2 is not there...
            ctx.minimum_version = ssl.TLSVersion.MINIMUM_SUPPORTED
        logger.debug('SSLv2HTTPAdapter ctx.options: %r', ctx.options)
        super().__init__(ssl_context=ctx, **kwargs)


def sslv2_session():
    s = Session()
    s.mount('https://', SSLv2HTTPAdapter())
    return s



class TLSv1HTTPAdapter (CustomSSLContextHTTPAdapter):

    def __init__(self, **kwargs):
        ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ctx.options |= ssl.PROTOCOL_TLS
        ctx.options |= ssl.OP_NO_SSLv3
        ctx.options |= ssl.OP_NO_SSLv2
        ctx.options &= ~ssl.OP_NO_TLSv1
        if hasattr(ssl, 'TLSVersion'):
            ctx.minimum_version = ssl.TLSVersion.TLSv1
        logger.debug('TLSv1HTTPAdapter ctx.options: %r', ctx.options)
        super().__init__(ssl_context=ctx, **kwargs)


def tlsv1_session():
    s = Session()
    s.mount('https://', TLSv1HTTPAdapter())
    return s


