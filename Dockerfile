FROM ubuntu:18.04

RUN apt update && \
    apt install -y bash \
                   build-essential \
                   git \
                   curl \
                   ca-certificates \
                   python3 \
                   python3-pip && \
    rm -rf /var/lib/apt/lists


WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

WORKDIR /code_dir/repo
RUN python3 -m pip install --no-cache-dir huggingface_hub
#COPY download_and_cache.py download_and_cache.py
#RUN python3 download_and_cache.py
COPY . .
ENV PORT 8080
CMD ["./run.sh"]
