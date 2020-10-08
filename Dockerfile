# Dockerfile for testing / delivering ea_test_player_unified repo.

# Pull base image.

FROM python:3.7-slim-stretch

# Install.

# Set environment variables.
ENV HOME /file_words

# Define working directory.
WORKDIR /file_words
RUN pip3 install --upgrade pip
ADD file_paeser .

CMD ["common/file_parser.py"]
CMD bash


