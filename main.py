import argparse
import os
import sys

from src.utils import config
from src.data.synthetic_data import sanity_check

def parse_args():
    """

    Returns:
        argparse.Namespace: parsed arguments
        
    """
    parser = argparse.ArgumentParser("NTM Lab")
    parser.add_argument("run", help="Run a training experiment")
    parser.add_argument("--config", type=str,
                        help="Path to the YAML config file.")
    return parser.parse_args()

if __name__ == '__main__':
    argv = parse_args()
    
    config.enable_logs()

    config.load_config(argv.config)
    
    sanity_check()

