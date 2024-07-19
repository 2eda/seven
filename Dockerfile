FROM gcc:latest

RUN apt-get update && apt-get install -y \
    libopencv-dev \
    libpcl-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

CMD ["make"]
