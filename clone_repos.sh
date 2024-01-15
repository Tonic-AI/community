#!/bin/bash

# Define an array of repository URLs
REPO_URLS=(
    https://github.com/cg123/mergekit
    https://github.com/meta-introspector/time/
    https://github.com/meta-introspector/ai-ticket
    https://github.com/runpod/runpod-python
    https://github.com/facebookresearch/pytorchvideo    
)

# Directory where you want to clone the repositories
DEST_DIR="./"

# Check if destination directory exists, if not create it
if [ ! -d "$DEST_DIR" ]; then
    mkdir -p "$DEST_DIR"
fi

# Change to the destination directory
cd "$DEST_DIR"

# Loop through the repository URLs and clone each one
for url in "${REPO_URLS[@]}"; do
    echo "Cloning $url ..."
    git clone "$url"
done

echo "Cloning complete."
