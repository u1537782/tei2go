# Temporal Expression Identification to Go

This branch serves to present/reproduce the results presented in the paper "TEI2GO: A Multilingual Methodology for Fast Temporal
Expression Identification" which was submitted to ECIR'23. 

The directory is structured as follows:
```shell
├── logs  "Contain the logs produced by running the training process."
│     
├── models
│   └── download.sh  "A shell script that will download the models presente don the manuscript."
│     
├── reproduce.sh  "A shell script to reproduce the models to replicate the training process that we done at the time."
│            
├── resources
│   └── download.sh  "A shell script to download the necessary resources."
│            
├── result  "The metrics of the models on the test set of each corpus in each language."
```

## Setup environment and directory.
```shell
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
```

Since the evaluation notebook uses the HeidelTime model as a baseline one is required to follow the installation steps
of the [py_heideltime package](https://github.com/JMendes1995/py_heideltime). For a linux system one just needs to run
the following command.

```sh
sudo chmod 111 venv/lib/python3.8/site-packages/py_heideltime/Heideltime/TreeTaggerLinux/bin/*
```

## How to...

### reproduce the training process?
In short, the training process can be reproduced by running the following line:
```shell
sh reproduce.sh
```
The more elaborated answered would be 


### evaluate the models?

```shell
sh models/download.sh
python -m src.evaluate
```

While the first line of the script above will download the models that were presented in the manuscript, the second line
will produce the results that are presented in the folder `results`.   

