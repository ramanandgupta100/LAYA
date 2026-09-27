# download_model.py
from pathlib import Path
from huggingface_hub import snapshot_download

MODEL_DIR = Path(
    snapshot_download(repo_id="convaiinnovations/laya")
)