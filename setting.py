DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'UsQuakes',
        'USER': 'forif@forif',
        'PASSWORD': 'rkdalswn1!',
        'HOST': 'forif.mysql.database.azure.com',
        'PORT': '3306',

        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
        },
    },
}

# set this to False if you want to turn off pyodbc's connection pooling
DATABASE_CONNECTION_POOLING = False