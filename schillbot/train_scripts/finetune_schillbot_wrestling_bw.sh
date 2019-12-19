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
 --local_eval_frequency=5000 \
 --keep_checkpoint_max=30 \
 --keep_checkpoint_every_n_hours=1 \
 --train_steps=1250000
 # --schedule=train_eval_and_decode \
 # --hparams="sampling_method=random,sampling_temp=0.75" \
 # --decode_hparams="beam_size=1,alpha=0.6,num_decodes=1,multiproblem_task_id=32001" \
 # --decode_from_file=/mnt/data/schillbot_wrestling_bw/decode_sample.txt \
 # --decode_to_file=/mnt/data/schillbot_wrestling_bw_big/decode_samples/training_generated_sample_wwe_75.txt



