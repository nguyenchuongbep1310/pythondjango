# salehome
git clone https://github.com/nguyenchuongbep1310/pythondjango.git
virtualenv env --no-site-packages
source env/bin/activate
pip install -r requirements.txt
In setting.py, change:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'salehomedb',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

Create a new user with name: salehomedb in phAdmin(PostgrestSQL)

python manage.py migrate
python manage.py runserver

More:
create admin account

python manage.py createsuperuser
