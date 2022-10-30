FROM ubuntu:latest

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y tk-dev python3-tk python3 python3-pip xvfb ghostscript inkscape 


COPY . turtlethread
RUN cd turtlethread && pip3 install -e .[dev,docs] && cd ..

ENV DISPLAY=:12

CMD Xvfb $DISPLAY -screen 0 1920x1080x24 2>/tmp/Xvfb.log & sleep 1 && bash
