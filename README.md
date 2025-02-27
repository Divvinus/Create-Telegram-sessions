# Telegram Session Creator

<div align="center">

```
████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
   ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║
   ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
███████╗███████╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔════╝██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
███████╗█████╗  ███████╗███████╗██║██║   ██║██╔██╗ ██║
╚════██║██╔══╝  ╚════██║╚════██║██║██║   ██║██║╚██╗██║
███████║███████╗███████║███████║██║╚██████╔╝██║ ╚████║
╚══════╝╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
 ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

<a href="https://t.me/your_channel">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram" alt="Telegram Channel">
</a>
<a href="https://t.me/your_contact">
    <img src="https://img.shields.io/badge/Telegram-Contact-blue?style=for-the-badge&logo=telegram" alt="Telegram Contact">
</a>
<br>
<b>Donations:</b> <code>Your Wallet Address Here</code>
</div>


A powerful tool for creating and managing Telegram sessions using Pyrogram. Supports multiple accounts, proxy integration, and automated session management.

## 🚀 Key Features

- Automated Telegram session creation
  - Easy setup with API credentials
  - Multiple session management
  - Phone number verification
- Proxy integration
  - HTTP/SOCKS5 proxy support
  - Individual proxy assignment per session
  - Proxy rotation capabilities
- Session management
  - Custom session naming
  - Session information display
  - Organized session storage
- Additional features
  - Logger integration with success/error reporting
  - Clean workspace organization
  - Extensible for bot development

## 📋 System Requirements

- Python 3.7 or higher
- Windows/Linux/macOS
- Telegram account
- API credentials from my.telegram.org

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/telegram-session-creator.git
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/macOS
.\venv\Scripts\activate   # for Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. API Credentials Setup

1. Visit [my.telegram.org](https://my.telegram.org/auth) and log in
2. Go to "API development tools" and create a new application
3. Copy your API_ID and API_HASH
4. Update `config.py` with your credentials:

```python
# my.telegram.org
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'

WORKDIR = "sessions/"
USE_PROXY = False
PROXY_TYPE = 'http'  # or 'socks5'
```

### 2. Proxy Configuration (Optional)

If you want to use proxies, set `USE_PROXY = True` in `config.py` and create a `proxy.txt` file with the following format:

```
hostname:port:username:password session_name1
hostname:port:username:password session_name2
```

### 3. Session Workspace

Sessions will be stored in the `sessions/` directory. Make sure this directory exists or will be created automatically when running the script.

## 🚀 Launch

```bash
python main.py
```

## 📚 Available Commands

After launching the tool, follow the prompts:
1. Select action: 
   - 1. Create session - Create a new Telegram session

When creating a session:
1. Enter a session name (descriptive for your reference)
2. Follow the authentication prompts (phone number, verification code)
3. Session will be created and saved to the workspace

## 🔍 Troubleshooting

1. "API ID/API HASH invalid" - Double-check your API credentials from my.telegram.org
2. "Proxy connection error" - Verify your proxy information and format
3. "Too many attempts" - Wait before trying again (Telegram rate limits)
4. "Phone number already in use" - Use a different phone number or delete existing session

## ⚠️ Important Notes

1. Keep your API credentials private and never share them
2. Telegram has rate limits for session creation
3. Follow Telegram's Terms of Service
4. Proxies must be in the correct format if used
5. Session files contain sensitive authentication data - keep them secure

## 🔧 Advanced Usage

1. You can extend this tool to:
   - Implement multi-user Telegram bots
   - Create automated message senders
   - Develop group management tools
   - Build Telegram marketing tools

2. Recommended best practices:
   - Use session names that help identify accounts
   - Rotate proxies regularly if using automation
   - Keep sessions organized by purpose

## ⚠️ Disclaimer

Use this tool responsibly and in compliance with Telegram's Terms of Service. The author is not responsible for any misuse of this tool or violations of Telegram's policies.