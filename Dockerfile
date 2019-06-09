FROM python:3.7
COPY . /pyapitest/
WORKDIR /pyapitest/
RUN pip install -r requirements.txt
CMD ["pytest", "/pyapitest/src/tests", "--html=report.html", "--self-contained-html"]

