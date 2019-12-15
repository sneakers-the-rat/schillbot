import tensorflow as tf
from tqdm import tqdm
import pdb

schill_fn = "/home/lab/jonny/schillbot/schill.txt"
#schill_fn = "/mnt/data/schillbot_pt/spooky.txt"
decode_out = "/mnt/data/schillbot_pt/decode_full.txt"


low_threshold=10
up_threshold = 512

out_sentences = []

print('splitting sentences')
with open(schill_fn, 'r') as schill:

    txt = ""
    for line in tqdm(schill):
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

print('writing sentences')
with open(decode_out, 'w+') as out:
    for sent in tqdm(out_sentences):
        out.write(sent+'\n')



