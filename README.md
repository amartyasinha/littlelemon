# Little Lemon Restaurant

A simple Django project to manage restraurant's table booking.

## Setup

1. Clone the project: `git clone https://github.com/amartyasinha/littlelemon.git`
2. Enter project dir: `cd littlelemon`
3. Setup and activate venv (optional): `python3 -m venv .venv; source .venv/bin/activate`
4. Install deps: `pip3 install -r requirements.txt`
5. Run server: `python3 manage.py runserver`

## API Endpoints

1. `/registration/`: Make a table reservation.
2. `/bookings/`: List all bookings.
3. `/bookings/<id>`: View/Modify specific <id> bookings.
