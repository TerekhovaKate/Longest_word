# Dockerfile for testing.

FROM python:3.7-slim-stretch

# Set environment variables.
ENV HOME /file_words

# Define working directory.
WORKDIR /file_words
RUN pip3 install --upgrade pip
ADD Longest_word .

# add entrypoint to docker
ENTRYPOINT ["python"]
CMD ["file_parser.py"]




