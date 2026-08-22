# Snakepit

A growing collection of Python projects, experiments, and course exercises.

The name is intentional: Python runs on snakes — this is where they live.

## Background

I'm a mechanical engineer with a background in product ownership. I'm building this repo to develop practical Python and machine learning skills — one small project at a time. The goal is breadth: shipping something small beats planning something big.

## Start here

If you only look at three things:

1. **[CATIA V5 Knowledge Test](./Applications/Knowledge%20Tests/Catia%20V5/)** — the most complete project here. A Tkinter quiz app with 187 questions, single- and multiple-choice grading, explanations, and a review mode.
2. **[Failure Theory](./Mechanical%20Engineering/Notebooks/Machine%20Design/Failure%20Theory/)** — Von Mises and Tresca yield envelopes plotted in principal stress space. The clearest example of using Python on the engineering problems I already know.
3. **[Deploy a Model](./Machine%20Learning/fastai/Exercises/Deploy_Model/)** — training an image classifier and putting it behind a Gradio interface, end to end.

## What's here

| Section | Content |
|---|---|
| [Mechanical Engineering](./Mechanical%20Engineering/) | Physics simulations and engineering calculations built with NumPy and Matplotlib |
| [Machine Learning](./Machine%20Learning/) | Image classification, model deployment, and Gradio UIs following Jeremy Howard's fast.ai course |
| [Applications](./Applications/) | Standalone tools — starting with a Catia V5 knowledge quiz app |

Each section has its own README explaining what the projects do and how to run them.

## Getting started

Developed against **Python 3.12**.

```bash
git clone https://github.com/kelinio/Snakepit.git
cd Snakepit
pip install -r requirements.txt
jupyter lab
```

The application in `Applications/` needs no dependencies at all — it's standard-library Tkinter. Run it directly:

```bash
python "Applications/Knowledge Tests/Catia V5/main.py"
```

The fast.ai notebooks train much faster on a GPU. Without one locally, open them in [Google Colab](https://colab.research.google.com/) and pick a GPU runtime.

## Approach

This is a learning log as much as a portfolio. Some projects are polished tools, others are single-notebook experiments. New projects get added whenever I work through a course or explore something new.

## License

Original work in this repo is under the [MIT License](./LICENSE).

Notebooks in `Machine Learning/fastai/fastbook/` are exercises derived from the
[fast.ai book](https://github.com/fastai/fastbook) by Jeremy Howard & Sylvain Gugger,
which is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
Those notebooks follow that license, not MIT.
