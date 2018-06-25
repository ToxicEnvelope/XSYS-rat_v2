#!/usr/bin/env python3
try:
    import socket
    import ssl
    from client.core.base_sock.BaseSock import BaseSock
except ImportError as e:
    raise e


class SslWrapper(BaseSock):

    __SERVER_HOSTNAME = "www.cr-teachable.com"
    """
        Constructor:
        This constructs an SSL Wrapper 
        over our BaseSock object as a secured layer
    """
    def __init__(self, port=443):
        super(SslWrapper, self).__init__(port)
        self._ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._s = super(SslWrapper, self)._get_sock
        self._ssl_sock = None
        self._conn = None
        self._cert = None
        self.init_preps()
    """
        This method initialize a context preparation
        for the SSL Wrapper to handle Certificate Authentication        
    """
    def init_preps(self):
        self._ctx.verify_mode = ssl.CERT_REQUIRED
        self._ctx.check_hostname = True
        self._ctx.load_default_certs()
        try:
            self._conn = self._ssl_sock = self._ctx.wrap_socket(self._s, server_hostname=self.__SERVER_HOSTNAME)
        except ssl.socket_error as e:
            raise e
    """
        This method connect to a 
        the server end-point using teh SSL layer
    """
    def connect_to_server_and_fetch(self):
        try:
            self._conn.connect((self.__SERVER_HOSTNAME, super(SslWrapper, self)._get_port))
            self._cert = self._conn.getpeercert()
        except ssl.socket_error as e:
            raise e
    """
        This method responsible to
        return a socket instance
    """
    @property
    def _get_ssl_sock(self):
        try:
            if not self._ssl_sock:
                raise "[Err] '_ssl_sock' doesn't exists : {}".format(self._ssl_sock)
            else:
                return self._ssl_sock
        except Exception as e:
            raise e
    """
        This method responsible to
        store a new socket object 
        to _ssl_sock variable
    """
    @_get_ssl_sock.setter
    def _set_ssl_sock(self, sock):
        try:
            if not sock:
                raise "[Err] cannot accept empty param : {}".format(self._ssl_sock)
            elif not isinstance(sock, socket.socket):
                raise "[Err] cannot accept param type : {}".format(type(sock))
            else:
                self._ssl_sock = sock
        except Exception as e:
            raise e
    """
        This method responsible to
        return a client certification
    """
    @property
    def _get_client_cert(self):
        try:
            if not self._cert:
                raise "[Err] '_cert' doesn't exists : {}".format(self._cert)
            else:
                return self._cert
        except Exception as e:
            raise e
    """
        This method responsible to
        store a new client certification 
        to _cert variable
    """
    @_get_ssl_sock.setter
    def _set_client_cert(self, cert):
        try:
            if not cert:
                raise "[Err] cannot accept empty param : {}".format(cert)
            elif not isinstance(cert, tuple):
                raise "[Err] cannot accept param type : {}".format(type(cert))
            else:
                self._cert = cert
        except Exception as e:
            raise e
# EOF #


""" for debugging purposes """
if __name__ == "__main__":
    ssl_sock = SslWrapper(8080)
    ssl_sock.connect_to_server_and_fetch()