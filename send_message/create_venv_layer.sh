#!/bin/bash
# Create a lambda layer .zip file that includes python dependencies
pip install -r requirements.txt -t ./python
zip -r venv_layer.zip python
rm -rf python