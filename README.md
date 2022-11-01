# Temporal Expression Identification to Go

Temporal Expression Identification to Go (TEI2GO) is an approach for fast and effective identification of temporal expressions.

> **_NOTE:_** TEI2GO was submitted to ECIR'23. To ensure the reproducibility of the results presented in the manuscript
> we created the branch `paper` which contains the script to reproduce the presented models along with the logs that the
> training process produced. Furthermore, the README of that branch also contains information that complements the 
> original manuscript. Therefore, we encourage our most interested readers to `git checkout paper` in order to attain a  
> hands-on understanding of the approach. 

## Development environment

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

## Train

```shell
python run.py --data "tempeval_2_italian" --language "it" --model "spacy" --n_epochs 5 --dropout 0.1
```

### Download Pre-Trained Models

```shell
cd models
sh download.sh
```

### Download Resources

```shell
cd resources
sh download.sh
```