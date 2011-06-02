from zeroconf import dns as r
from zeroconf import mdns
from unittest import TestCase
import struct


class TestFramework(TestCase):

    def test_launch_and_close(self):
        rv = mdns.Zeroconf()
        rv.close()



class TestPacketGeneration(TestCase):
    
    def testParseOwnPacketSimple(self):
        generated = r.DNSOutgoing(0)
        parsed = r.DNSIncoming(generated.packet())
        print("parsed %s " % parsed)
        self.assertEqual(type(parsed), r.DNSIncoming)

    def testParseOwnPacketSimpleUnicast(self):
        generated = r.DNSOutgoing(0, 0)
        parsed = r.DNSIncoming(generated.packet())
        print("parsed %s " % parsed)
        self.assertEqual(type(parsed), r.DNSIncoming)
    
    def testParseOwnPacketFlags(self):
        generated = r.DNSOutgoing(r._FLAGS_QR_QUERY)
        parsed = r.DNSIncoming(generated.packet())
        print("parsed %s " % parsed)

    def testParseOwnPacketQuestion(self):
        generated = r.DNSOutgoing(r._FLAGS_QR_QUERY)
        generated.addQuestion(r.DNSQuestion("testname.local.", r._TYPE_SRV, r._CLASS_IN))
        parsed = r.DNSIncoming(generated.packet())
        print("parsed questions %s " % parsed.questions)

    def testMatchQuestion(self):
        generated = r.DNSOutgoing(r._FLAGS_QR_QUERY)
        question = r.DNSQuestion("testname.local.", r._TYPE_SRV, r._CLASS_IN)
        generated.addQuestion(question)
        parsed = r.DNSIncoming(generated.packet())
        print("parsed", dir(parsed))
        print("generated.questions %s " % generated.questions)
        print("parsed.questions %s " % parsed.questions)
        self.assertEqual(len(generated.questions), 1)
        self.assertEqual(len(generated.questions), len(parsed.questions))
        self.assertEqual(question, parsed.questions[0])



class TestPacketForm(TestCase):
    
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
        b = generated.packet()
        print("bytes", b)
        #flags = ord(b[2]) << 8 | ord(b[3])
        flags = b[2] << 8 | b[3]
        self.assertEqual(flags, 0x8000)
        
        
        
        
        