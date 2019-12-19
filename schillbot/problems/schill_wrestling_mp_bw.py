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
from schillbot.problems.schill_subwords_bw import SchillSubwordsBw
from schillbot.problems.wwe_subwords import WWESubwords
from schillbot.problems.wwe_subwords_bw import WWESubwordsBw

import os

from tensor2tensor.data_generators import multi_problem



def mix_generators(generator_list):
  """Given python generators, generate from one, then from another, etc."""
  i = 0
  l = len(generator_list)
  stopiters_seen = 0
  while stopiters_seen <= l:
    try:
      yield six.next(generator_list[i % l])
      i += 1
      stopiters_seen = 0
    except StopIteration:
      i += 1
      stopiters_seen += 1





@registry.register_problem
class SchillWrestlingMpBw(multi_problem.MultiProblem):
  """Predict next line of poetry from the last line. From Gutenberg texts."""

  #@property
  #def approx_vocab_size(self):
  #  return 5000  # ~8k

  def __init__(self, was_reversed=False, was_copy=False):

    super(SchillWrestlingMpBw, self).__init__(was_reversed, was_copy)

    self.task_list.append(LanguagemodelLm1b32k())
    self.task_list.append(SchillSubwordsBw())
    self.task_list.append(WWESubwordsBw())

  @property
  def vocab_type(self):
    return text_problems.VocabType.SUBWORD

  @property
  def use_vocab_from_other_problem(self):
    return LanguagemodelLm1b32k()

