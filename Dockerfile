From seriallab/python3.6dev

COPY requirements.txt /opt/requirements.txt

RUN pip install -r /opt/requirements.txt

WORKDIR opt

COPY . /opt/


