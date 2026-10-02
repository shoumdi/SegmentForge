FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt \
    && mkdir -p /artifacts /data /scripts

EXPOSE 8501

CMD ["streamlit","run","app.py"]