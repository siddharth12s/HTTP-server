import http.server
import time
import json
import uuid

class Server(http.server.BaseHTTPRequestHandler):

    
    def do_GET(self):
        path_parts = self.path.split('/')
        if self.path == '/html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = ""
            with open('first.html', 'r') as file:
                html_content = file.read()
            
            self.wfile.write(html_content.encode())
            
            
        elif self.path == '/json':
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            with open('first.json', 'rb') as page:
                self.wfile.write(page.read())  
        
        elif self.path == '/uuid':
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            uuid_content = {
                "uuid": str(uuid.uuid4())
            }
            json_res = json.dumps(uuid_content).encode('utf-8')
            self.wfile.write(json_res)
        
        elif len(path_parts) >=3 and path_parts[1]=='status':
                statusCode = int(path_parts[2])
                self.send_response(statusCode)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"Response with status code: {statusCode}".encode())
         
        elif len(path_parts) >=3 and path_parts[1] == 'delay':
            try:
                delay_seconds = int(path_parts[2])
                time.sleep(delay_seconds)  
                self.send_response(200)
                self.send_header('Content-type', "text/json")
                self.end_headers()
                self.wfile.write(f"Time delayed was {delay_seconds} seconds".encode())     
            except:
                self.send_res  
        else:
            self.send_response(404);
            self.end_headers();
    


PORT =9000

my_server = http.server.HTTPServer(('localhost', PORT), Server)
try:
    # Serve indefinitely until interrupted
    print("Server running on http://localhost/9000")
    my_server.serve_forever()
except KeyboardInterrupt:
    # Close the server when interrupted by Ctrl+C
    my_server.server_close()
    print("Server closed")