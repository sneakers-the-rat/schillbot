from tensor2tensor.utils import registry

from tensor2tensor.models.transformer import transformer_base

@registry.register_hparams
def transformer_schill():
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
  hparams.multiproblem_mixing_schedule = "pretrain"
  hparams.multiproblem_vocab_size = 32000
  hparams.clip_grad_norm = 1.0

  # pretrain_lm
  hparams.learning_rate_constant = 2e-4
  hparams.learning_rate_schedule = ("linear_warmup*constant*cosdecay")
  hparams.optimizer = "adam_w"
  hparams.optimizer_adam_beta1 = 0.9
  hparams.optimizer_adam_beta2 = 0.999
  hparams.optimizer_adam_epsilon = 1e-8
  # Set max examples to something big when pretraining only the LM, definitely
  # something an order of magnitude bigger than number of train steps.
  hparams.multiproblem_schedule_max_examples = 5e8
  # Set train steps to learning_rate_decay_steps or less
  hparams.learning_rate_decay_steps = 5000000


  # small
  hparams.learning_rate_warmup_steps = 10000
  return hparams
