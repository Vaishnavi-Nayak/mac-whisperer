import subprocess
from google.adk import Agent

def check_disk_space():
    """Returns the current disk usage of the MacBook."""
    result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    return result.stdout

def check_memory_usage():
    """Returns current memory usage statistics."""
    result = subprocess.run(['vm_stat'], capture_output=True, text=True)
    return result.stdout

def check_battery_status():
    """Returns the current battery status."""
    result = subprocess.run(['pmset', '-g', 'batt'], capture_output=True, text=True)
    return result.stdout

def list_network_interfaces():
    """Lists all network interfaces and their status."""
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)
    return result.stdout

def check_uptime():
    """Returns how long the system has been running."""
    result = subprocess.run(['uptime'], capture_output=True, text=True)
    return result.stdout

def show_network_connections():
    """Shows active network connections."""
    result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
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
    tools=[check_disk_space, get_heavy_processes,check_memory_usage, check_battery_status, list_network_interfaces, check_uptime, show_network_connections]
)