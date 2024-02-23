while ! nc -z mysql_db 3306; do
  sleep 1
done

python manage.py migrate --noinput

python manage.py cron add

gunicorn MoC.wsgi:application -b 0.0.0.0:8000
