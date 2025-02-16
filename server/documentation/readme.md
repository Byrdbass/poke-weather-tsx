## running the python virtual env
Windows: `source .venv/Scripts/activate` or Mac: `source .venv/bin/activate`

## Install dependencies
`pip install requests beautifulsoup4 pandas sqlalchemy apscheduler`

## error with mac 
- llib3/__init__.py", line 42, in <module>
    "urllib3 v2.0 only supports OpenSSL 1.1.1+, currently "
    ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.1.
    - had to run `pip install urllib3==1.26.6`
    - [Stack Overflow for urlib3](https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modu)

