# samplepath  
# The Sample Path Analysis Library and Toolkit

A reference implementation of sample-path–based flow metrics, convergence analysis, and stability diagnostics for flow processes in 
complex adaptive systems.

[![PyPI](https://img.shields.io/pypi/v/pypcalc.svg)](https://pypi.org/project/pypcalc/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-online-blue.svg)](https://py.pcalc.org)

---

## 🔍 Overview

**samplepath** is a Python library for **empirical analysis of flow processes** 
using the finite-window formulation of **Little’s Law**.  

It provides deterministic, pathwise measurement tools for analyzing long run
process dynamics: arrival/departure equilibrium, process time coherence, and
process stability along an observed sample path.

The package implements the computational framework used in the
*Presence Calculus* project to reason about **equilibrium**, **coherence**, and **stability**
of flow processes from observed event timelines.

### Background

For an overview of the key concepts please see 
[The Many Faces of Little's Law](https://www.polaris-flow-dispatch.com/p/the-many-faces-of-littles-law).

Our continuing series on Little's Law and sample path analysis at [The Polaris Flow Dispatch](https://www.polaris-flow-dispatch.com)
has more background and applications of these concepts. Please subscribe if you want to get 
ongoing guidance on how to use these tools and techniques to analyze flow processes in your organization. 

## Core capabilities

A flow process is simply a timeline of events from some underlying domain where
events have effects that persist beyond the time of the event. Each event has one or more
*marks* to as metadata to describe those effects. The toolkit is designed to be lightweight
with minimal dependencies. 

The data requirements are  minimal: a csv file with id, start and end date columns.

The current version supports the analysis of binary flow processes: Where we require no
additional explicit marks (the start and end date serve as implicit marks for the
start and end of some observed effect)

Given this input, the toolkit provides

A. Core python modules that correctly implement the computations for: 

- Time-averaged flow metrics that are governed by the finite version of Little's Law
   `N(t), L(T)`,`Λ(T)`, `w(T)`, `λ*(T)`, `W*(T)` (Please see here for definitions)
- Performing *equilibrium* and **coherence** calculations (e.g., verifying `L(T) ≈ λ*(T)·W*(T)`)
- Estimating empirical **limits** with uncertainty and **tail** checks to verify stability (alpha)

B. Command line tools also provide simple modules that wrap all these calculation

- Generate publication-ready **charts and panel visualizations** 
- Simple file based tools to run and save scenarios from different scenario analyses.

This toolkit provides the computational foundation for analyzing flow dynamics in 
software delivery, operations, and other knowledge-work systems.


## 🚀 Installation (End Users)

Pre-requisites Python 3 (only tested on version 3.11 or higher at present).

```bash
pip install samplepath
```

After installation, the CLI will be available:

```bash
samplepath --help
```

Or run the module directly:

```bash
python -m samplepath.cli --input events.csv --completed
```

To upgrade to the latest version:

```bash
pip install -U samplepath
```

---

## 🧠 Concepts

Deterministic, sample-path analogues of Little’s Law:

| Quantity | Meaning |
|-----------|----------|
| `L(T)` | Average work-in-process over window `T` |
| `Λ(T)` | Cumulative arrivals per unit time up to `T` |
| `w(T)` | Average residence time over window `T` |
| `λ*(T)` | Empirical arrival rate up to `T` |
| `W*(T)` | Empirical mean sojourn time of items completed by `T` |

These quantities enable rigorous study of **equilibrium** (rate balance), **coherence** (`L ≈ λ*·W*`), and **stability** (convergence of process and empirical measures to limits) even when processes operate far from steady state.

---

## 📂 Output Layout

For input `events.csv`, output is organized as:

```
<output or ./out>/
└── events/
    └── <scenario>/                 # e.g., latest
        ├── input/                  # input snapshots
        ├── core/                   # core metrics & tables
        ├── convergence/            # limit estimates & diagnostics
        ├── convergence/panels/     # multi-panel figures
        ├── stability/panels/       # stability/variance panels
        ├── advanced/               # optional deep-dive charts
        └── misc/                   # ancillary artifacts
```

Only the **known** subdirectories above are created.

---

## 🧩 Example Usage

```bash
# Analyze completed items and clean output directories
samplepath --input events.csv --scenario weekly --completed --clean

# Limit analysis to the past 60 days
samplepath --input events.csv --horizon-days 60

# Apply lambda percentile and warmup filtering
samplepath --input events.csv --lambda-pctl-lower 5 --lambda-pctl-upper 95 --lambda-warmup-hours 24
```

Results and charts are saved under the generated scenario directory.

---

## 🛠 Development Setup (for Contributors)

---

## 📦 Package Layout

```
samplepath/
├── cli.py               # Command-line interface
├── csv_loader.py        # CSV import utilities
├── metrics.py           # Empirical flow metric calculations
├── limits.py            # Convergence and limit estimators
├── plots.py             # Chart and panel generation
└── tests/               # Pytest suite
```

---

Developers working on **samplepath** use [Poetry](https://python-poetry.org/) for dependency and build management.

### 1. Clone and enter the repository
```bash
git clone https://github.com/krishnaku/samplepath.git
cd samplepath
```

### 2. Install development dependencies
```bash
poetry install
```

### 3. Activate the virtual environment
```bash
poetry shell
```

### 4. Run tests
```bash
pytest
```

### 5. Code quality checks
```bash
black samplepath/
isort samplepath/
mypy samplepath/
```

### 6. Build and publish (maintainers)
To build the distributable wheel and sdist:

```bash
poetry build
```

To upload to PyPI (maintainers only):

```bash
poetry publish --build
```


## 📚 Documentation

Further documentation, examples, and conceptual background are available in the  
[*Presence Calculus* repository](https://github.com/krishnaku/pypcalc)  
and the associated research series on *Flow Processes and Little’s Law*.

---

## 📝 License

Licensed under the **MIT License**.  
See `LICENSE` for details.
