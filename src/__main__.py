"""Module defines the main entry point for the Apify Actor.

This module imports and executes the main function from main.py to ensure
proper Actor execution within the Apify platform.
"""

from .main import main
import asyncio

if __name__ == '__main__':
    asyncio.run(main())