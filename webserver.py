#Copyright Jon Berg , turtlemeat.com

import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import commands
import os

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path == "/senseo/action/1cup.run":
                print 'Activation de la senseo '
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write('Coucou')
                os.system("python /home/pi/senseo/senseo.py 1cup")
                return
            if self.path == "/senseo/action/2cup.run":
                print 'Activation de la senseo '
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write('Coucou')
                os.system("python /home/pi/senseo/senseo.py 2cup")
                return
            if self.path == "/senseo/action/4cup.run":
                print 'Activation de la senseo '
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write('Coucou')
                os.system("python /home/pi/senseo/senseo.py 4cup")
                return
            if self.path == "/senseo/action/getStatus":
                print 'Recuperation du statuts de la Senseo'
                status, text = commands.getstatusoutput('python /home/pi/senseo/senseo.py status')
                stu = text[text.find('La senseo'):]
                print ' Senseo : {}'.format(stu)
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write(stu)
                return
                
            return
                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
     

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass

def main():
    try:
        server = HTTPServer(('', 8001), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()

