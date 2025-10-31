#!/usr/bin/env python3
"""
Main application entrypoint for the ETL pipeline system.
This file serves as the primary entrypoint for the Docker container.
"""

import os
import sys
import logging
from sdk.your_sdk.cli import main as cli_main

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """
    Main entrypoint function for the application
    """
    logger.info("Starting ETL Pipeline application...")
    
    # You can add initialization logic here
    # For now, we'll just call the CLI main function
    try:
        # Check if CLI is available and run it
        logger.info("ETL Pipeline application started successfully")
        logger.info("Available commands can be found by running: python -m sdk.your_sdk.cli --help")
        
        # Keep the container running
        # This is a simple placeholder - in a real application you might want to
        # run a server, start processing jobs, etc.
        while True:
            import time
            time.sleep(60)  # Sleep for 60 seconds before next check
    except KeyboardInterrupt:
        logger.info("Application terminated by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()