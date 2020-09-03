# Docker file for building pyrento.net from pelican SSG

# Docker build
# (cd support/ && docker build -t pyrento_net .)

# Docker run
# docker run -it --mount type=bind,source=${PWD},target=/pyrento_net  pyrento_net

FROM alpine

LABEL author="Dan Williams"
LABEL maintainer="dww@pyrento.net"

RUN apk add python3-dev bash
RUN mkdir /support
ADD requirements.txt /support
RUN pip3 install -r /support/requirements.txt
RUN adduser -u 1000 -D danw

USER danw

CMD pelican /pyrento_net/pyrento_site/content -o /pyrento_net/pyrento_site/output -s /pyrento_net/pyrento_site/pelicanconf.py
