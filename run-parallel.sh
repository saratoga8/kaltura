#!/bin/bash

echo -e "\nInstall Python version ---------------------------------"
pyenv install

echo -e "\nInstall virtual environment ----------------------------"
python -m venv .venv

echo -e "\nActivate virtual environment ---------------------------"
source .venv/bin/activate

echo -e "\nInstall dependencies -----------------------------------"
pip install -r requirements.txt

echo -e "\nRunning tests ------------------------------------------"
export HEADLESS=True && pytest -n auto