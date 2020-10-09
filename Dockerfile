# Dockerfile for testing.

FROM python:3.7-slim-stretch

# Set environment variables.

ENV HOME /longest_word

# Define working directory.
WORKDIR /longest_word
RUN pip3 install --upgrade pip
ADD . longest_word
ADD unittests /

# add entrypoint to docker
ENTRYPOINT ["python"]
CMD ["file_parser.py"]




