from pytest import mark, skip


@mark.parametrize('hostname', ['google.com', 'cbaccesscontrol.xdl.dk'])
def test_adapter_with_ssl_version(hostname):
    import ssl
    from urllib3.poolmanager import PoolManager
    from requests import Session
    from requests.adapters import HTTPAdapter

    assert HTTPAdapter.init_poolmanager

    class CustomHttpAdapter (HTTPAdapter):
        '''Transport adapter" that allows us to use custom ssl_version.'''

        def __init__(self, ssl_version=None, **kwargs):
            self.ssl_version = ssl_version
            super().__init__(**kwargs)

        def init_poolmanager(self, connections, maxsize, block=False):
            self.poolmanager = PoolManager(
                num_pools=connections, maxsize=maxsize,
                block=block, ssl_version=self.ssl_version)

    s = Session()
    s.mount('https://', CustomHttpAdapter(ssl.PROTOCOL_SSLv23))
    url = 'https://' + hostname
    try:
        r = s.get(url)
        r.raise_for_status()
    except Exception as e:
        skip(repr(e))


@mark.parametrize('hostname', ['google.com', 'cbaccesscontrol.xdl.dk'])
def test_adapter_with_ssl_context(hostname):
    import ssl
    from urllib3.poolmanager import PoolManager
    from requests import Session
    from requests.adapters import HTTPAdapter

    assert HTTPAdapter.init_poolmanager

    class CustomHttpAdapter (HTTPAdapter):
        '''Transport adapter" that allows us to use custom ssl_context.'''

        def __init__(self, ssl_context=None, **kwargs):
            self.ssl_context = ssl_context
            super().__init__(**kwargs)

        def init_poolmanager(self, connections, maxsize, block=False):
            self.poolmanager = PoolManager(
                num_pools=connections, maxsize=maxsize,
                block=block, ssl_context=self.ssl_context)

    s = Session()
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options &= ~ssl.OP_NO_SSLv3
    ctx.options &= ~ssl.OP_NO_SSLv2
    s.mount('https://', CustomHttpAdapter(ctx))
    url = 'https://' + hostname
    try:
        r = s.get(url)
        r.raise_for_status()
    except Exception as e:
        skip(repr(e))
