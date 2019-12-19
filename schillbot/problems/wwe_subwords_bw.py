from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry
from tensor2tensor.data_generators.wiki_lm import LanguagemodelEnWiki32k
from tensor2tensor.data_generators.lm1b import LanguagemodelLm1b32k
import tensorflow as tf

from schillbot.problems.schill_subwords_pretrained import SchillSubwordsPretrained

import os

from tensor2tensor.data_generators import multi_problem


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
class WWESubwordsBw(text_problems.Text2SelfProblem):

  @property
  def use_vocab_from_other_problem(self):
    return LanguagemodelLm1b32k()

  @property
  def approx_vocab_size(self):
    return 2**15  # 32768

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
        "shards": 99,
    }, {
        "split": problem.DatasetSplit.EVAL,
        "shards": 1,
    }]

  def generate_samples(self, data_dir, tmp_dir, dataset_split):


    filename = os.path.join(data_dir, 'wwe.txt')

    up_threshold = self.combine_characters_threshold
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
