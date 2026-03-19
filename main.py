"""
Top-level entrypoint for running the data pipeline.
"""

from src.pipeline import run_pipeline


def main() -> None:
    """Main entrypoint for executing the pipeline."""
    run_pipeline()


if __name__ == "__main__":
    main()
