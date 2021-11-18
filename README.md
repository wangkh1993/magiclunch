# magiclunch
A python application gives your some lunch idea.

## Usage
Place input JSON files into `data` directory if you would like to run in Docker mode
Otherwise, run `main/main.py` and input JSON file as per hint

## Project Structure
```
magiclunch
├── data
│   ├── ingredients.json
│   └── recipes.json
├── Dockerfile
├── main
│   └── main.py
├── README.md
├── requirements.txt
├── test
│   └── unit
│       ├── test_input.py
│       ├── test_input1.json
│       ├── test_input2.json
│       ├── test_input3.json
│       └── __init__.py
```
## Files
`main.py`: application file, contains PickLunch class for producing correct recipe.
`requirements.txt`: python dependencies 
`test_input.py`: unittest 
`test_input.json`: sample input for unittest

## Running using Docker
Required Docker installed. Note, Docker Volume is not implemented, running docker mode requires input files to be pre-placed in the `data` directory, such that files can be copied into container.

Run below command to build image:

``` docker build -t picklunch:latest .```

Run below command to execute the container:

```docker run -ti picklunch python /magiclunch/main/main.py```

Run below command for unittest:

``` docker run -ti --rm picklunch python /magiclunch/test/unit/test_input.py```

## Running Using Local Python Env
Module was built using Python 3.7. Use `pip` to install dependencies
```pip install -r requirements.txt```

Firing up application:
``` python .\main\main.py```

