t2t-trainer \
 --generate_data \
 --problem=schill_wrestling_mp \
 --t2t_usr_dir=/home/lab/git/schillbot/schillbot \
 --data_dir=/mnt/data/schillbot_pt \
 --tmp_dir=/mnt/data/jonny/schillbot_pt \
 --train_dir=/mnt/data/schillbot_wrestling_mp/checkpoints \
 --output_dir=/mnt/data/schillbot_wrestling_mp/checkpoints \
 --checkpoint_dir=/mnt/data/schillbot_wrestling_mp/checkpoints \
 --warm_start_from=/mnt/data/schillbot_pt/checkpoints \
 --model=transformer \
 --hparams_set=transformer_schill_wrestling_mp \
 --local_eval_frequency=5000 \
 --keep_checkpoint_max=30 \
 --keep_checkpoint_every_n_hours=1 \
 --train_steps=500000


