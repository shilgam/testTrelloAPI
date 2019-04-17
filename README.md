# testTrelloAPI

Simple test framework for testing CRUD operations of RESTful API.

[![Build Status](https://travis-ci.com/shilgam/testTrelloAPI.svg?branch=master)](https://travis-ci.com/shilgam/testTrelloAPI)

## Prerequisites

Docker and docker-compose installed

## Usage

1. Clone the repo
1. Get your API key and secret from https://trello.com/app-key and save them into the `.env` file. So that your `.env` will look like this:

        API_KEY={your api key here}
        API_SECRET={your api secret here}

1. Build the Docker image:

        $ docker-compose build

1. Get remaining secrets by running script below:

        $ docker-compose run --rm app python trello/lib/get_trello_creds.py

     and by follow instructions.

1. Run the test suite:

        $ docker-compose up

1. Clean up containers after tests:

        $ docker-compose down
