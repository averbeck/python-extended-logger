import logging
import sys

from pathlib import Path


class ExtendedLogger(logging.Logger):
    """Custom configurable logger

    Configure logging

    """

    def __init__(
        self,
        strLoggerName: str,
        strLogLevel: str = "info",
        iMaxClassNameLength: int = 25,
        bToStdOut: bool = True,
        pathLogFile: Path | None = None,
    ):

        enLogLevel = getattr(logging, strLogLevel.upper())
        super().__init__(strLoggerName, level=enLogLevel)

        # Set log format
        strLogFormatFull: str = f"%(asctime)2s %(name)-{iMaxClassNameLength+1}s %(levelname)-8s %(message)s"
        strLogFormatSimple: str = f"%(name)-{iMaxClassNameLength+1}s: %(levelname)-8s : %(message)s"
        strLogFormatDate: str = "%m.%d.%Y %H:%M:%S"

        # Set logging streams
        if pathLogFile is not None and pathLogFile.parent.is_dir():
            # File logger
            fileLogger = logging.FileHandler(pathLogFile)
            fileLogger.setLevel(enLogLevel)
            fileLogger.setFormatter(logging.Formatter(strLogFormatFull, strLogFormatDate))
            self.addHandler(fileLogger)

            if not bToStdOut:
                # Standard error stream logger
                errorLogger = logging.StreamHandler(stream=sys.stderr)
                errorLogger.setLevel(logging.ERROR)
                errorLogger.setFormatter(logging.Formatter(strLogFormatSimple, strLogFormatDate))
                self.addHandler(errorLogger)
        else:
            bToStdOut = True
            self.warning("Invalid log file was set! Sending log to <stout>")

        # Standard out stream logger
        if bToStdOut:
            standardLogger = logging.StreamHandler(stream=sys.stdout)
            standardLogger.setLevel(enLogLevel)
            standardLogger.setFormatter(logging.Formatter(strLogFormatSimple, strLogFormatDate))
            self.addHandler(standardLogger)
