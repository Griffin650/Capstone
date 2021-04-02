# Reference for using cron
# https://pypi.org/project/django-crontab/
# https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/
from models import populate


def get_amazon_gpus():
    print('get_amazon_gpus cron job running')
    exec('./../manage.py update')
    populate()
