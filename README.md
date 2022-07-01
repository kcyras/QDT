# Quantitative Dispute Trees

A very limited collection of tools for [Qualitative (Bipolar) Argumentation](https://doi.org/10.1016/j.ijar.2018.11.019).

## Requirements

* [sympy](https://www.sympy.org/en/index.html) for Python
* [Jupyter](https://jupyter.org/) for notebooks

## Assumes

* Computation of [Quadratic Energy (QE) semantics](semantics_QE_acyclic.pl) for *acyclic* Quantitative Bipolar Argumentation Graphs (QBAGs) as described in [Nico Potyka @ KR2018](https://aaai.org/ocs/index.php/KR/KR18/paper/view/17985) and [Nico Potyka @ AAMAS2019](https://www.ifaamas.org/Proceedings/aamas2019/pdfs/p1722.pdf).

## Contents

* **WIP**: [symbolic derivatives](contrib.py) for determining _saliency gradient_ contributions in acyclic QBAGs under QE semantics (also on Jupyter notebooks, e.g. [example01](exampleQDT.ipynb))
