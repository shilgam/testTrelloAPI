# testTrelloAPI

Simple test framework for testing CRUD operations of RESTful API.

## Prerequisites

Docker and docker-compose installed

## Usage

1. Clone the repo
1. Get your API key and secret from https://trello.com/app-key and save them into the `.env` file. So that your `.env` will look like this:

        API_KEY={your api key here}
        API_SECRET={your api secret here}

1. Build the Docker image:

        $ docker-compose build

1. Get remaining secrets (`request_token`, `request_token_secret`, `pin`) by running script and by following instructions:

        $ docker-compose run --rm app sh
        $ python lib/get_trello_creds.py

1. Add your received secrets into the `.env` file. So that after that `.env` file will look like this:

        API_KEY={your api key here}
        API_SECRET={your api secret here}
        REQUEST_TOKEN={your request_token here}
        REQUEST_TOKEN_SECRET={your request_token_secret here}
        PIN={your pin here}

1. Run the test suite:

        $ docker-compose up

1. Clean up containers after tests:

        $ docker-compose down
