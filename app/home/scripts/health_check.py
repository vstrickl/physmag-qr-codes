"""Module that creates a UI view of the app."""
# ruff: noqa: E402
# pylint: disable=wrong-import-position
import os
import sys
import logging
from django.http import JsonResponse
from django.core.exceptions import ImproperlyConfigured

# Logger setup
LEVEL = logging.INFO
FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=LEVEL, format=FORMAT)
logger = logging.getLogger(__name__)

# Setup Django environment
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "physmagQrCodes.settings")

try:
    import django
    django.setup()
except ImportError as e:
    logger.error("Failed to import Django or setup the environment: %s", e, exc_info=True)
    sys.exit(1)
except ImproperlyConfigured as e:
    logger.error("Django settings are improperly configured: %s", e, exc_info=True)
    sys.exit(1)


# Create your views here.
def health_check(request):  # pylint: disable=unused-argument
    """Function that returns a JSON response with a status code of 200."""
    logger.info("Received health check request.")
    response_data = {"status": "ok"}
    logger.info("Health check response: %s", response_data)
    try:
        return JsonResponse({"status": "ok"}, status=200)
    except ValueError as e:
        logger.error("Value error in health_check: %s", e, exc_info=True)
        raise
    except TypeError as e:
        logger.error("Type error in health_check: %s", e, exc_info=True)
        raise

if __name__ == "__main__":
    logger.info("Starting health check module.")
    try:
        # Simulate a test call to health_check
        DUMMY_REQ = 200  # Replace this with an actual request object if needed
        response = health_check(DUMMY_REQ)
        logger.info("Health check test call successful: %s", response.content)
    except TypeError as e:
        logger.error("Type error during health check: %s", e, exc_info=True)
    except ValueError as e:
        logger.error("Value error during health check: %s", e, exc_info=True)
