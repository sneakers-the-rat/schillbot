t2t-trainer \
 --problem=schill_wrestling_mp \
 --t2t_usr_dir=/Users/jonny/git/schillbot/schillbot \
 --data_dir=/Users/jonny/Desktop/schillbot/data \
 --tmp_dir=/Users/jonny/Desktop/schillbot/tmp \
 --train_dir=/Users/jonny/Desktop/schillbot/checkpoints \
 --output_dir=/Users/jonny/Desktop/schillbot/checkpoints \
 --checkpoint_dir=/Users/jonny/Desktop/schillbot/checkpoints \
 --model=transformer \
 --hparams_set=macbook_transformer_schill_wrestling_mp \
 --local_eval_frequency=100 \
 --keep_checkpoint_max=10 \
 --keep_checkpoint_every_n_hours=2 \
 --train_steps=500000

# --warm_start_from=/Users/jonny/Desktop/schillbot/checkpoints \

