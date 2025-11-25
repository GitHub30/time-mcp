from server import get_time_logic as get_time
import zoneinfo
from datetime import datetime

def test_get_time():
    # Test UTC
    print("Testing UTC...")
    time_utc = get_time("UTC")
    print(f"UTC Time: {time_utc}")
    assert "+00:00" in time_utc or "Z" in time_utc

    # Test Tokyo
    print("\nTesting Asia/Tokyo...")
    time_tokyo = get_time("Asia/Tokyo")
    print(f"Tokyo Time: {time_tokyo}")
    assert "+09:00" in time_tokyo

    # Test New York
    print("\nTesting America/New_York...")
    time_ny = get_time("America/New_York")
    print(f"New York Time: {time_ny}")
    # New York is -05:00 (EST) or -04:00 (EDT)
    # Currently it's November, so EST (-05:00)
    assert "-05:00" in time_ny

    print("\nAll tests passed!")

if __name__ == "__main__":
    try:
        test_get_time()
    except Exception as e:
        print(f"\nTest failed: {e}")
        # Check if it's a zoneinfo error
        if "No time zone found" in str(e):
            print("It seems tzdata might be missing on Windows.")
