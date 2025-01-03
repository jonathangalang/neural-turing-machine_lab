import os
import torch
import numpy as np
from PIL import Image

from src.utils.logs import get_logger

def write_to_bitmap(data_tensor, out_dir, filename='signal.png'):

    logger = get_logger(__name__)
    out_path = os.path.join(out_dir, filename)

    # move tensor to CPU and detach from computational graphs
    cpu_tensor = data_tensor.detach().cpu()

    # strip to numpy array
    raw_sequence = np.expand_dims(cpu_tensor.numpy(), axis=0)

    # expand each int as a binary vector
    binary_sequence = np.unpackbits(raw_sequence, axis=0)
    
    # scale 1s for contrast
    binary_sequence *= 255

    # convert to PIL image
    img = Image.fromarray(binary_sequence, mode='L')
    try:
        img.save(out_path)
    except Exception:
        logger.error(f'Failed to write uint8 tensor of shape {data_tensor.shape} to location {out_path}')
    else:
        logger.info(f'Success: wrote uint8 tensor of shape {data_tensor.shape} to location {out_path}')
