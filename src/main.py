"""..."""

import sys

import uvicorn
from services import cli_service
from config import config


def main():
    """..."""
    args = sys.argv[1:]
    if len(args):
        cli_service.handle(args=args)
    else:
        uvicorn.run(
            "api:app",
            host=config.host,
            port=config.port,
            reload=config.debug,
        )


if __name__ == "__main__":
    main()
