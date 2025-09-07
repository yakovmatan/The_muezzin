import logging


def get_logger(
    name: str = "console_logger",
    level: int = logging.INFO,
    fmt: str = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt: str = "%d-%m-%Y %H:%M:%S"
) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt, datefmt)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
