"""
This is the function of the code that reads from memory the location to
how to update the Slack service. It manages the logic of handling
multiple Slack servers and allows users to update all of them at once.
"""

API_ROUTE = '/api/users.profile.set'

# TODO: Create this function.
def sendUpdate(token: str, status: str, emoji: str, expiriation: int = 0) -> bool:
    """
    Updates the status of the given token with the given status and
    emoji. Also takes an expiriation argument formatted as an integer
    with UNIX timestamp format. If no UNIX timestamp is provided, it
    defaults to 0, which Slack treats as no expiration. Returns true
    if the status updated successfully. 
    """
    return False

# TODO: Create this function
def update(status: str, emoji: str, expiriation: int = 0) -> bool:
    """
    Updates all logged into Slack platforms with the given status and
    emoji. I haven't decided if I want to format expiriation as a UNIX
    timestamp yet or 'time from now' sort of thing. Returns true if
    all of the status updates updated successfully.
    """
    return False