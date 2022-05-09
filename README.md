# data-farmer 👨‍🌾

## Requirements

You should have these installed:

- Python 3
- Docker

## Running locally

```shell
# fill out the env vars, for optional ones you can leave the value empty
cp .env.template .env
vim .env

# start the master
python main.py master start --help

# list plugins supported by the master
python main.py master list-plugins

# run an experiment
python main.py experiment start --help
```
