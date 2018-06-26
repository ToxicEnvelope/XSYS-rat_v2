#!/usr/bin/env python3
try:
    import socket
    import ssl
    from client.core.base_sock.BaseSock import BaseSock
except ImportError as e:
    raise e


class SslWrapper(BaseSock):

    """
        Constructor:
        This constructs an SSL Wrapper 
        over our BaseSock object as a secured layer
    """
    def __init__(self, port=10023):
        super(SslWrapper, self).__init__(port)
        self._ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)


# EOF #
