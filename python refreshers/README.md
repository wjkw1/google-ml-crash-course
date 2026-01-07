# Python Refreshers

This directory contains quick refresher tutorials for Python libraries NumPy and Pandas.
I wanted a refresher of NumPy and Pandas basics for quick reference while working on projects that involve numerical computations and data manipulation and analysis. These tutorials serve as concise guides to help me remember key concepts and functions in NumPy and Pandas.
Thankfully, Google has provided ultraquick tutorials for both libraries as part of their Machine Learning Crash Course.

## 1. Numpy Ultraquick Tutorial

https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/numpy_ultraquick_tutorial.ipynb?hl=en#scrollTo=azZFyENLZm_g

This is a quick tutorial on NumPy, a powerful library for numerical computing in Python. It covers the basics of creating arrays, performing operations, and using various functions provided by NumPy.

See file `numpy-refresher.py` for relevant code snippets.

## 2. Pandas Ultraquick Tutorial

https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb?hl=en

This is a quick tutorial on Pandas, a powerful library for data manipulation and analysis in Python. It covers the basics of creating DataFrames, performing operations, and using various functions provided by Pandas.

See file `pandas-refresher.py` for relevant code snippets.

## Setup venv

If you haven't already, set up a virtual environment and install the required packages:

```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` should contain:

```
numpy
pandas
```

Alternatively you can install packages manually

```zsh
pip install numpy pandas
```

But I'd recommend using the `requirements.txt` file and a virtual environment for better package management.

## VS Code Usage

I run the code using the Play button in VS Code after selecting the appropriate Python interpreter from the virtual environment.

In the past I've run the python3 commands directly in the terminal like so:

```zsh
python3 numpy-refresher.py
```

But VS Code's ecosystem makes it much easier to run and debug code snippets. You simply drop a debug point and click the Play button with a bug on it (Run with Debug), and then you can see all required information in once place.

This works for me, if you want to run the code in a different way, feel free to do so!
