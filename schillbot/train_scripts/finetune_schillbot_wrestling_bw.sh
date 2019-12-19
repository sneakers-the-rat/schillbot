t2t-trainer \
 --generate_data \
 --problem=schill_wrestling_mp_bw \
 --t2t_usr_dir=/home/lab/git/schillbot/schillbot \
 --data_dir=/mnt/data/schillbot_data \
 --tmp_dir=/mnt/data/jonny/schillbot_tmp \
 --train_dir=/mnt/data/schillbot_wrestling_bw_big/checkpoints \
 --output_dir=/mnt/data/schillbot_wrestling_bw_big/checkpoints \
 --checkpoint_dir=/mnt/data/schillbot_wrestling_bw_big/checkpoints \
 --model=evolved_transformer \
 --hparams_set=transformer_schill_wrestling_bw_big \
 --local_eval_frequency=10000 \
 --keep_checkpoint_max=30 \
 --keep_checkpoint_every_n_hours=1 \
 --train_steps=1250000


