#!-*-coding:utf-8-*-
# author: by yanan wang 2018/3/19 15:06
import os

DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'db5',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'',
        'PORT':'',

    }
}


TEMPLATE_DIR={
    os.path.join(BASE_DIR,'templates'),
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)