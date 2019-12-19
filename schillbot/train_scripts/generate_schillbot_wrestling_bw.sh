#python make_decode_wrestling.py

t2t-decoder \
 --problem=schill_wrestling_mp_bw \
 --data_dir=/mnt/data/schillbot_data \
 --t2t_usr_dir=/home/lab/git/schillbot/schillbot \
 --tmp_dir=/mnt/data/schillbot_tmp \
 --train_dir=/mnt/data/schillbot_wrestling_bw_big/checkpoints\
 --output_dir=/mnt/data/schillbot_wrestling_bw_big/checkpoints \
 --model=evolved_transformer \
 --hparams_set=transformer_schill_wrestling_bw_big \
 --hparams="sampling_method=random,sampling_temp=0.75" \
 --decode_hparams="beam_size=1,alpha=0.6,num_decodes=1,multiproblem_task_id=32000" \
 --decode_from_file=/mnt/data/schillbot_wrestling_bw/decode_sample.txt \
 --decode_to_file=/mnt/data/schillbot_wrestling_bw_big/decode_samples/generated_sample_schillbot_75.txt

 t2t-decoder \
 --problem=schill_wrestling_mp_bw \
 --data_dir=/mnt/data/schillbot_data \
 --t2t_usr_dir=/home/lab/git/schillbot/schillbot \
 --tmp_dir=/mnt/data/schillbot_tmp \
 --train_dir=/mnt/data/schillbot_wrestling_bw_big/checkpoints\
 --output_dir=/mnt/data/schillbot_wrestling_bw_big/checkpoints \
 --model=evolved_transformer \
 --hparams_set=transformer_schill_wrestling_bw_big \
 --hparams="sampling_method=random,sampling_temp=0.75" \
 --decode_hparams="beam_size=1,alpha=0.6,num_decodes=1,multiproblem_task_id=32001" \
 --decode_from_file=/mnt/data/schillbot_wrestling_bw/decode_sample.txt \
 --decode_to_file=/mnt/data/schillbot_wrestling_bw_big/decode_samples/generated_sample_wwe_75.txt

