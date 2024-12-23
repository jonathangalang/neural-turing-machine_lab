import src.utils.logs as logs
import torch

logger = logs.get_logger(__name__)

def setup():
    logs.configure()
    torch.set_default_device('cuda')
    if 'cuda' not in torch.get_default_device().type:
        logger.warning('No GPU detected. Running with CPU...')
    else:
        logger.info('Successfully set default device to CUDA.')

