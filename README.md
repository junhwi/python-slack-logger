# python-slack-logger
Python logging handler for Slack web hook integration.

## Example
```python
import logging
from slack_handler import SlackHandler

sh = SlackHandler('YOUR_WEB_HOOK_URL') # url is like 'https://hooks.slack.com/...'
logging.basicConfig(handlers=[sh])
logging.warning('warn message')

logger = logging.getLogger(__name__)
sh = SlackHandler(username='logger', icon_emoji=':robot_face:', url='YOUR_WEB_HOOK_URL')
logger.addHandler(sh)
logger.warn('warn message')
```

## TODO
Making formatter for better representation in Slack
