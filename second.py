"""Classify a YouTube title as educational or not."""
import json, os
os.environ.update(HF_HUB_OFFLINE='1', TRANSFORMERS_OFFLINE='1')
import torch, laya
from download_model import MODEL_DIR

torch.set_num_threads(3)
agent = laya.load(str(MODEL_DIR), device='cpu')

questions = {
    'educational': {
        'type': 'noul',
        'instructions': 'Does this YouTube title indicate educational/informative content (teaches a skill, explains a concept, tutorial, lecture, documentary) as opposed to entertainment, vlog, music, gaming, or clickbait?',
    }
}

# title = "How Neural Networks Actually Work (Full Course)"
# title = "Ray Gunn | Official Trailer | Netflix"
# title = "Green Lantern is Atrociously Goated"
# title = "Guy Gardner scenes in superman #superman #guygardner #lanterns #greenlantern #dcu"
title = "On set for Rouge Dior with Jenna Ortega"

result = agent.predict(title, questions)
print(json.dumps(result['answers']['educational'], indent=2))