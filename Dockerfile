# Dockerfile for testing.

FROM python:3.7-slim-stretch
ENV HOME /longest_word


# Set environment variables.
ADD . /longest_word

ENV HOME /longest_word

# Define working directory.
WORKDIR /longest_word
RUN pip3 install --upgrade pip

# add entrypoint to docker
#ENTRYPOINT ["python"]
CMD ["file_parser.py"]





