'''
/django_api/user/apps.py
-------------------------
Entrance of the User  
'''


from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
