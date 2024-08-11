FROM python:3.12.1-bookworm

ENV TURTLETHREAD_VENV=/turtlethread-venv
ENV DISPLAY=:12
RUN apt-get update -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y\
        xvfb \
        ghostscript \
        inkscape \
        git \
        vim \
    && python -m venv $TURTLETHREAD_VENV \
    && echo "if ! pidof Xvfb; then Xvfb $DISPLAY -screen 0 1920x1080x24 2>/tmp/Xvfb.log & fi" >> /root/.bashrc \
    && echo "test -z $VIRTUAL_ENV && source $TURTLETHREAD_VENV/bin/activate" >> /root/.bashrc

CMD Xvfb $DISPLAY -screen 0 1920x1080x24 2>/tmp/Xvfb.log & sleep 1 && bash