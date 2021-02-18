FROM python:3.9
WORKDIR app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY tgpartner ./tgpartner
CMD [ "apt-get", "install", "-y", "git"]
CMD [ "git", "init"]
CMD [ "git", "remote", "add", "upstream", "https://github.com/TheShubhendra/TGPartner"]
CMD [ "python" ,"-m" ,"tgpartner" ]
