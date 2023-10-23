import logging
import os
import warnings

warnings.simplefilter("default")
logging.captureWarnings(True)


def get_logging_configuration():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "{asctime} [{levelname}] {name}.{funcName}({lineno}) pid({process:d}) {threadName}({thread:d}) - {message}",
                "style": "{",
            }
        },
        "filters": {
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            },
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "verbose",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "loggers": {
            "": {
                "handlers": ["console"],
                "level": "DEBUG",
                "propagate": False,
            },
            "django": {
                "handlers": ["console"],
                "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
                "propagate": False,
            },
            "django.request": {
                "handlers": ["console"],
                "level": "DEBUG",
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False,
            },
            "apscheduler": {
                "level": "WARN",
                "handlers": ["console"],
                "propagate": False,
            },
            "mailer.engine": {
                "level": "WARN",
                "handlers": ["console"],
                "propagate": False,
            },
            "django.db.backends.schema": {
                "level": "INFO",
                "handlers": ["console"],
                "propagate": False,
            },

        },
    }
