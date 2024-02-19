FROM python:3.11

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ['python', '-m', 'src.app.main']
