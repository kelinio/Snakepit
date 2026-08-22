# Machine Learning

Work from Jeremy Howard's [Practical Deep Learning for Coders](https://course.fast.ai/) (fast.ai). The focus is on getting a model trained and deployed end to end rather than on theory — each notebook is small and does one thing.

## What's here

| Notebook | What it does | Run |
|---|---|---|
| [Is it a Bird?](./fastai/Exercises/Is_it_a_Bird/main.ipynb) | Builds an image classifier that tells birds from forests. Scrapes training images with DuckDuckGo search, fine-tunes a `resnet18` for 3 epochs, then predicts on a held-out photo. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kelinio/Snakepit/blob/main/Machine%20Learning/fastai/Exercises/Is_it_a_Bird/main.ipynb) |
| [Deploy a Model — training](./fastai/Exercises/Deploy_Model/model.ipynb) | Trains a cat-vs-dog classifier on the Oxford-IIIT Pets dataset and exports it as `model.pkl`. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kelinio/Snakepit/blob/main/Machine%20Learning/fastai/Exercises/Deploy_Model/model.ipynb) |
| [Deploy a Model — Gradio UI](./fastai/Exercises/Deploy_Model/gradio.ipynb) | Wraps the exported model in a [Gradio](https://gradio.app/) interface with three example images, so it can be used from a browser. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kelinio/Snakepit/blob/main/Machine%20Learning/fastai/Exercises/Deploy_Model/gradio.ipynb) |
| [fastbook ch. 1](./fastai/fastbook/01_intro.ipynb) · [ch. 2](./fastai/fastbook/02_production.ipynb) | Exercises worked through alongside the fast.ai book chapters. | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kelinio/Snakepit/blob/main/Machine%20Learning/fastai/fastbook/01_intro.ipynb) |

## Running these

From the repository root:

```bash
pip install -r requirements.txt
```

fast.ai training is much faster with a GPU. If you don't have one locally, open the notebooks in [Google Colab](https://colab.research.google.com/) and select a GPU runtime.

**Order matters for the deployment pair:** `gradio.ipynb` loads a file called `model.pkl`, which is *not* checked into this repo — model weights are build output, not source. Run `model.ipynb` first to produce it, then run `gradio.ipynb` from the same folder.

## What I took away from it

- A useful classifier needs surprisingly little data and surprisingly little code — the `resnet18` fine-tune is three lines.
- Most of the real work is in the data: search results need verifying (`verify_images`) because broken downloads will otherwise crash training.
- Deployment is a separate skill from training. Exporting to `.pkl` and loading it in a process that has never seen the training data is what makes the model actually usable.

## License note

The notebooks in `fastai/fastbook/` are derived from the [fast.ai book](https://github.com/fastai/fastbook) by Jeremy Howard & Sylvain Gugger, licensed [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). They follow that license, not this repository's MIT license.
