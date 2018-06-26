#!/usr/bin/env python3
try:
    import socket
except ImportError as e:
    raise e


class BaseSock:
    """
        Constructor:
        This construct a new BaseSock object to
        handle and support network connection using
        Ethernet infra and TCP communication protocol
    """
    def __init__(self, port):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._port = port
    """
        This method responsible to 
        return a socket instance  
    """
    @property
    def _get_sock(self):
        try:
            if not self._sock:
                raise "[Err] '_sock' doesn't exists : {}".format(self._sock)
            else:
                return self._sock
        except Exception as e:
            raise e
    """
        This method responsible to store 
        a socket object to _sock variable
    """
    @_get_sock.setter
    def _set_sock(self, sock):
        try:
            if not sock:
                raise "[Err] cannot accept empty param : {}".format(sock)
            elif not isinstance(sock, socket.socket):
                raise "[Err] cannot accept param type : {}".format(type(sock))
            else:
                self._sock = sock
        except Exception as e:
            raise e
    """
        This method responsible to
        return int which represents
        a port number 
    """
    @property
    def _get_port(self):
        try:
            if not self._port:
                raise "[Err] '_port' does't exists : {}".format(self._port)
            else:
                return self._port
        except Exception as e:
            raise e
    """
        This method responsible to store
        an int number to _port variable
    """
    @_get_port.setter
    def _set_port(self, port):
        try:
            if not port:
                raise "[Err] cannot accept empty param : {}".format(port)
            elif not isinstance(port, int):
                raise "[Err] cannot accept param type : {}".format(type(port))
            else:
                self._port = port
        except Exception as e:
            raise e
# EOF #