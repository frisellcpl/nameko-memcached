# nameko-memcached
[![PyPI version](https://badge.fury.io/py/nameko-memcached.svg)](https://badge.fury.io/py/nameko-memcached)
[![Build Status](https://travis-ci.org/frisellcpl/nameko-memcached.svg?branch=master)](https://travis-ci.org/frisellcpl/nameko-memcached)

Memcached dependency for nameko services. Note that this dependency uses \
memcached binary protocol. Supported by python-binary-memcached.

Inspiration and structure **proudly** stolen from nameko-redis :) Thanks guys!

## Installation
```
pip install nameko-memcached
```

## Usage
```python
from nameko.rpc import rpc
from nameko_memcached import Memcached


class MyService(object):
    name = "my_service"

    memcached = Memcached()

    @rpc
    def hello(self, name):
        self.memcached.set("foo", name)
        return "Hello, {}!".format(name)

    @rpc
    def bye(self):
        name = self.memcached.get("foo")
        return "Bye, {}!".format(name)
```

To specify memcached uri(s) and optional username/password you will need a config
```yaml
AMQP_URI: 'amqp://guest:guest@localhost'
MEMCACHED_URIS: ['127.0.0.1:11211', ]
MEMCACHED_USER: 'playerone'
MEMCACHED_PASSWORD: 'ready'
```

You can also pass extra options to the class, like this:
```python
class MyService(object):
    name = "my_service"

    memcached = Memcached(socket_timeout=5)

    ...
```
