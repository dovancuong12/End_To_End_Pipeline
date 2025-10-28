from setuptools import setup, find_packages

setup(
    name="end-to-end-pipeline-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyspark>=3.3.0",
        "apache-airflow>=2.4.0",
        "kafka-python>=2.0.2",
        "elasticsearch>=8.0.0",
        "redis>=4.3.4",
        "great-expectations>=0.15.0",
        "sqlalchemy>=1.4.0",
        "pandas>=1.5.0",
        "minio>=7.1.0",
        "requests>=2.28.0",
        "pyyaml>=6.0",
        "click>=8.0.0",
        "python-dotenv>=0.19.0"
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950"
        ]
    },
    entry_points={
        "console_scripts": [
            "e2e-pipeline=sdk.cli:main"
        ]
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="End-to-End Data Pipeline SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/end-to-end-pipeline",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)