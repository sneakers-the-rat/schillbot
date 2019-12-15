import sys
import os

sys.path.append(os.path.abspath(__file__))

from schillbot.problems import schill_words
from schillbot.problems import schill_chars
from schillbot.problems import schill_subwords_pretrained
from schillbot.problems import schill_subwords_mp
from schillbot.problems import wwe_subwords
from schillbot.problems import schill_wrestling_mp

from schillbot.hparams import transformer_schill
from schillbot.hparams import transformer_schill_ft
from schillbot.hparams import transformer_schill_mp
from schillbot.hparams import transformer_schill_wrestling_mp


