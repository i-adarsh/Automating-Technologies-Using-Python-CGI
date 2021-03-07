#!/usr/bin/python3 

print('content-type: text/html')
print()

import header

header.header()

print(''' <div class="row">
                <!-- ***** Testimonials Item Start ***** -->
                <div class="col-lg-12 col-md-12 col-sm-12">
                    <div class="team-item">
                        <div class="team-content">
                            <i><img src="assets/images/resize_64.png" alt=""></i>
                            <div class="pricing-header">
                                <i><img src="http://'''+ header.ip() +'''/assets/images/apache-hadoop-logo-361D6613CB-seeklogo.com.png" alt=""></i>
                                <br />
                                <br />
                                <h3 class="pricing-title" align="center">Command &nbsp; Output</h3>
                                <br />
                            </div>''')

import subprocess
import cgi, os
import cgitb; cgitb.enable()   

form = cgi.FieldStorage()
fileitem = form['filename']

ip = " "
password = " "
path = " "

ip = form.getvalue('ipaddr')
password = form.getvalue('pass')

if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
#    fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   path = '/tmp/' + fn
   message = 'The file "' + fn + '" was uploaded successfully'
 
else:
   message = 'No any file is uploaded'
 

if password == None:
    password = "Not Entered"

output = '''
IP Address : '''+ ip +'''
Password : '''+ password +'''
Path : '''+ path +'''
'''

output = message + "\n\n" + output

print("<br /><div class='col-lg-12'><pre style='border:grey; border-width:1px; border-style:solid; padding: 20px;' >")

print(output +"&#160;</pre></div><br/><br />")
print('<br/>')

header.footer("hadoop")