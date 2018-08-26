import eventlet
eventlet.monkey_patch()  # noqa (code before rest of imports)

from nameko.containers import ServiceContainer
from nameko.testing.services import entrypoint_hook, dummy

import pytest

import bmemcached

from nameko_memcached import Memcached


TEST_KEY = 'nameko-test-value'


class ExampleService(object):
    name = "exampleservice"
    memcached = Memcached()

    @dummy
    def write(self, value):
        self.memcached.set(TEST_KEY, value)

    @dummy
    def read(self):
        return self.memcached.get(TEST_KEY)


@pytest.fixture
def memcached():
    uri = '127.0.0.1:11211'

    yield uri

    client = bmemcached.Client((uri, ))
    client.delete(TEST_KEY)


def test_end_to_end(memcached):
    config = {
        'MEMCACHED_URIS': [memcached, ]
    }

    container = ServiceContainer(ExampleService, config)
    container.start()

    # write through the service
    with entrypoint_hook(container, "write") as write:
        write("foobar")

    # verify changes written to memcached
    client = bmemcached.Client((memcached, ))
    assert client.get(TEST_KEY) == "foobar"

    # read through the service
    with entrypoint_hook(container, "read") as read:
        assert read() == "foobar"
