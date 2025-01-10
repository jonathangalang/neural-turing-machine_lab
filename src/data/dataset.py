import torch
from torch.utils.data import IterableDataset

from src.utils.logs import get_logger
from src.data import synthetic_data

class CopyProblemDataset(IterableDataset):

    """

    Attributes: 
        max_seq_len: The maximum number of ints to generate
        max_delay: The maximum number of time-steps to delay before the recall signal
        batch_size: The number of sample sequences to draw
        unsqueeze: Flag to add singleton dimension to targets
    """
    def __init__(self, batch_size, max_seq_len, max_delay, unsqueeze=True):
        super().__init__()
        self.max_seq_len = max_seq_len
        self.max_delay = max_delay
        self.batch_size = batch_size
        self.unsqueeze = unsqueeze

    def generate(self):
        
        """
        Generator wrapper for synthetic_data.generate_copy_problem()

        Yields: 
            (inputs, targets): tuple of batched sequence-to-sequence pairs
            
        """
        while True:

            sequence_len = torch.randint(1, self.max_seq_len, (1,)).item()
            delay_len = torch.randint(1, self.max_delay, (1,)).item()

            inputs, targets = synthetic_data.generate_copy_problem(
                sequence_len, delay_len, self.batch_size
            )
            
        if unsqueeze:
            yield (inputs.unsqueeze(2), targets.unsqueeze(2))
        else:
            yield (inputs, targets)

    def __iter__(self):

        return self.generate()


