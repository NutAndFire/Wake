import socket


class Wol(object):
    def __init__(self) -> None:
        # here you can change the broadcast address for the subnet you want to broadcast to
        self.broadcast = ['10.1.1.255']
        self.wol_port = 40000

    """
    You can use any ports, the ports below is what wireshark will decode from the network stack of that local machine. Best to use WOL 

    WINDOWS PORTS:
    7: ECHO
    9: DISCARD
    40000: WOL

    LINIX PORTS:
    7: ECHO
    9: WOL
    """

    def wol(self, mac_address):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        magic = b"\xff" * 6 + mac_address * 16
        for i in self.broadcast:
            s.sendto(magic, (i, self.wol_port))
        s.close


if __name__ == "__main__":
    Wol().wol(b"\xde\xad\xbe\xef\x20\x24")