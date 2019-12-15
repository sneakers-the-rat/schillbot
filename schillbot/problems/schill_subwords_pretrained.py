from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry
from tensor2tensor.data_generators.wiki_lm import LanguagemodelEnWiki32k
import tensorflow as tf

import os

def concat_generator(filename, up_threshold, low_threshold=10):
  """Generate concatenated lines from file upto up_threshold characters."""
  txt = ""
  for line in tf.gfile.Open(filename):
    line = line.strip()
    if len(txt) + len(line) + 1 >= up_threshold:
      ret = txt
      txt = ""
      # We don't yield very short long parts to prevent noisy examples.
      if len(ret) > low_threshold and len(ret) < up_threshold:
        yield {"targets": ret}

    if not txt:
      txt = line
    else:
      txt = " ".join([txt, line])


class VocabType(object):
  """Available text vocabularies."""
  CHARACTER = "character"
  SUBWORD = "subwords"
  TOKEN = "tokens"


@registry.register_problem
class SchillSubwordsPretrained(text_problems.Text2SelfProblem):
  """Predict next line of poetry from the last line. From Gutenberg texts."""

  #@property
  #def approx_vocab_size(self):
  #  return 5000  # ~8k

  @property
  def use_vocab_from_other_problem(self):
    return LanguagemodelEnWiki32k()

  @property
  def approx_vocab_size(self):
    return 32000

  @property
  def combine_characters_threshold(self):
    """Threshold for upto how many characters to combine in examples."""
    return 512*8  # So we should have 512 tokens on average, maybe more.

  @property
  def vocab_type(self):
    return VocabType.SUBWORD


  @property
  def is_generate_per_split(self):
    # generate_data will shard the data into TRAIN and EVAL for us.
    return False

  @property
  def dataset_splits(self):
    """Splits of data to produce and number of output shards for each."""
    # 10% evaluation data
    return [{
        "split": problem.DatasetSplit.TRAIN,
        "shards": 9,
    }, {
        "split": problem.DatasetSplit.EVAL,
        "shards": 1,
    }]

  def generate_samples(self, data_dir, tmp_dir, dataset_split):


    filename = os.path.join(data_dir, 'schill.txt')

    up_threshold = 512*8
    low_threshold= 10


    txt = ""
    for line in tf.gfile.Open(filename):
      line = line.strip()
      if len(txt) + len(line) + 1 >= up_threshold:
        ret = txt
        txt = ""
        # We don't yield very short long parts to prevent noisy examples.
        if len(ret) > low_threshold and len(ret) < up_threshold:
          yield {"targets": ret}

      if not txt:
        txt = line
      else:
        txt = " ".join([txt, line])




