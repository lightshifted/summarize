### Virtual environment

```bash
python -m venv venv
& venv/scripts/activate
python -m pip install pip setuptools wheel
python -m pip install -e .
```

## Install PyTorch
```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
```

### Objectives 
Our objective is to employ a text classification model into production...