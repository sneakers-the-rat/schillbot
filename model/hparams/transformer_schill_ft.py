from tensor2tensor.utils import registry

from tensor2tensor.models.transformer import transformer_base

@registry.register_hparams
def transformer_schill_ft():
  """Hparams for transformer on LM for pretraining/finetuning/mixing."""
  hparams = transformer_base()
  hparams.batch_size = 1024
  hparams.hidden_size = 768
  hparams.filter_size = 2048
  hparams.num_hidden_layers = 12
  hparams.num_heads = 12
  hparams.label_smoothing = 0.0
  hparams.max_length = 1024
  hparams.eval_drop_long_sequences = True
  hparams.multiproblem_vocab_size = 32000
  hparams.clip_grad_norm = 1.0

  return hparams

