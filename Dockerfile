FROM snakepacker/python:all as builder

RUN python3.8 -m venv /usr/share/python3/app
RUN /usr/share/python3/app/bin/pip install -U pip

COPY requirements.txt /mnt/
RUN /usr/share/python3/app/bin/pip install -Ur /mnt/requirements.txt

COPY dist/ /mnt/dist/
RUN /usr/share/python3/app/bin/pip install /mnt/dist/* && /usr/share/python3/app/bin/pip check

FROM snakepacker/python:3.8 as api

COPY sh_start_point.sh ./
COPY --from=builder /usr/share/python3/app /usr/share/python3/app

RUN ln -snf /usr/share/python3/app/bin/CatalanNumber /usr/local/bin/ && \
	ln -snf /usr/share/python3/app/bin/gunicorn /usr/local/bin/

USER 1002:33
CMD bash ./sh_start_point.sh