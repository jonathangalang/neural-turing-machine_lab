from src.utils.logs import get_logger

def run_experiment(experiment_config):
    logger = get_logger(__name__)
    logger.info('Successfully reached experiment entrypoint. ')
    logger.info(f'Received config {experiment_config}.')
