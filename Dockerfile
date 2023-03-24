FROM python:3 


WORKDIR /LOCADORA

COPY . .

RUN pip install --no-cache-dir -r requeriments.txt

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]