from http.server import HTTPServer

from server import Server

HOST = '0.0.0.0'
PORT = 8000

if __name__ == '__main__':
    server = HTTPServer((HOST, PORT), Server)
    print('Up: %s:%s' % (HOST, PORT))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
