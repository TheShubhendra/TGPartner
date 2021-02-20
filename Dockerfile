FROM python:3.9
WORKDIR app/
RUN apt-get install -y git
RUN git clone https://github.com/TheShubhendra/TGPartner .
RUN pip install -r requirements.txt
CMD [ "python" ,"-m" ,"tgpartner" ]
