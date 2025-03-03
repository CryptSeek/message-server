FROM python:3.11-bookworm
LABEL authors="CryptSeek"

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install app
COPY message-server ./message-server
COPY run_server.sh .

EXPOSE 9090
EXPOSE 5555

CMD ["bash", "run_server.sh"]