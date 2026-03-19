"""
Defines the pipeline workflow (ingest → transform → validate).
"""

from src.ingest import main as ingest_main
from src.logger import get_logger
from src.transform import main as transform_main
from src.validate import main as validate_main

logger = get_logger(__name__)


def run_pipeline() -> None:
    """Run the full pipeline with error handling."""
    logger.info("Pipeline run started")

    try:
        ingest_main()
        transform_main()
        validate_main()
        logger.info("Pipeline run completed successfully")

    except Exception as e:
        logger.error(f"Pipeline run failed: {e}", exc_info=True)
