## Python WebAPI
Python WebApi with IBM i DB

This demo show how to set up an web service server (WebAPI) based on python

This WebAPI can run on Linux, Windows and IBM i.<br/>
You only need an ODBC driver on your machine.

So, you can develop the WebAPI on your local computer.<br/>
When you have finished your work, you can deploy it on your IBM i without changing your code (if you have a clean environment :eyes: ).

## Setup your WebAPI

1. Requirements
   * Install ODBC driver
     
     ```sh
     -bash-5.1$ yum install python39 python39-devel unixODBC python39-pyodbc python39-wheel python39-six python39-setuptools python39-pandas
     ```
     You can check your ODBC settings using the `odbcinst` command

     ```sh
     -bash-5.1$ odbcinst -j
     unixODBC 2.3.9
     DRIVERS............: /QOpenSys/etc/odbcinst.ini
     SYSTEM DATA SOURCES: /QOpenSys/etc/odbc.ini
     FILE DATA SOURCES..: /QOpenSys/etc/ODBCDataSources
     USER DATA SOURCES..: /home/PROUZA/.odbc.ini
     SQLULEN Size.......: 8
     SQLLEN Size........: 8
     SQLSETPOSIROW Size.: 8
     ```

2. Go into your directory
    
    This is the directory where your `requirements.txt` file is stored.

    ```sh
    -bash-5.1$ cd python-webapi/webapi
    ```
3. Create a virtual environment
    
    ```sh
    -bash-5.1$ python -m venv --system-site-packages ./venv
    ```

4. Activate your virtual environment
    
    ```sh
    -bash-5.1$ source venv/bin/activate
    ```

5. Upgrade your PIP first (recommended)
    
    ```sh
    (venv) -bash-5.1$ pip install --upgrade pip
    ```

6. Install Python required packages
    
    ```sh
    (venv) -bash-5.1$ pip install -r requirements.txt
    ```

7. Run the WebService
    
    ```sh
    (venv) -bash-5.1$ python webapi.py
    ```