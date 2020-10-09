# Find the longest word in text file


#### Installation

Installation is done in two steps: clone from GitHub,
requires python 3.6 or python 3.7
Note: not compatible with 3.9

```bash
$ git clone https://github.com/TerekhovaKate/Longest_word.git

```

### QuickStart
run the  job with `file_parser.py`

example
  1. python3 file_parser.py (would use default file )

  2. python3 file_parser.py  --file <user unput>

|     option       |                will show...                     |
| ---------------  | ----------------------------------------------- |
| `--file`  | the user input  path to the .txt file                  |



## Additional Info
### Unit testing
python3 -m unittest unittests/unittests.py
### Docker
Option 2 - Docker Image: Python Interpreter running inside a Docker Image

build a Docker container

    docker build -t <tag_name>:<tag> .

example

    docker build -t parser:0.0.1 .

2.1 run test with docker container

    2.1.1 specify the input for  custom .txt file specify the input for  custom .txt file
    docker run -it -v /tmp:/tmp parser:0.0.1 python file_parser.py --file /tmp/<file from local /tmp>

    2.1.2. docker run will use default .txt insade the container
    docker run -it parser:0.0.1 python file_parser.py

    2.1.3. docker run for unit testing
    docker run -it parser:0.0.1 python -m unittest unittests/unittests.py

