from http.server import BaseHTTPRequestHandler, HTTPServer 
import time 
import json
from socketserver import ThreadingMixIn
import threading

hostName = "0.0.0.0"
serverPort = 80

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            content = open("index.html", "r").read() 
            self.wfile.write(bytes(content, "utf-8"))
        else:
            self.send_response("404")
            
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread"""
    
if __name__ == '__main__':
        server = ThreadedHTTPServer((hostName, serverPort), Handler)
        print(time.asctime(), "Server Starts - %s:%s" % (hostName, serverPort))
              
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
    
server.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, serverPort))
        

