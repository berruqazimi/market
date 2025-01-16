FROM python:3.10

WORKDIR /app

COPY requiremets.txt /app/

RUN pip install --no-cache-dir -r requiremets.txt

COPY . /app/


EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]