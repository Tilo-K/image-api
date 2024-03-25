FROM python:3.12

RUN apt-get update -y
RUN apt-get install python3-opencv poppler-utils -y

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r ./requirements.txt

# run python program
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0" , "main:app"]
