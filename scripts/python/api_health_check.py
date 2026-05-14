"""
Basic API health check for support-level troubleshooting.

Purpose:
    This script performs a simple HTTP endpoint check and reports
    the response status and basic latency.

    It is designed for IT Operations / AI Platform Operations practice,
    where support teams often need to confirm whether an endpoint responds,
    collect evidence and escalate with useful technical context.

What this script demonstrates:
    - Basic endpoint availability check
    - HTTP status handling
    - Simple latency measurement
    - API troubleshooting awareness
    - Support-level Python usage

What this script does NOT demonstrate:
    - Production monitoring
    - Advanced observability
    - Secure API authentication handling
    - Advanced Python development
    - Real Azure OpenAI integration

Example:
    python api_health_check.py https://www.microsoft.com
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
