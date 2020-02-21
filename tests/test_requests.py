from pytest import mark

from legacy_ssl_client.requests import sslv2_session


@mark.parametrize('hostname', ['google.com', 'cbaccesscontrol.xdl.dk'])
def test_sslv2_session(hostname):
    url = 'https://' + hostname
    s = sslv2_session()
    r = s.get(url)
    r.raise_for_status()
