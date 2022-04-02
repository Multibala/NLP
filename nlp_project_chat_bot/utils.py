input_text,target_text = [],[]
input_vocabulary,output_vocabulary = set(),set()
df = None
start_token = '\t'
stop_token = '\n'


max_training_samples = min(25000,len(df))