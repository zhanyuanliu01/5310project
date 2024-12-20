import time
import torch._dynamo
torch._dynamo.config.suppress_errors = True
out_dir = 'out-titleintro-medium'
eval_interval = 5
eval_iters = 40
wandb_log = False # feel free to turn on
wandb_project = 'titleintro'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'titleintro'
init_from = 'gpt2-medium' 

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# titleintro has 35167 tokens, so 1 epoch ~= 1.07 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 50

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False
