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

        docker run -it parser:0.0.1 python file_parser.py
        docker run -it parser:0.0.1 python -m unittest unittests/unittests.py
        docker run -it parser:0.0.1 python -m unittest
