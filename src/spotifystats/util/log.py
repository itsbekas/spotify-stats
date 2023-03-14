import logging

logger = logging.getLogger(__name__)


def init_logger():
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(name)s.%(funcName)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
        level=logging.INFO,
    )
