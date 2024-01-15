#!/bin/bash

# Define an array of repository URLs
REPO_URLS=(
    https://github.com/intel/ai-workflows
    https://github.com/intel/ai-containers
    https://github.com/Clarifai/clarifai-python
    https://github.com/docker/compose
    https://github.com/huggingface/diffusers
    https://github.com/embedchain/embedchain
    https://github.com/deepset-ai/haystack
    https://github.com/KBVE/kbve
    https://github.com/logspace-ai/langflow
    https://github.com/run-llama/llama_index
    https://github.com/mistralai/client-python
    https://github.com/allenai/open-instruct
    https://github.com/KillianLucas/open-interpreter
    https://github.com/raidendotai/openv0
    https://github.com/huggingface/optimum
    https://github.com/replicate/replicate-python
    https://github.com/docker/scout-cli
    https://github.com/raidendotai/shell2-cli
    https://github.com/google-research/t5x
    https://github.com/togethercomputer/together-cli
    https://github.com/huggingface/transformers
    https://github.com/UKPLab/sentence-transformers
    https://github.com/vercel/vercel
    https://github.com/facebookresearch/xformers
    https://github.com/NVIDIA/nvidia-container-toolkit
    https://github.com/dusty-nv/jetson-containers
    https://github.com/e2b-dev/E2B
    https://github.com/FlowiseAI/Flowise
    https://github.com/cpacker/MemGPT
    https://github.com/QwenLM/Qwen-Agent
    https://github.com/microsoft/TaskWeaver
    https://github.com/langchain-ai/langchain
    https://github.com/microsoft/promptflow
    https://github.com/openai/openai-python
    https://github.com/chroma-core/chroma
    https://github.com/qdrant/qdrant
    https://github.com/streamlit/streamlit
    https://github.com/gradio-app/gradio
    https://github.com/openai/tiktoken
    https://github.com/google/sentencepiece
    https://github.com/TimDettmers/bitsandbytes    
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
