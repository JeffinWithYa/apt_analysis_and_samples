#!/usr/bin/python

# Pulls samples from MalwareBazaar for Jupyter malware

import requests
import json
import argparse
import os
import pyzipper
from pathlib import Path

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Pull samples from MalwareBazaar by specifying a tag and the number of samples to download. If no number is specified, the default of 50 samples will be used."
)
parser.add_argument("tag", help="Specify the tag used on MalwareBazaar to identify the malware to download.")
parser.add_argument("--limit", "-l", default="50", type=int, help="Specify the maximum number of samples to pull. Default is 50.")
parser.add_argument("--sample_directory", "-s", default=".", help="Specify a directory for saving the samples. Defaults to current directory.")
parser.add_argument("--unzip", "-u", help="Specify a directory for saving unzipped samples. Defaults to creating a directory named 'Unzipped'.")
parser.add_argument("--password", "-p", default="infected", help="Specify a password for unzipping files. Default is 'infected'.")
parser.add_argument("--prefix", "-x", help="Optional prefix to add to the filename (e.g., 'APT28').")
args = parser.parse_args()

# Make request to MalwareBazaar API
query = {"query": "get_taginfo", "tag": args.tag, "limit": args.limit}
dataRequest = requests.post("https://mb-api.abuse.ch/api/v1/", data=query)

# Raise an error if the request fails
dataRequest.raise_for_status()

# Convert API response to Python dictionary
jsonPythonValue = json.loads(dataRequest.text)

# Save the current working directory
cwd = os.getcwd()

# Create the sample directory if it does not exist, and switch to it
if args.sample_directory:
    os.makedirs(args.sample_directory, exist_ok=True)
    os.chdir(args.sample_directory)

# Loop through the results and download each sample
resultsSHA = []
for i in range(len(jsonPythonValue["data"])):
    sha256_hash = jsonPythonValue["data"][i]["sha256_hash"]
    resultsSHA.append(sha256_hash)

    # Determine the filename with optional prefix
    if args.prefix:
        filename = f"{args.prefix}_{sha256_hash}.zip"
    else:
        filename = f"{sha256_hash}.zip"

    # Make request to download the file
    query = {"query": "get_file", "sha256_hash": sha256_hash}
    fileRequest = requests.post("https://mb-api.abuse.ch/api/v1/", data=query)

    # Save the file with the determined filename
    with open(filename, "wb") as file:
        file.write(fileRequest.content)

# If --unzip option is provided, unzip the downloaded files
if args.unzip:
    # Switch back to the original directory if necessary
    if os.getcwd() != cwd:
        os.chdir(cwd)

    # Create the unzip directory if it doesn't exist
    os.makedirs(args.unzip, exist_ok=True)

    # Iterate over the downloaded ZIP files and extract them
    for zippedfile in os.listdir(args.sample_directory):
        if zippedfile.endswith(".zip"):
            zip_path = os.path.join(args.sample_directory, zippedfile)
            with pyzipper.AESZipFile(zip_path, 'r') as zf:
                zf.pwd = bytes(args.password, "UTF-8")
                zf.extractall(args.unzip)
