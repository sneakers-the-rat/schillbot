t2t-trainer \
 --generate_data \
 --problem=schill_subwords_pretrained \
 --t2t_usr_dir=/home/lab/jonny/schillbot \
 --data_dir=/mnt/data/schillbot_pt \
 --tmp_dir=/mnt/data/jonny/schillbot_pt \
 --train_dir=/mnt/data/schillbot_ft/checkpoints \
 --output_dir=/mnt/data/schillbot_ft/checkpoints \
 --checkpoint_dir=/mnt/data/schillbot_ft/checkpoints \
 --warm_start_from=/mnt/data/schillbot_pt/checkpoints \
 --model=transformer \
 --hparams_set=transformer_schill_ft \
 --local_eval_frequency=2000 \
 --keep_checkpoint_max=100 \
 --train_steps=1000000


