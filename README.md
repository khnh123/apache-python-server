# apache-python-server

#### Table of Contents
- [Quick Start for Windows, either 32-bit or 64-bit](#headers)  
   - To install Apache Server
   - To install Python and run through Apache Server 
   - To run a Flask application using Apache module "mod_wsgi" 
- Full installation for Windows, either 32-bit or 64-bit
   - To install Apache Server
   - To install Python and run through Apache Server 
   - To run a Flask application using Apache module "mod_wsgi" 
- Quick Start for Linux, either 32-bit or 64-bit
- Full installation for Linux, either 32-bit or 64-bit

## Quick Start for Windows, either 32-bit or 64-bit <a name="headers"/>
Note this will install a 32-bit version of Apache, if you'd like a 64-bit version, please see the next section below.  Also note, if you have issues making the below instructions work, you may want to try the Full Installation method below.

Also note, this has only been tested on Windows Server 2012, but should work on Windows 10 and other Windows versions.

### To install Apache Server
1. Unzip Git file `/Windows/Apache24.zip` to your `C:\` directory
1. Open command prompt, run the following:
   1. `"C:\Apache24\bin\httpd.exe" -k start`
1. Open browser, go to http://localhost:82
1. You should see a page saying "Hello from Apache Server!"
1. Extras
   1. To debug, look at logs in your `C:\Apache24\logs` directory
   1. To restart the Apache server after you've made a change, run the following command:
      1. `"C:\Apache24\bin\httpd.exe" -k restart`
   1. To stop the Apache server, run the following command:
      1. `"C:\Apache24\bin\httpd.exe" -k stop`
   1. To install Apache, meaning it will be added as an automatically starting Windows service, run the following command in an Admin command prompt:
      1. `"C:\Apache24\bin\httpd.exe" -k install`

### To install Python and run through Apache Server 
1. Install a 32-bit version of [Python](https://www.python.org/downloads/), I used version 3.7, but other versions should work as well. Make sure to map to PATH variables in installation
1. Edit the top line of file `C:\Apache24\htdocs\testcgi.py` to your Python installation directory, for example for me it was:
   1. `#!C:\Program Files (x86)\Python37-32\python.exe`
1. Restart Apache, then go to http://localhost:80/testcgi.py and you should see a page saying "Hello from Python!"

### To run a Flask application using Apache module "mod_wsgi" 
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
1. Install these Python packages that are being used by this test website, by running command prompt commands:
   1. `pip install flask`
   1. `pip install numpy`
   1. `pip install pandas`
   1. `pip install plotly`
1. Restart Apache, then go to http://localhost:82/ and you should see a page saying "Welcome to the Flask application!"

## Full installation for Windows, either 32-bit or 64-bit
Note, this has only been tested on Windows Server 2012, but should work on Windows 10 and other Windows versions.

### To install Apache Server 
1. Download Apache server from Git directory `/Windows/full_installation/httpd-2.4.35-win32-VC15.zip` or from https://httpd.apache.org/docs/2.4/platform/windows.html
1. Unzip contents into `C:\Apache24` directory such that the `htdocs` directory is located here: `C:\Apache24\htdocs`
1. Open command prompt, run the following:
   1. `"C:\Apache24\bin\httpd.exe" -k start`
1. Open browser, go to http://localhost:80
1. You should see a page saying "It works!"
1. Extras
   1. To debug, look at logs in your `C:\Apache24\logs` directory
   1. A common issue here is that port 80 is already being used.  Running `netstat -an` in the command prompt will tell you what ports are in use. You may want to try changing the `Listen 80` port in file `C:\Apache24\conf\httpd.conf` to something else
   1. To restart the Apache server after you've made a change, run the following command:
      1. `"C:\Apache24\bin\httpd.exe" -k restart`
   1. To stop the Apache server, run the following command:
      1. `"C:\Apache24\bin\httpd.exe" -k stop`
   1. To install Apache, meaning it will be added as an automatically starting Windows service, run the following command in an Admin command prompt:
      1. `"C:\Apache24\bin\httpd.exe" -k install`

### To install Python and run through Apache Server 
1. Install a 32-bit version of [Python](https://www.python.org/downloads/), I used version 3.7, but other versions should work as well. Make sure to map to PATH variables in the installation
1. Copy Git file `/Windows/full_installation/testcgi.py` to `C:\Apache24\htdocs\`. Edit the top line of file to your Python installation directory, for example for me it was:
   1. `#!C:\Program Files (x86)\Python37-32\python.exe`
1. Edit file `C:\Apache24\conf\httpd.conf`
   1. Find this line: `Options Indexes FollowSymLinks` and replace it with this: `Options Indexes FollowSymLinks ExecCGI` 
   1. Find this line: `#AddHandler cgi-script .cgi` and replace it with this: `AddHandler cgi-script .cgi .py`
1. Restart Apache, then go to http://localhost:82/testcgi.py and you should see a page saying "Hello from Python!"

### To run a Flask application using Apache module "mod_wsgi" 
1. Copy Git files `/Windows/full_installation/htdocs_wsgi/app.py` and `/Windows/full_installation/htdocs_wsgi/web.wsgi` to your directory `C:\Apache24\htdocs_wsgi\` 
1. Open an Administrator command prompt, and navigate to folder `C:\Apache24\modules`
1. Run command `pip install mod_wsgi` then run command `mod_wsgi-express module-config` which will create a module file in this directory.  For me this was named `mod_wsgi.pyd` and its contents will depend on your Windows/Python versions.
1. Open `C:\Apache24\conf\httpd.conf` in a text editor.  Add the following code underneath the line with text `Listen 80`
    
    ```
    <VirtualHost localhost:80>
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
1. Install this Python package that is being used by this test website, by running command:
   1. `pip install flask`
1. Restart Apache, then go to http://localhost:80/ and you should see a page saying "Hello from Flask!"
1. If you'd like to test a fully formatted example website, do the following:
   1. Delete contents of `C:\Apache24\htdocs_wsgi` and copy in contents of Git directory `/Windows/Apache24/htdocs_wsgi`
   1. Install these Python packages, by running command prompt commands:
         1. `pip install numpy`
         1. `pip install pandas`
         1. `pip install plotly`
1. Restart Apache, then go to http://localhost:80/ and you should see a sample webpage

## Quick Start for Linux , either 32-bit or 64-bit

Coming soon!

## Full installation for Linux, either 32-bit or 64-bit

Coming soon!
