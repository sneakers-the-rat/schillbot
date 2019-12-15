t2t-trainer \
 --generate_data \
 --problem=schill_subwords_mp \
 --t2t_usr_dir=/home/lab/jonny/schillbot \
 --data_dir=/mnt/data/schillbot_pt \
 --tmp_dir=/mnt/data/jonny/schillbot_pt \
 --train_dir=/mnt/data/schillbot_mp_tenth/checkpoints \
 --output_dir=/mnt/data/schillbot_mp_tenth/checkpoints \
 --checkpoint_dir=/mnt/data/schillbot_mp_tenth/checkpoints \
 --warm_start_from=/mnt/data/schillbot_pt/checkpoints \
 --model=transformer \
 --hparams_set=transformer_schill_mp \
 --local_eval_frequency=5000 \
 --keep_checkpoint_max=1000 \
 --train_steps=500000


