# SP Cup 2026 – Audio Source Enhancement Submission

This repository contains our submission for the IEEE Signal Processing Cup 2026.
The task focuses on audio source enhancement using a DCCRN-Conformer model.

Two tasks are included:
- Task 1: Anechoic environment
- Task 2: Reverberant environment

MATLAB is used only as a wrapper to call Python inference and to generate
submission-ready .mat files.

--------------------------------------------------

REQUIREMENTS

MATLAB:
- MATLAB R2021a or newer
- Signal Processing Toolbox
- Audio Toolbox

Python:
- Python 3.9 or newer
- Recommended to use a virtual environment

Python packages required:

torch==2.1.0
torchaudio==2.1.0
numpy<2.0
scipy
soundfile
pystoi
torchmetrics==1.3.2
tqdm

--------------------------------------------------

REPOSITORY STRUCTURE

SP_CUP_SUBMISSION/
│
├── Resources/
│   ├── Dataset_Generation/
│   │   ├── split_librispeech_gender.m
│   │   ├── train_anechoic.mlx
│   │   ├── train_reverb.mlx
│   │   ├── test_anechoic.mlx
│   │   └── test_reverb.mlx
│   │
│   └── Model/
│       ├── inference_Conformer.py
│       ├── train_Conformer.py
│       ├── anechoic_Conformer.pth
│       └── reverb_Conformer.pth
│
├── Submission/
│   ├── Task1_Anechoic/
│   │   ├── target_signal.wav
│   │   ├── interference_signal1.wav
│   │   ├── mixture.wav
│   │   ├── meta.json
│   │   ├── process_Task1.m
│   │   └── Task1_Anechoic_5dB.mat
│   │
│   └── Task2_Reverb/
│       ├── target_signal.wav
│       ├── interference_signal1.wav
│       ├── mixture.wav
│       ├── rir.wav
│       ├── meta.json
│       ├── process_Task2.m
│       └── Task2_Reverberant_5dB.mat
│
└── README.md

--------------------------------------------------

INPUT FILES (PER TASK)

Each task folder must already contain:

- target_signal.wav       : clean target speech
- interference_signal1.wav: interference signal
- mixture.wav             : mixture at SIR = 0 dB, SNR = 5 dB
- meta.json               : contains target_angle

Example meta.json:
{
  "target_angle": 90
}

Task 2 only:
- rir.wav : room impulse response

--------------------------------------------------

HOW TO RUN

Task 1 – Anechoic:

Open MATLAB and run:
cd Submission/Task1_Anechoic
process_Task1

Outputs:
- processed_signal.wav
- Task1_Anechoic_5dB.mat

Task 2 – Reverberant:

Open MATLAB and run:
cd Submission/Task2_Reverb
process_Task2

Outputs:
- processed_signal.wav
- Task2_Reverberant_5dB.mat

--------------------------------------------------

NOTES

- Same filenames across tasks are intentional.
- Tasks are separated by folder structure.
- No training is performed during submission execution.
- .mat files contain all required signals for evaluation.

--------------------------------------------------

Thank you for reviewing our submission.
