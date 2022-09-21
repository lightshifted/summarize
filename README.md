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

### Objective 
Our objective is to employ a text classification model into production. Huggingface offers many fine-tuned models trained on datasets similar to the ELLIPSE corpus: argumentative essays written by 8th-12th grade English Language Learners (ELLs).

<b>W</b>e'd like to know the model which will perform best on the given dataset. To this objective, our solution is to assemble five pre-trained Huggingface models and:
* Determine each model's computational cost by benchmarking them on both _speed_ and _required memory_.
* Train each model on the same data and collect their respective performance metrics
* Optimize each model using [Optuna](https://dl.acm.org/doi/10.1145/3292500.3330701)
* Use each optimized model's [state dictionary](https://pytorch.org/tutorials/recipes/recipes/what_is_state_dict.html) in a [new model](https://discuss.pytorch.org/t/combining-trained-models-in-pytorch/28383) that outputs a (6, 9) tensor, where each row is a probability distribution estimating the predicted class for a given category.

When choosing our models, it is not enough to compare them on their performance on a specific task alone. Each model's computational cost must be considered. 
