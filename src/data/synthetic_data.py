import torch
# import matplotlib.pyplot as plt

from src.utils.logs import get_logger

UINT8_MAX = (2 ** 8) - 1

def generate_copy_problem(signal_length, delay_length, batch_size):
    """

    Args:
        signal_length (int): the number of 8-bit integers to generate
        delay_length (int): the number of time-steps to delay before the recall signal
        batch_size (int): the number of copy problems to generate

    Returns:
        (inputs, targets):  Tensors of shape [batch_size, total_seq_len];
                            Each entry is an unsigned 8-bit integer
    """
    # generate batches of sequences of random 8-bit integers
    signal = torch.randint(0, UINT8_MAX, (batch_size, signal_length), dtype=torch.uint8) 
    
    # after each signal, a delay period with no new information ensues
    delay = torch.zeros(batch_size, delay_length, dtype=torch.uint8)

    # highest 8-bit integer is reserved for the recall marker
    recall_marker = UINT8_MAX * torch.ones(batch_size, 1, dtype=torch.uint8)
    
    # after the recall marker, the model is expected to output the signal from memory
    # thus, perform additional zero-padding for the duration of the recall period
    post_delay = torch.zeros(batch_size, signal_length - 1, dtype=torch.uint8)
    
    # concatenate these artifacts in order for the input
    inputs = torch.cat([signal, delay, recall_marker, post_delay], dim=1)
    
    # the target is a zero-padded copy of the original signal
    pre_recall = torch.zeros(batch_size, signal_length + delay_length, dtype=torch.uint8)
    targets = torch.cat([pre_recall, signal], dim=1)

    return (inputs, targets)

def sanity_check():
    logger = get_logger(__name__)
    inputs, targets = generate_copy_problem(25, 50, 100)
    logger.info('Successfully generated inputs and targets for copy problem.')
    if inputs.shape == targets.shape:
        logger.info('Success: Input and target shapes match.')
    else:
        logger.error('Failure: Input and target shapes do not match.')
    
