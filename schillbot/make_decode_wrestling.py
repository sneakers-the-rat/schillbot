import tensorflow as tf
from tqdm import tqdm
import pdb
import numpy as np
import argparse

parser = argparse.ArgumentParser()

schill_fn = "data/schill.txt"
wwe_fn = "data/wwe.txt"


#schill_fn = "/mnt/data/schillbot_pt/spooky.txt"
decode_out = "data/decode_sample.txt"


low_threshold=10
up_threshold = 512
n_samples = 100

out_sentences = []

print('loading sentences')

def load_sentences(fn):
    out_sentences = []
    txt = ""
    with open(fn, 'r') as ofile:
        for line in tqdm(ofile):
            line = line.strip()

            if len(txt) + len(line) + 1 >= up_threshold:
                ret = txt
                txt = ""
                # We don't yield very short long parts to prevent noisy examples.
                if len(ret) > low_threshold and len(ret) < up_threshold:
                  out_sentences.append(ret)

            if not txt:
                txt = line
            else:
                txt = " ".join([txt, line])

    return out_sentences

wwe = load_sentences(wwe_fn)
schill = load_sentences(schill_fn)

wwe.extend(schill)

# get random selection
select_ints = np.random.randint(low=0,high=len(wwe)-1, size=n_samples)

out_sentences = [wwe[i] for i in select_ints]


print('writing sentences')
with open(decode_out, 'w+') as out:
    for sent in tqdm(out_sentences):
        out.write(sent+'\n')



