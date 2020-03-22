import os
import logging.config
import yaml
import my_module


def setup_logging(
    default_path='./logging.yaml',
    default_level=logging.DEBUG,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


setup_logging()


logger = logging.getLogger(__name__)

my_module.foo()
bar = my_module.Bar()
bar.bar()
