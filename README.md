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

<b>W</b>e'd like to know the model which will perform best on the given dataset. To this objective, our solution is to assemble five pre-trained Huggingface models and:
* Train each model on the same data and collect their respective performance metrics
* Optimize each model using [Optuna](https://dl.acm.org/doi/10.1145/3292500.3330701)
* Use each optimized model's [state dictionary](https://pytorch.org/tutorials/recipes/recipes/what_is_state_dict.html) in a [new model](https://discuss.pytorch.org/t/combining-trained-models-in-pytorch/28383) that outputs a (6, 9) tensor, where each row is a probability distribution estimating the predicted class for a given category.
