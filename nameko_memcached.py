from weakref import WeakKeyDictionary

from nameko.extensions import DependencyProvider

import bmemcached


class Memcached(DependencyProvider):
    def __init__(self, **options):
        self.clients = WeakKeyDictionary()
        self.options = options

    def setup(self):
        self.uris = self.container.config['MEMCACHED_URIS']
        self.user = self.container.config.get('MEMCACHED_USER', None)
        self.password = self.container.config.get('MEMCACHED_PASSWORD', None)

    def get_dependency(self, worker_ctx):
        client = self._get_client()
        self.clients[worker_ctx] = client
        return client

    def worker_teardown(self, worker_ctx):
        client = self.clients.pop(worker_ctx)
        client.disconnect_all()

    def _get_client(self):
        return bmemcached.Client(
            servers=self.uris,
            username=self.user,
            password=self.password,
            **self.options
        )
