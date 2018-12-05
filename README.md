# apache-python-server

This guide shows how to:
1. Get a working Apache server
1. Run Python scripts on this server
1. Set up a Flask application using module "mod_wsgi"

Quick Start for Windows, either 32-bit or 64-bit
-
Note this will install a 32-bit version of Apache, if you'd like a 64-bit version, please see the next section below.  Also note, if you have issues making the below instructions work, you may want to try the Full Installation method below.

#### To install Apache Server ####
1. Unzip `/working_windows_version/Apache24.zip` to your `C:\` directory
1. Open command prompt, run the following:
   1. `"C:\Apache24\bin\httpd.exe" -k start`
1. Open browser, go to http://localhost:82
1. You should see a page saying "Hello from Apache Server!", this means your Apache server is working
1. Extras
   1. To debug, look at logs in your `C:\Apache24\logs` directory
   1. To restart the Apache server after you've made a change, run the following command:
      1. `"C:\Apache24\bin\httpd.exe" -k restart`
   1. To stop the Apache server, run the following command:
      1. `"C:\Apache24\bin\httpd.exe" -k stop`
   1. To install Apache, meaning it will be added as an automatically starting Windows service, run the following command in an Admin command prompt:
      1. `"C:\Apache24\bin\httpd.exe" -k install`

#### To install Python and run through Apache Server ####
1. Install a 32-bit version of [Python](https://www.python.org/downloads/), I used version 3.7, but other versions should work as well
1. Edit the top line of file `C:\Apache24\htdocs\testcgi.py` to your Python installation directory, for example for me it was:
   1. `#!C:\Program Files (x86)\Python37-32\python.exe`
1. Go to http://localhost:82/testcgi.py and you should see a page saying "Hello from Python!"

#### To run a Flask application using Apache module "mod_wsgi" ####
1. Open `C:\Apache24\conf\httpd.conf` in a text editor.  Add the following code underneath the line with text `Listen localhost:82`
    
    ```
    <VirtualHost localhost:82>
    ServerAdmin domains@domain1.com
    WSGIScriptAlias / "C:/Apache24/htdocs_wsgi/web.wsgi"
    WSGIApplicationGroup %{GLOBAL}
    DocumentRoot C:/Apache24/htdocs_wsgi
    <Directory "C:/Apache24/htdocs_wsgi/">
    Options +Indexes +Includes +FollowSymLinks +MultiViews +ExecCGI
    Require all granted   
    </Directory>
    CustomLog C:/Apache24/logs/access.log common
    ErrorLog C:/Apache24/logs/error.log
    </VirtualHost>
    ```
1. Go to http://localhost:82/ and you should see a page saying "Welcome to the Flask application!"

Full Installation for any operating system
-

