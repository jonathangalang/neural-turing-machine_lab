import torch

INT_MAX = (2 ** 8) + 1

def generate_copy_problem(signal_length, delay, batch_size):
    """

    Args:
        signal_length (int): the number of 8-bit integers to generate
        delay (int): the number of time-steps to delay before the recall signal
        batch_size (int): the number of copy problems to generate
    """
    # generate batches of sequences of random 8-bit integers
    signal = torch.randint(0, INT_MAX, (batch_size, signal_length), dtype=torch.uint8) 
    

