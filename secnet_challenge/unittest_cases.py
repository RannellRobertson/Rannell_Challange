from unittest import TestCase
import requests
import ssl
import socket


class SecNetTestCase(TestCase):
    def setUp(self):
        server_address = "127.0.0.1"
        port = 443
    
    def test_get_200_response(self):
        resp = requests.get(server_address)
        self.assertEqual(resp.status_code. 200)
        
        
    def test_get_ssl_certificate(self):
        cert = ssl.get_server_certificate((server_address, port))
        self.assertNotEqual(cert, None)
        
    
    def test_server_configuration(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_address, port))
            s.sendall("PING!")
            data = s.recv(1024)
            self.assertNotEqual(data, None)
        
        
if __name__ == "__main__":
    main(verbosity=2)
