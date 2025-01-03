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
    logger.info(f'binary sequence of shape {binary_sequence.shape}:\n{binary_sequence}')
    
    # scale 1s for contrast
    binary_sequence *= 255
    
    # convert to PIL image
    img = Image.fromarray(binary_sequence, mode='L')
    img.save(out_path)

