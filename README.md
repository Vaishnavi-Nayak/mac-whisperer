# MacWhisperer 🖥️✨

A friendly macOS system monitoring and file management agent powered by Google's Gemini AI.

## Overview

MacWhisperer is an intelligent agent that helps you monitor your Mac's system resources and intelligently organize your Downloads folder. It analyzes file contents, provides system insights in a conversational tone, and suggests smart file organization strategies.

## Features

### System Monitoring
- **Disk Space**: Check available storage
- **Memory Usage**: Monitor RAM statistics
- **CPU Usage**: Track top CPU-consuming processes
- **Battery Status**: View current battery level and charging state
- **Network Info**: List network interfaces and active connections
- **System Uptime**: See how long your Mac has been running

### Intelligent File Management
- **Smart Downloads Scanner**: Automatically analyzes files in your Downloads folder
- **PDF Preview**: Reads PDF content to understand document type
- **Intelligent Suggestions**: Recommends destination folders based on file content
- **Safe Operations**: Always asks for confirmation before moving files
- **Folder Resolution**: Smart folder name matching (e.g., "Documents" finds ~/Documents)

## Prerequisites

- Python 3.8+
- macOS (uses system-specific commands like `pmset`, `vm_stat`, etc.)
- Google API Key with Gemini API access

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd macwhisperer
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install google-adk pymupdf
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_GENAI_USE_VERTEXAI=0
   GOOGLE_API_KEY=your_api_key_here
   ```

   **⚠️ Security Note**: Never commit your `.env` file to version control. It's already listed in `.gitignore`.

## Usage

```python
from agent import root_agent

# Example: Check disk space
response = root_agent.run("How much disk space do I have?")

# Example: Organize Downloads
response = root_agent.run("Can you check my Downloads folder and organize it?")

# Example: System health check
response = root_agent.run("Give me a system health overview")
```

## How It Works

### File Organization Flow

1. **Scan**: Agent lists all files in Downloads
2. **Analyze**: For PDFs, reads first 500 characters to understand content
3. **Suggest**: Proposes destination folders based on file type and content
4. **Confirm**: Waits for your approval
5. **Execute**: Moves files only after confirmation

### Smart Folder Resolution

The agent can find folders by name:
- "Documents" → `~/Documents`
- "Desktop" → `~/Desktop`
- Custom folder names anywhere in your home directory

If multiple matches exist, it shows all options for you to choose.

## Available Tools

| Tool | Description |
|------|-------------|
| `check_disk_space()` | Shows disk usage with `df -h` |
| `check_memory_usage()` | Displays RAM statistics via `vm_stat` |
| `check_battery_status()` | Battery level and charging status |
| `get_heavy_processes()` | Top 5 CPU-consuming processes |
| `check_uptime()` | System uptime information |
| `list_network_interfaces()` | Network interface details |
| `show_network_connections()` | Active network connections |
| `list_downloads()` | Files in ~/Downloads folder |
| `read_pdf_preview()` | First 500 chars of PDF content |
| `move_file()` | Move file to destination folder |
| `get_largest_files()` | Find largest files in a folder |

## Project Structure

```
.
├── agent.py           # Main agent definition and tools
├── __init__.py        # Package initialization
├── .env               # Environment variables (not in repo)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Configuration

The agent uses **Gemini 2.0 Flash Lite** for fast, cost-effective responses. To use a different model:

```python
root_agent = Agent(
    name="MacWhisperer",
    model="gemini-2.0-flash-exp",  # or another Gemini model
    instruction="...",
    tools=[...]
)
```

## Safety Features

- **Confirmation Required**: Never moves files without explicit user approval
- **Preview Mode**: Shows what will be moved before executing
- **Error Handling**: Graceful handling of PDF read errors
- **Path Validation**: Ensures folders exist before moving files

## Example Interactions

**System Monitoring:**
```
User: "How's my Mac doing?"
Agent: "Let me check your system health... Your Mac has been running for 3 days, 
        CPU usage is at 15% with Chrome being the hungriest app, and you have 
        45GB of free space. Battery is at 78% and not charging. Looking good! 🚀"
```

**File Organization:**
```
User: "Organize my Downloads"
Agent: "I found tax_return_2025.pdf. I suggest moving it to Documents/Taxes 
        because it appears to be a tax document. Should I proceed?"
User: "Yes"
Agent: "Successfully moved tax_return_2025.pdf to Documents/Taxes ✓"
```

## Limitations

- macOS only (uses system-specific commands)
- Requires manual API key setup
- PDF preview limited to first 500 characters
- Network access required for Gemini API

## Contributing

Contributions welcome! Please ensure:
- Code follows existing style
- New tools include proper error handling
- README updated for new features


## Security

**Never commit your `.env` file!** It contains sensitive API keys. The `.gitignore` file already excludes it, but always verify before pushing to a repository.

## Troubleshooting

**"No module named 'google.adk'"**
- Install: `pip install google-adk`

**"Permission denied" errors**
- Some system commands may require elevated privileges

**API key not working**
- Verify key is correct in `.env`
- Check API is enabled in Google Cloud Console