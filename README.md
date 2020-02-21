legacy-ssl-client
=================

Python Requests Session object configured to connect to servers with historical SSL configuration.


Installation
------------

```shell
$ pip install https://github.com/messa/legacy-ssl-client/archive/master.zip
```


Usage
-----

```python3
from legacy_ssl_client.requests import sslv2_session

s = sslv2_session()
r = s.get('https://example.com')
r.raise_for_status()
```


Links
-----

- https://requests.readthedocs.io/en/master/
- https://requests.readthedocs.io/en/master/user/advanced/#example-specific-ssl-version
- https://lukasa.co.uk/2013/01/Choosing_SSL_Version_In_Requests/
- https://github.com/psf/requests/blob/master/requests/adapters.py
- https://github.com/psf/requests/issues/3774#issuecomment-267871876
- https://github.com/urllib3/urllib3/blob/master/src/urllib3/poolmanager.py
