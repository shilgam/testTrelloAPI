# repo https://github.com/grihabor/pytest.images
FROM grihabor/pytest:python3.7-alpine

WORKDIR /usr/src/

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . .
