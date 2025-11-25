from fastmcp import FastMCP
from datetime import datetime
import zoneinfo

# Initialize FastMCP server
mcp = FastMCP("time-server")

def get_time_logic(timezone: str) -> str:
    """
    Logic to get the current time in the specified timezone.
    """
    try:
        tz = zoneinfo.ZoneInfo(timezone)
        now = datetime.now(tz)
        return now.isoformat()
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_time(timezone: str) -> str:
    """
    Get the current time in the specified timezone.
    
    Args:
        timezone: The IANA timezone identifier (e.g., "Asia/Tokyo", "America/New_York", "UTC").
    
    Returns:
        The current time in ISO 8601 format with timezone information.
    """
    return get_time_logic(timezone)

if __name__ == "__main__":
    mcp.run()
