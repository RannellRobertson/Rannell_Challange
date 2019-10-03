from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from ssl import wrap_socket


context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain("/path/to/certchain.pem")

with TCPServer(("server_address", 443), SimpleHTTPRequestHandler) as httpd:
    print("Serving at port 443")
    httpd.socket = context.wrap_socket(http.socket, certfile="/path/to/certs_and_keys.pem", server_side=True)
    httpd.serve_forever()
