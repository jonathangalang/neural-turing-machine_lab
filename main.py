import argparse
import os
import sys

from src.utils import config
from src.utils.logs import get_logger
from src.training.trainer import train_model
from experiments.run_experiment import run_experiment


def parse_args():
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(description='NTM Lab')
    
    # Define subparsers for different modes
    subparsers = parser.add_subparsers(dest='mode', required=True,
        help='Choose an action: train or experiment')
    
    # Parent parser for config
    config_parser = argparse.ArgumentParser(add_help=False)
    config_parser.add_argument(
        '--config',
        type=str,
        default='configs/models/lstm.yaml',
        help='Path to the configuration file.'
    )    

    # Train subcommand
    parser_train = subparsers.add_parser('train', 
        parents=[config_parser],
        help='Run the training pipeline.')
    
    # Experiment subcommand
    parser_experiment = subparsers.add_parser('experiment', 
        parents=[config_parser],
        help='Run experiment analysis.')

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
