import logging
import logging.config

from app.configs import config


class OnDebugFalse(logging.Filter):
    """Log only if DEBUG_MODE is False"""

    def filter(self, _):
        return not config.debug


class OnDebugTrue(logging.Filter):
    """Log only if DEBUG_MODE is True"""

    def filter(self, _):
        return config.debug


# set logging configuration
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "%(name)s - %(levelname)s - %(message)s"},
        "file": {
            "format": "%(name)s - %(levelname)s - %(asctime)s - %(module)s - %(message)s"
        },
    },
    "filters": {"debug_true": {"()": OnDebugTrue}, "debug_false": {"()": OnDebugFalse}},
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        "file": {
            "level": "WARNING",
            "filters": ["debug_false"],
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "file",
            # should be in root/logs directory
            # filename should be month-date-year.txt
            "filename": "logs/logging.log",
            "when": "H",
            "interval": 3,
        },
        # "database": {
        #     "level": "WARNING",
        #     "filters": ["debug_false"],
        #     "class": "logging.handlers.TimedRotatingFileHandler",
        #     "formatter": "file",
        #     "filename": "logs/db_logging.log",
        #     "when": "H",
        #     "interval": 3,
        # },
        "product_update": {
            "level": "INFO",
            "filters": ["debug_false"],
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "file",
            "filename": "logs/product_update.log",
            "when": "midnight",
        },
    },
    "loggers": {
        "main": {"handlers": ["console", "file"], "LEVEL": "INFO", "propagate": True},
        "database": {
            "handlers": ["console", "database"],
            "LEVEL": "INFO",
            "propagate": True,
        },
        "uvicorn.error": {
            "handlers": ["console", "file"],
            "LEVEL": "DEBUG",
            "propagate": True,
        },
        "uvicorn.access": {
            "handlers": ["console", "file"],
            "LEVEL": "DEBUG",
            "propagate": True,
        },
        "activity": {
            "handlers": ["console", "file"],
            "LEVEL": "INFO",
            "propagate": True,
        },
        "product_update": {
            "handlers": ["console", "product_update"],
            "LEVEL": "INFO",
            "propagate": False,
        },
        "db_client": {
            "handlers": ["console", "database"],
            "level": "WARNING",
            "propagate": True,
        },
        "tortoise": {
            "handlers": ["console", "database"],
            "level": "WARNING",
            "propagate": True,
        },
        "httpx_client": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
