

from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems
from tensor2tensor.utils import registry

import os


@registry.register_problem
class SchillWords(text_problems.Text2TextProblem):
  """Predict next line of poetry from the last line. From Gutenberg texts."""

  @property
  def approx_vocab_size(self):
    return 5000  # ~8k

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

    with open(os.path.join(data_dir, 'schill.txt'), 'r') as schill_f:
        schill = schill_f.read().replace("\n", " <eos> ").encode('ascii', errors='ignore').decode('utf-8').lower().split()

    # make 40-length series w next word

    for i in range(len(schill)-40):
        yield {
            'inputs': " ".join(schill[i:i+39]),
            'targets': schill[i+39]
        }


