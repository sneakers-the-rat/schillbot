from tensor2tensor.utils import registry

from tensor2tensor.models.transformer import transformer_base
from tensor2tensor.models.evolved_transformer import evolved_transformer_base, evolved_transformer_big

@registry.register_hparams
def transformer_schill_wrestling_mp():
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

  # multiproblem
  hparams.multiproblem_per_task_threshold = "14,1,1"
  hparams.multiproblem_mixing_schedule = "constant"
  hparams.learning_rate_constant = 2e-2
  hparams.learning_rate_schedule = ("linear_warmup*constant*cosdecay")
  hparams.optimizer = "adam_w"
  hparams.optimizer_adam_beta1 = 0.9
  hparams.optimizer_adam_beta2 = 0.999
  hparams.optimizer_adam_epsilon = 1e-8
  hparams.learning_rate_decay_steps = 500000

  return hparams

@registry.register_hparams
def transformer_schill_wrestling_bw():
  """Hparams for transformer on LM for pretraining/finetuning/mixing."""
  hparams = evolved_transformer_base()
  hparams.learning_rate_decay_steps = 1000000

  hparams.batch_size = 3000
  hparams.hidden_size = 768
  hparams.filter_size = 2048
  hparams.num_encoder_layers = 4
  hparams.num_decoder_layers = 5
  hparams.label_smoothing = 0.0
  hparams.max_length = 750
  hparams.eval_drop_long_sequences = True
  hparams.multiproblem_vocab_size = 2**15
  hparams.clip_grad_norm = 1.0
  hparams.weight_decay = 1e-6

  # multiproblem
  hparams.multiproblem_per_task_threshold = "40,1,2"
  #hparams.multiproblem_mixing_schedule = "constant"
  hparams.multiproblem_schedule_max_examples = 100000
  #hparams.learning_rate_constant = 2e-2
  #hparams.learning_rate_schedule = ("linear_warmup*constant*cosdecay")
  hparams.optimizer = "adam_w"
  hparams.optimizer_adam_beta1 = 0.9
  hparams.optimizer_adam_beta2 = 0.99
  hparams.optimizer_adam_epsilon = 1e-8

  return hparams

@registry.register_hparams
def transformer_schill_wrestling_bw_big():
  """Hparams for transformer on LM for pretraining/finetuning/mixing."""
  hparams = evolved_transformer_base()
  hparams.learning_rate_decay_steps = 1000000

  hparams.batch_size = 2048
  hparams.hidden_size = 768
  #hparams.filter_size = 2048
  #hparams.num_encoder_layers = 4
  #hparams.num_decoder_layers = 5
  #hparams.layer_prepostprocess_dropout = 0.3
  #hparams.num_heads = 12
  #hparams.label_smoothing = 0.0
  hparams.max_length = 750
  hparams.eval_drop_long_sequences = True
  hparams.multiproblem_vocab_size = 2**15
  #hparams.clip_grad_norm = 1.0
  #hparams.weight_decay = 1e-6

  # multiproblem
  hparams.multiproblem_per_task_threshold = "40,1,2"
  hparams.multiproblem_mixing_schedule = "constant"
  #hparams.multiproblem_schedule_max_examples = 1000000
  #hparams.learning_rate_constant = 2e-2
  #hparams.learning_rate_schedule = ("linear_warmup*constant*cosdecay")
  #hparams.optimizer = "adam_w"
  #hparams.optimizer_adam_beta1 = 0.9
  #hparams.optimizer_adam_beta2 = 0.99
  #hparams.optimizer_adam_epsilon = 1e-8
  return hparams

@registry.register_hparams
def colab_transformer_schill_wrestling_mp():
  """Hparams for transformer on LM for pretraining/finetuning/mixing."""
  hparams = transformer_base()
  hparams.batch_size = 4096
  hparams.hidden_size = 768
  hparams.filter_size = 2048
  hparams.num_hidden_layers = 8
  hparams.num_heads = 8
  hparams.label_smoothing = 0.0
  hparams.max_length = 1024
  hparams.eval_drop_long_sequences = True
  hparams.multiproblem_vocab_size = 32000
  hparams.clip_grad_norm = 1.0


  # multiproblem
  hparams.multiproblem_per_task_threshold = "14,1,1"
  hparams.multiproblem_mixing_schedule = "constant"
  #hparams.learning_rate_constant = 2e-2
  hparams.weight_decay = 1e-6
  #hparams.learning_rate_schedule = ("linear_warmup*constant*cosdecay")
  #hparams.learning_rate_warmup_steps = 10000
  # one epoch for languagemodel_lm1b32k_packed = 27200 steps w/ bsize 128
  #hparams.learning_rate_decay_steps = 400000
  hparams.optimizer = "adam_w"
  hparams.optimizer_adam_beta1 = 0.9
  hparams.optimizer_adam_beta2 = 0.999
  hparams.optimizer_adam_epsilon = 1e-8
  #hparams.learning_rate_decay_steps = 500000

  return hparams

@registry.register_hparams
def macbook_transformer_schill_wrestling_mp():
  """Hparams for transformer on LM for pretraining/finetuning/mixing."""
  hparams = transformer_base()
  hparams.batch_size = 256
  hparams.hidden_size = 256
  hparams.filter_size = 1024
  hparams.num_hidden_layers = 8
  hparams.num_heads = 8
  hparams.label_smoothing = 0.0
  hparams.max_length = 512
  hparams.eval_drop_long_sequences = True
  hparams.multiproblem_vocab_size = 32000
  hparams.clip_grad_norm = 1.0

  # multiproblem
  hparams.multiproblem_per_task_threshold = "14,1,1"
  hparams.multiproblem_mixing_schedule = "constant"
  hparams.learning_rate_constant = 1e-1
  hparams.learning_rate_schedule = ("linear_warmup*constant*cosdecay")
  hparams.optimizer = "adam_w"
  hparams.optimizer_adam_beta1 = 0.9
  hparams.optimizer_adam_beta2 = 0.999
  hparams.optimizer_adam_epsilon = 1e-8
  hparams.learning_rate_decay_steps = 200000

  return hparams


