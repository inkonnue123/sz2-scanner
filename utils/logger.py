import logging
import sys

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[0;37m',  # White
        'INFO': '\033[1;32m',  # Green
        'WARNING': '\033[1;33m',  # Yellow
        'ERROR': '\033[1;31m',  # Red
        'CRITICAL': '\033[1;41m',  # Red background
    }
    RESET = '\033[0m'

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        message = super().format(record)
        return f'{color}{message}{self.RESET}'

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout,
)

# Apply the colored formatter to the root logger
for handler in logging.getLogger().handlers:
    handler.setFormatter(ColoredFormatter())

# Example usage
if __name__ == '__main__':
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
