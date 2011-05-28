""" Multicast DNS Service Discovery for Python, v0.12
    Copyright (C) 2003, Paul Scott-Murphy

    This module provides a unit test suite for the Multicast DNS
    Service Discovery for Python module.

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

"""

__author__ = "Paul Scott-Murphy"
__email__ = "paul at scott dash murphy dot com"
__version__ = "0.12"

from zeroconf import dns as r
from zeroconf import mdns
import unittest

class PacketGeneration(unittest.TestCase):
    
    pass

    """
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
    
    """
    #===========================================================================
    # 
    # def testJoin(self):
    #    """
    #        l is a copy of a list from self.data obtained from the dns.packet() method
    #        causes an xmlrpc.client.Fault invalid character 0x0
    #    """
    #    
    #    l = [b'\x00\x00', b'\x00\x00', b'\x00\x00', b'\x00\x00', b'\x00\x00', b'\x00\x00']
    #    #l = [b'\x00\x00', b'\x84\x00', '\x00\x00', '\x00\x04', '\x00\x00', '\x00\x00', '\x05', '_http', '\x04', '_tcp', '\x05', 'local', '\x00', '\x00\x0c', '\x00\x01', '\x00\x00\x0e\x10', '\x00"', '\x0f', 'My Service Name', '\x05', '_http', '\x04', '_tcp', '\x05', 'local', '\x00', '\xc0', '(', '\x00!', '\x00\x01', '\x00\x00\x0e\x10', '\x00\x08', '\x00\x00', '\x00\x00', '\x04\xd2', '\xc0', '(', '\xc0', '(', '\x00\x10', '\x00\x01', '\x00\x00\x0e\x10', '\x00*', '\x0ca=test value\x0cversion=0.10\x0fb=another value', '\xc0', '(', '\x00\x01', '\x00\x01', '\x00\x00\x0e\x10', '\x00\x04', "\xd5r\xa7'"] 
    #    print("l", l)
    #    ff = ''.join(s.decode('utf-8', 'ignore') for s in l)
    #    print("ff", ff)
    # 
    #===========================================================================
        
 
class PacketForm(unittest.TestCase):

    def testTransactionID(self):
        # ID must be zero in a DNS-SD packet
        generated = r.DNSOutgoing(r._FLAGS_QR_QUERY)
        bytes = generated.packet()
        id = ord(bytes[0]) << 8 | ord(bytes[1])
        self.assertEqual(id, 0)
        
    def testQueryHeaderBits(self):
        generated = r.DNSOutgoing(r._FLAGS_QR_QUERY)
        bytes = generated.packet()
        flags = ord(bytes[2]) << 8 | ord(bytes[3])
        self.assertEqual(flags, 0x0)
    
    def testResponseHeaderBits(self):
        generated = r.DNSOutgoing(r._FLAGS_QR_RESPONSE)
        bytes = generated.packet()
        print("bytes", bytes.encode())
        flags = ord(bytes[2].encode()) << 8 | ord(bytes[3].encode())
        print("flags " , flags)
        self.assertEqual(flags, 0x8000)
        
        
        
class Framework(unittest.TestCase):

    def testLaunchAndClose(self):
        rv = mdns.Zeroconf()
        rv.close()

if __name__ == '__main__':
    
    unittest.main()
