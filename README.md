[![Python 3.7.12+](https://img.shields.io/badge/python-3.7.2+-blue.svg)](https://www.python.org/downloads/release/python-3712/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

# phm_evolutionary_optimization

The tuning of a BERT model requires expertise and contains a large amount of variance. However, if one were to represent tuning as a pre-defined search space, a Genetic Algorithm (GA) could be used to tune BERT, resulting in more fit and robust solutions and a less intensive tuning step. On the whole, we propose that introducing GAs as a tuning algorithm for the BERT model will result in less variance and better classifications of PHM. As a result of our experiments, we have found that even short training times have improved the PHM classifications of a zero-shot BERT model classification task. 

## Team

The members of team are as follows:

* [Victoria Armstrong](https://github.com/victoriaaarmstrong)
* [Emily Medema](https://github.com/emedema)
* [Debbie Wang](https://github.com/debbiewang99)

## Implementation

We have implemented the [BERT model via HuggingFace](https://huggingface.co/docs/transformers/model_doc/bert) in Python. The GA is also written in Python. We use binary representation within the GA and test each potential solution by passing that binary string to the BERT model, which translates the binary, tests the specifications, and then returns the performance in the required format.

### Data

We are working with two tweet datasets regarding personal health mentions, [PHM2017](https://github.com/emory-irlab/PHM2017) and [FLU2013](http://michaeljpaul.com/downloads/flu_data.php). We followed the classification used in the PHM2017 dataset which is the following:

|Classification|Definition|
|--------------|----------|
|0|Not Health Related|
|1|Awareness for Disease|
|2|Mention of Other Person Having Disease|
|3|Mention of Self Having Disease|

### EA Design

The EA design we are using is as follows:

|Technical Aspect|Choice|
|----------------|------|
|Representation|Binary String|
|Mutation|Bit Flip|
|Recombination|Uniform Crossover|
|Parent Selection|Tournament (size = 10)|
|Survivor Selection|$\mu + \lambda$|
|Fitness |F1 score|
|Population Size|20|
|No. of Generations |20|

## Installation

1. Install the required libaries with the following line of code in terminal:
```
pip install -r requirements.txt
```

2. Navigate to the `ga_code` folder and run the `main.py` file with the following command:
```
python3 main.py
```
