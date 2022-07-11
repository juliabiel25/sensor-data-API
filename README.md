# Instructions for running the API server 🚀

0. If using venv, activate it and install the required modules.

On Windows:

`[path to the venv folder]\Scripts\activate`

`pip install -r [path to the app\requirements.txt file]`

1. Go to the main repo folder and run command:

`uvicorn app.api:app`

or

`uvicorn app.api:app --reload`

for automatic server reload on change

2. View the GUI of the API under:
http://localhost:8000/docs
