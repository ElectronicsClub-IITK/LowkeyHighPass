"""
Task 2 – Reverberant Room Simulation
Generates Task2_Reverberant_5dB.mat (SP Cup compliant)
"""

import os
import sys
import json
import torch
import torchaudio
import numpy as np
import scipy.io as sio

# ===============================
# PATH SETUP (DO NOT CHANGE)
# ===============================
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(THIS_DIR, ".."))

MODEL_DIR = os.path.join(ROOT_DIR, "SP_CUP_Phase_2", "Model Inference")
sys.path.append(MODEL_DIR)

from inference_Conformer import DCCRNConformer

# ===============================
# CONFIG
# ===============================
FS = 16000
DEVICE = "cpu"   # submission-safe
MODEL_PATH = os.path.join(MODEL_DIR, "reverb_Conformer.pth")
OUT_MAT = os.path.join(THIS_DIR, "Task2_Reverberant_5dB.mat")

# ===============================
# LOAD AUDIO FILES
# ===============================
def load_mono(fname):
    path = os.path.join(THIS_DIR, fname)
    x, sr = torchaudio.load(path)
    if sr != FS:
        x = torchaudio.functional.resample(x, sr, FS)
    return x[0].numpy()

target_signal = load_mono("target_signal.wav")
interference_signal = load_mono("interference_signal1.wav")

mixture, sr = torchaudio.load(os.path.join(THIS_DIR, "mixture.wav"))
if sr != FS:
    mixture = torchaudio.functional.resample(mixture, sr, FS)

# ensure stereo
if mixture.shape[0] == 1:
    mixture = mixture.repeat(2, 1)
elif mixture.shape[0] > 2:
    mixture = mixture[:2]

mixture_signal = mixture.numpy()

# ===============================
# LOAD RIR
# ===============================
rir, sr = torchaudio.load(os.path.join(THIS_DIR, "rir.wav"))
if sr != FS:
    rir = torchaudio.functional.resample(rir, sr, FS)

rir_data = rir.numpy()

# ===============================
# LOAD METADATA
# ===============================
with open(os.path.join(THIS_DIR, "meta.json"), "r") as f:
    meta = json.load(f)

target_angle = float(meta.get("target_angle", 0.0))

# ===============================
# MODEL INFERENCE
# ===============================
model = DCCRNConformer(n_fft=512, hop_length=128).to(DEVICE)
state = torch.load(MODEL_PATH, map_location=DEVICE)
model.load_state_dict(state)
model.eval()

mix_tensor = torch.tensor(mixture_signal).unsqueeze(0).to(DEVICE)
angle_tensor = torch.tensor([[target_angle]], dtype=torch.float32).to(DEVICE)

with torch.no_grad():
    processed = model(mix_tensor, angle_tensor)

processed_signal = processed.squeeze().cpu().numpy()

# save processed wav
torchaudio.save(
    os.path.join(THIS_DIR, "processed_signal.wav"),
    torch.tensor(processed_signal).unsqueeze(0),
    FS
)

# ===============================
# METRICS (PLACEHOLDERS – ALLOWED)
# ===============================
metrics = {
    "OSINR": np.nan,
    "PESQ": np.nan,
    "STOI": np.nan
}

# ===============================
# PARAMS
# ===============================
params = {
    "fs": FS,
    "SIR_dB": 0,
    "SNR_dB": 5,
    "RT60": 0.5,
    "target_angle": target_angle,
    "environment": "Reverberant"
}

# ===============================
# SAVE .MAT (STRICT FORMAT)
# ===============================
sio.savemat(
    OUT_MAT,
    {
        "target_signal": target_signal,
        "interference_signal": interference_signal,
        "mixture_signal": mixture_signal,
        "rir_data": rir_data,
        "processed_signal": processed_signal,
        "metrics": metrics,
        "params": params,
    },
)

print("===================================")
print("Task 2 Reverberant processing done.")
print(f"Saved: {OUT_MAT}")
print("===================================")
