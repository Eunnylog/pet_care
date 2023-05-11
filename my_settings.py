DATABASES = {
    'default' : {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'Scheme Name',
        'USER'    : 'User Name',
        'PASSWORD': 'Your Password',
        'HOST'    : 'localhost',
        'PORT'    : 'Database Server Port',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset'     : 'utf8mb4',
            'use_unicode' : True,
        },
    }
}

SECRET_KEY = {
    'secret'   :'django-insecure-^n14@6b+ql8=73=aelftddeb^vs4dbx&_)r4=0*@500d4nve9b',
    'algorithm':'HS256' 
}


EMAIL = {
    'EMAIL_BACKEND'      :'django.core.mail.backends.smtp.EmailBackend', 
    'EMAIL_USE_TLS'      : True,      
    'EMAIL_PORT'         : 587,                   
    'EMAIL_HOST'         : 'smtp.gmail.com',
    'EMAIL_HOST_USER'    : 'pretty981210@gmail.com',#pjm970128@gmail.com
    'EMAIL_HOST_PASSWORD': 'jgauvhtqadzwoiwq', 
    'SERVER_EMAIL'       : 'Gmail ID',
    'REDIRECT_PAGE'      : 'https://wave1994.tistory.com' 
}