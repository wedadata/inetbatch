from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class Code(BaseHTTPRequestHandler):
    def do_GET(self):
        rawparams = self.path.split('?')

        if len(rawparams) > 1:
            params = dict(item.split('=') for item in rawparams[1].split('&'))

            arg = params.get('arg')

            shellcommand = f'app.bat %s' % arg
            responce = subprocess.getoutput(shellcommand).encode()
        else:
            shellcommand = f'app.bat'
            responce = subprocess.getoutput(shellcommand).encode()
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(responce)

with HTTPServer(('localhost', 80), Code) as server:
    server.serve_forever
