from src.utils.logs import get_logger
from src.data.synthetic_data import generate_copy_problem
from src.data.bitmaps import write_to_bitmap

def devtest(output_dir):
    logger = get_logger(__name__)
    inputs, targets = generate_copy_problem(25, 50, 100)
    logger.info('Success: Generated inputs and targets for copy problem.')
    if inputs.shape == targets.shape:
        logger.info('Success: Input and target shapes match.')
    else:
        logger.error('Failure: Input and target shapes do not match.')
    if inputs.get_device() != -1 and targets.get_device() != -1:
        logger.info('Success: Generated tensors on GPU.')
    else:
        logger.warning('Failure: Generated tensors were not placed on the GPU.')
    logger.info(f'Writing tensor {inputs[0]} to file...')
    write_to_bitmap(inputs[0], output_dir)

