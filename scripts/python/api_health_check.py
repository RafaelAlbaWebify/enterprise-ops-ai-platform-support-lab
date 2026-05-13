"""
Basic API health check script for support-level troubleshooting.

Usage:
    python api_health_check.py https://example.com/health

Notes:
    This script is intentionally simple. It is designed for learning and support evidence,
    not for production monitoring.
"""

import sys
import time
import urllib.request
import urllib.error


def check_url(url: str) -> None:
    start = time.time()

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            elapsed_ms = round((time.time() - start) * 1000, 2)
            print(f"URL: {url}")
            print(f"Status: {response.status}")
            print(f"LatencyMs: {elapsed_ms}")
            print("Support note: Endpoint responded successfully.")

    except urllib.error.HTTPError as error:
        elapsed_ms = round((time.time() - start) * 1000, 2)
        print(f"URL: {url}")
        print(f"Status: {error.code}")
        print(f"LatencyMs: {elapsed_ms}")
        print("Support note: Endpoint responded with an HTTP error.")
        print("Next step: Check error code, request ID, permissions, quota and service health.")

    except Exception as error:
        elapsed_ms = round((time.time() - start) * 1000, 2)
        print(f"URL: {url}")
        print(f"LatencyMs: {elapsed_ms}")
        print(f"Error: {error}")
        print("Support note: Endpoint could not be reached or request failed before HTTP response.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python api_health_check.py <url>")
        sys.exit(1)

    check_url(sys.argv[1])
