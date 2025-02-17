## running the python virtual env
Windows: `source .venv/Scripts/activate` or Mac: `source .venv/bin/activate`

## Install dependencies
- `pip install requests beautifulsoup4 pandas sqlalchemy apscheduler`
- `pip install pymysql`
- `pip install mysql-connector-python`

### problem with sqlalchemy and pandas
- got error 

        pandas/io/sql.py", line 1147, in __init__ meta = MetaData(self.connectable, schema=schema) TypeError: __init__() got multiple values for argument 'schema'

- had to downgrade mysqlalchemy on mac to `pip install sqlalchemy==1.4.45`
    - works with sqlalchemy 2.0.38 on windows

## error with mac 
- llib3/__init__.py", line 42, in <module>
    "urllib3 v2.0 only supports OpenSSL 1.1.1+, currently "
    ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.1.
    - had to run `pip install urllib3==1.26.6`
    - [Stack Overflow for urlib3](https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modu)

## directory structure in txt
        server/
            |── weather_scraper
            │   ── config.py
            │── db/
            │   │── weather_scraper_db/
            │       │── create_weather_table.py 