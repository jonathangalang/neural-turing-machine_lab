import argparse
import os
import sys

from src.utils import config
from sanity_check import devtest

def parse_args():
    """

    Returns:
        argparse.Namespace: parsed arguments
        
    """
    parser = argparse.ArgumentParser("NTM Lab")
    subparsers = parser.add_subparsers(dest="mode", required=True,
                                      help="Choose an action: train or run experiments")

    # train subcommand
    parser_train = subparsers.add_parser("train", help="Run the training pipeline.")
    parser_train.add_argument(
        "--config",
        type=str,
        default="experiments/configs/lstm.yaml",
        help="Path to the training config file."
    )

    # experiment subcommand
    parser_experiment = subparsers.add_parser("experiment", help="Run experiment analysis.")
    parser_experiment.add_argument(
        "--config",
        type=str,
        default="experiments/configs/experiment.yaml",
        help="Path to the experiment config file."
    )

    return parser.parse_args()

if __name__ == '__main__':
    argv = parse_args()
    
    config.enable_logs()
    
    global_config = config.load_global_config()
    
    if argv.mode == "train":
        devtest(global_config['output_dir'])

