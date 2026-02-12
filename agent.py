import subprocess
from google.adk import Agent

def check_disk_space():
    """Returns the current disk usage of the MacBook."""
    result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    return result.stdout

def get_heavy_processes():
    """Returns the top 5 CPU-consuming processes."""
    result = subprocess.run(['ps', '-Ao', 'pcpu,comm', '-r'], capture_output=True, text=True)
    return "\n".join(result.stdout.splitlines()[:6])

# Define the Agent
root_agent = Agent(
    name="MacWhisperer",
    model="gemini-2.0-flash-lite", # Fast and cheap for local dev
    instruction="""You are a macOS expert. Help the user monitor their system. 
    Always explain technical stats in a friendly, witty way.""",
    tools=[check_disk_space, get_heavy_processes]
)