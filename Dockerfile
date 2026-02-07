# Isticmaal image leh Python
FROM python:3.10-slim-buster

# Rakib agabka dhismaha (Compilers) iyo ffmpeg
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    git

# Samey galka shaqada
WORKDIR /app
COPY . .

# Cusboonaysii pip oo rakib requirements
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

# Shid bot-ka
CMD ["python3", "bot.py"]
