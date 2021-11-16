# Additional Requirement

Our report is ./tianhu+yucjia_atmt_assignment03.pdf

We include all result files in ./results/ 

We include a processed sample dataset with BPE in ./data_bpe/ 

We require the subword-nmt library for BPE operations. You can then install using the following: 

pip install subword-nmt

To process the training data with BPE (change the number of merges directly in the .py file):

```
python preprocess_wBPEdropout.py \
    --source-lang fr \
    --target-lang en \
    --dest-dir ./data/en-fr/prepared \
    --train-prefix ./data/en-fr/preprocessed/train \
    --valid-prefix ./data/en-fr/preprocessed/valid \
    --test-prefix ./data/en-fr/preprocessed/test \
    --tiny-train-prefix ./data/en-fr/preprocessed/tiny_train \
    --threshold-src 1 \
    --threshold-tgt 1 \
    --num-words-src 4000 \
    --num-words-tgt 4000 \
	--bpedropout 0.1 \
	--bpe True 
```

To run model training with BPE:

```
python train.py \
    --data path/to/prepared/data \
    --source-lang en \
    --target-lang sv \
    --save-dir path/to/model/checkpoints \
    --train-on-tiny \ # for testing purposes only
	--bpe True \
	--bpedropout 0.1 \
```

# atmt code base
Materials for the first assignment of "Advanced Techniques of Machine Translation".
Please refer to the assignment sheet for instructions on how to use the toolkit.

The toolkit is based on [this implementation](https://github.com/demelin/nmt_toolkit).


# Environment Setup

### conda

```
# ensure that you have conda (or miniconda) installed (https://conda.io/projects/conda/en/latest/user-guide/install/index.html) and that it is activated

# create clean environment
conda create --name atmt36 python=3.6

# activate the environment
conda activate atmt36

# intall required packages
pip install torch==1.6.0 numpy tqdm sacrebleu
```

### virtualenv

```
# ensure that you have python 3.6 downloaded and installed (https://www.python.org/downloads/)

# install virtualenv
pip install virtualenv

# create a virtual environment named "atmt36"
virtualenv --python=python3 atmt36

# launch the newly created environment
atmt36/bin/activate

# intall required packages
pip install torch==1.6.0 numpy tqdm sacrebleu
```

<!-- # Data Preprocessing

```
# normalise, tokenize and truecase data
bash scripts/extract_splits.sh ../infopankki_raw data/en-sv/infopankki/raw

# binarize data for model training
bash scripts/run_preprocessing.sh data/en-sv/infopankki/raw/
``` -->

# Training a model

```
python train.py \
    --data path/to/prepared/data \
    --source-lang en \
    --target-lang sv \
    --save-dir path/to/model/checkpoints \
    --train-on-tiny # for testing purposes only
```

Notes:
- `path/to/prepared/data` and `path/to/model/checkpoints`
  are placholders, not true paths. Replace these arguments with the correct paths
  for your system.
- only use `--train-on-tiny` for testing. This will train a
dummy model on the `tiny_train` split.

# Evaluating a trained model

Run inference on test set
```
python translate.py \
    --data path/to/prepared/data \
    --dicts path/to/prepared/data \
    --checkpoint-path path/to/model/checkpoint/file/for/loading \
    --output path/to/output/file/model/translations
```

Postprocess model translations
```
bash scripts/postprocess.sh path/to/output/file/model/translations path/to/postprocessed/model/translations/file en
```

Score with SacreBLEU
```
cat path/to/postprocessed/model/translations/file | sacrebleu path/to/raw/target/test/file
```

# Assignments

Assignments must be submitted on OLAT by 14:00 on their respective
due dates.

- [x] Assignment 1: Training and evaluating an NMT model
  with in-domain and out-of-domain data **DUE: 12.10.2021**
- [ ] Assignment 2: Experiment design **DUE: 26.10.2021**
- [ ] Assignment 3: Improving a low-resource NMT system
  **DUE: 16.11.2021**
- [ ] Assignment 4: Decoding strategies - Beam Search **DUE: 07.12.2021**
- [ ] Assignment 5: Exam preparation **DUE: 21.12.2021**


