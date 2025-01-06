from torch.utils.data import DataLoader

def identity_collate(batch):
    return batch

class UnbatchedDataLoader(DataLoader):
    def __init__(self,
                 dataset,
                 batch_size=None,
                 collate_fn=identity_collate,
                 num_workers=0,
                 pin_memory=True,
                 timeout=0,
                 worker_init_fn=None,
                 **kwargs):

        if batch_size is not None:
            raise ValueError('UnbatchedDataLoader expects batch_size=None \
                    since data is already batched.')

        super(UnbatchedDataLoader, self).__init__(
            dataset,
            batch_size=None,
            collate_fn=collate_fn,
            num_workers=num_workers,
            pin_memory=pin_memory,
            timeout=timeout,
            worker_init_fn=worker_init_fn,
            **kwargs
        )

