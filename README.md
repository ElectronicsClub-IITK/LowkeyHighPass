# 🎧 Lowkey HighPass Audio Demo

Interactive web demo for comparing audio beamforming methods and interference removal techniques.

## 📁 File Organization

```
LowkeyHighPass/
├── index.html                          # Main demo webpage
├── README.md                           
│
├── mixed_audio/                        # Input: Mixed signals
│   ├── male_female_mixture.flac
│   ├── male_male_mixture.flac
│   ├── male_water_mixture.flac
│   └── male_song_mixture.flac
│
├── output_audio/                       # Output: Processed signals
│   ├── neural_female.flac
│   ├── neural_male.flac
│   ├── neural_water.flac
│   ├── neural_song.flac
│   ├── two_channel_female.flac
│   ├── two_channel_male.flac
│   ├── two_channel_water.flac
│   ├── two_channel_song.flac
│   ├── nested_female.flac
│   ├── nested_male.flac
│   ├── nested_water.flac
│   └── nested_song.flac
│
└── interference/                       # Source interference files
    ├── interference_female_speech.flac
    ├── interference_male.flac
    ├── interference_water.wav
    └── interference_song.flac
```

## 📊 Performance Metrics

- **STOI**: Speech intelligibility (0-1, higher is better)
- **PESQ**: Speech quality (1-5, higher is better)
- **SNR**: Signal-to-noise ratio in dB (higher is better)
- **ViSQOL**: Perceived quality (1-5, higher is better)

## 🛠️ Technical Requirements

- **Audio Format**: FLAC
- **Browser Support**: Chrome 49+, Firefox 51+, Edge 16+

