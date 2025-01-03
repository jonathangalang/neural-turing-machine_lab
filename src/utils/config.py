import src.utils.logs as logs
import torch
import yaml

logger = logs.get_logger(__name__)

def enable_logs():
    logs.configure()
    torch.set_default_device('cuda')
    if 'cuda' not in torch.get_default_device().type:
        logger.warning('Failure: No GPU detected. Running with CPU...')
    else:
        logger.info('Success: Set default device to CUDA.')

def load_config(config_path):
    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

def load_global_config():
    return load_config('configs/global.yaml')
