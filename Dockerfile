FROM python:3.10.8

COPY . /TestFast

COPY ./requirements.txt /TestFast/requirements.txt

WORKDIR /TestFast

RUN pip install -r requirements.txt

CMD ["uvicorn","main:app","--reload","--host=0.0.0.0","--port=8000"]