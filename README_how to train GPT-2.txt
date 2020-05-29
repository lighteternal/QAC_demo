Στο φάκελο DimPapSandbox>transformers>examples>language-modeling
αφού θέσω ως env_variables τις απαιτούμενες παρακάτω (train_file πχ sample_Data_period.txt):

python3 run_language_modeling.py --output_dir=output1 --model_type=gpt2     --model_name_or_path=gpt2 --do_train --train_data_file=$TRAIN_FILE --per_gpu_train_batch_size=1