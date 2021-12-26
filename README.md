# DRPC
Discord Rich Presence Client with **everything you will need** in your presence
## Quick start
First, set your Client ID (found [here](https://discord.com/developers/applications)) in `main.py` file.<br>
Then, set everything in this line:
```python
rpclient.update(buttons=[{"label": "Label", "url": "URL"}], details="Details")
```