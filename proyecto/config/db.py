from config.datosPersonales import *

MYSQL = {
  'default':{
  'ENGINE':'django.db.backends.mysql',
  'NAME':'django_proyecto', #nombre de la base de datos
  'USER':databaseAzure['user'],
  'PASSWORD':databaseAzure['password'],
  'HOST':databaseAzure['host'], #servidor local o también puede ser 'localhost'
  'PORT':'3306'
  }
}
