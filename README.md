# 5310project
Code are adapted and modified from nanoGPT created by Andrej Karpathy link: https://github.com/karpathy/nanoGPT/tree/master

#Prepare Training dataset

```sh
python data/titleintro_char/prepare.py
```
For GPT2 Tokenizer

```sh
python data/titleintro/prepare.py
```
#Train or finetune

```sh
python train.py config/train_titleintro_char.py
```

```sh
python train.py config/finetune_titleintro_medium.py
```

#Sample

```sh
python sample.py --out_dir=out-titleintro-char --start="Title:  Rh Single Atom Catalyst for Low Temperature CO Oxidation"
```
