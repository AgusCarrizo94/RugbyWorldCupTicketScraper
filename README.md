# RugbyWorldCupTicketScraper

Scraper script that returns available tickets in specific matchs of the Rugby World Cup 2023.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install beautifulsoup4 and msgWsp.

```bash
pip install beautifulsoup4 msgWsp
```

## Usage

Set the URLs of the matches where you want to obtain if there are available tickets.

```python
# main.py

import requests
from bs4 import BeautifulSoup
from msgWsp import whatsAppMessage

URL1 = "https://tickets.rugbyworldcup.com/en/resale_italy_uruguay"
URL2 = "https://tickets.rugbyworldcup.com/en/resale_quarter_final1"
URL3 = "https://tickets.rugbyworldcup.com/en/resale_semi_final2"
URL4 = "https://tickets.rugbyworldcup.com/en/resale_final"

URLs = [URL1, URL2, URL3, URL4]
```

Set the chat code from the whatsapp chat or group and replace CHATCODE.

```python
# msgWsp.py

import pywhatkit

def whatsAppMessage(message):
    pywhatkit.sendwhatmsg_to_group_instantly("CHATCODE", message, tab_close=True)
```
Run main.py in bash.

```bash
py main.py
```
