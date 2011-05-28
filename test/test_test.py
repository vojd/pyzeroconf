from zeroconf import dns as r
from zeroconf import mdns
from unittest import TestCase
import struct


class TestFramework(TestCase):

    def test_launch_and_close(self):
        rv = mdns.Zeroconf()
        rv.close()

class TestPacket(TestCase):
    
    def test_transaction_id(self):
        # ID must be zero in a DNS-SD packet
        generated = r.DNSOutgoing(r._FLAGS_QR_QUERY)
        b = generated.packet().decode()
        id = ord(b[0]) << 8 | ord(b[1])
        self.assertEqual(id, 0)

    def test_query_header_bits(self):
        generated = r.DNSOutgoing(r._FLAGS_QR_QUERY)
        b = generated.packet().decode()
        flags = ord(b[2]) << 8 | ord(b[3])
        self.assertEqual(flags, 0x0)

    def test_response_header_bits(self):
        generated = r.DNSOutgoing(r._FLAGS_QR_RESPONSE)
        b= generated.packet()
        print("bytes", b)
        #flags = ord(b[2]) << 8 | ord(b[3])
        #self.assertEqual(flags, 0x8000)