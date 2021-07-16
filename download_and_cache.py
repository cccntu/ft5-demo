from huggingface_hub import snapshot_download
snapshot_download('flax-community/ft5-cnn-dm', revision='859350e337148108b32b6f9eef45d0d4c6b668a9', cache_dir='.')
