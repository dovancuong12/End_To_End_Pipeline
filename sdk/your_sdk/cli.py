#!/usr/bin/env python3
"""
CLI commands for the SDK
This module provides command-line interface for the ETL system
"""

import click
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@click.group()
def main():
    """Main CLI group for the ETL Pipeline SDK"""
    logger.info("ETL Pipeline SDK CLI initialized")

@main.command()
@click.option('--config', default='config/config.yaml', help='Configuration file path')
def init(config):
    """Initialize the ETL pipeline system"""
    logger.info(f"Initializing ETL Pipeline with config: {config}")
    print(f"ETL Pipeline initialized with config: {config}")

@main.command()
def status():
    """Check the status of the ETL pipeline system"""
    logger.info("Checking ETL Pipeline status")
    print("ETL Pipeline is running")

@main.command()
@click.option('--job-type', type=click.Choice(['batch', 'streaming']), default='batch', help='Type of job to run')
def run_job(job_type):
    """Run an ETL job"""
    logger.info(f"Running {job_type} job")
    print(f"Running {job_type} ETL job")

if __name__ == '__main__':
    main()
