FROM python:3.12

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r ./requirements.txt

# run python program
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0" , "main:app"]
