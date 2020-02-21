from pytest import mark


@mark.parametrize('hostname', ['google.com', 'cbaccesscontrol.xdl.dk'])
def test_sslv2_session(hostname):
    url = 'https://' + hostname
    from legacy_ssl_client.requests import sslv2_session
    s = sslv2_session()
    r = s.get(url)
    r.raise_for_status()


@mark.parametrize('hostname', ['google.com', 'cbaccesscontrol.xdl.dk'])
def test_tlsv1_session(hostname):
    url = 'https://' + hostname
    from legacy_ssl_client.requests import tlsv1_session
    s = tlsv1_session()
    r = s.get(url)
    r.raise_for_status()
