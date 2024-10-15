FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN pip install pip-tools && pip-compile && pip-sync

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg --no-install-recommends && \
    curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

RUN wget https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.100/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver-linux64.zip

RUN nohup chromedriver &

ENV IN_CONTAINER="True"

CMD ["pytest"]