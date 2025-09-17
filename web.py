from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
  <title>TCP Protocol Explanation</title>
  <style>
    table {
      border-collapse: collapse;
      width: 80%;
      margin: 20px auto;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #333;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #4CAF50;
      color: white;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
    caption {
      font-size: 20px;
      margin: 10px;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <table>
    <caption>TCP Protocol Explanation</caption>
    <tr>
      <th>Feature</th>
      <th>Explanation</th>
    </tr>
    <tr>
      <td>Full Form</td>
      <td>Transmission Control Protocol</td>
    </tr>
    <tr>
      <td>Type</td>
      <td>Connection-oriented protocol</td>
    </tr>
    <tr>
      <td>Connection Setup</td>
      <td>Uses a 3-way handshake to establish a reliable connection before data transfer.</td>
    </tr>
    <tr>
      <td>Reliability</td>
      <td>Ensures reliable data delivery with error checking and retransmission of lost packets.</td>
    </tr>
    <tr>
      <td>Data Transfer</td>
      <td>Breaks data into segments, numbers them, and ensures they arrive in order.</td>
    </tr>
    <tr>
      <td>Flow Control</td>
      <td>Uses sliding window protocol to prevent sender from overwhelming receiver.</td>
    </tr>
    <tr>
      <td>Error Control</td>
      <td>Uses checksums to detect errors and acknowledgments (ACKs) for successful delivery.</td>
    </tr>
    <tr>
      <td>Applications</td>
      <td>Used in applications like HTTP, HTTPS, FTP, SMTP, and Telnet.</td>
    </tr>
    <tr>
      <td>Port Numbers</td>
      <td>Uses port numbers (e.g., HTTP – 80, HTTPS – 443, FTP – 21).</td>
    </tr>
  </table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()