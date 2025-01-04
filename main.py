import argparse
import os
import sys

from src.utils import config
from src.utils.logs import get_logger
from src.training.trainer import train_model
from experiments.run_experiment import run_experiment

def parse_args():
    """

    Returns:
        argparse.Namespace: parsed arguments
        
    """
    parser = argparse.ArgumentParser('NTM Lab')
    subparsers = parser.add_subparsers(dest='mode', required=True,
                                      help='Choose an action: train or run experiments')

    # train subcommand
    parser_train = subparsers.add_parser('train', help='Run the training pipeline.')
    parser_train.add_argument(
        '--config',
        type=str,
        default='configs/models/lstm.yaml',
        help='Path to the training config file.'
    )

    # experiment subcommand
    parser_experiment = subparsers.add_parser('experiment', help='Run experiment analysis.')
    parser_experiment.add_argument(
        '--config',
        type=str,
        default='configs/experiment.yaml',
        help='Path to the experiment config file.'
    )

    return parser.parse_args()

if __name__ == '__main__':
    # runtime arguments defined in compose.yaml
    argv = parse_args()
    
    # set up logging
    config.enable_logs()
    logger = get_logger(__name__)

    # read settings that apply to all builds/modes
    global_config = config.load_global_config()
    logger.info(f'Received global config object {global_config}')

    # read settings for this specific build
    logger.info(f'Acquiring runtime config from {argv.config}')
    runtime_config = config.load_config(argv.config)
    logger.info(f'Read config object {runtime_config}')

    if argv.mode == 'train':
        train_model(runtime_config)
    elif argv.mode == 'experiment':
        run_experiment(runtime_config)
