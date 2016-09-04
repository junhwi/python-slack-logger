import json
from urllib.parse import urlparse
from logging.handlers import HTTPHandler


class SlackHandler(HTTPHandler):

  def __init__(self, url, username=None, icon_url=None, icon_emoji=None, channel=None):
    o = urlparse(url)
    is_secure = o.scheme == 'https'
    HTTPHandler.__init__(self, o.netloc, o.path, method="POST", secure=is_secure)
    self.username = username
    self.icon_url = icon_url
    self.icon_emoji = icon_emoji
    self.channel = channel

  def mapLogRecord(self, record):
    payload = {
      'text': self.format(record),
    }
    if self.username:
      payload['username'] = self.username
    if self.icon_url:
      payload['icon_url'] = self.icon_url
    if self.icon_emoji:
      payload['icon_emoji'] = self.icon_emoji
    if self.channel:
      payload['channel'] = self.channel

    ret = {
      'payload': json.dumps(payload),
    }
    return ret
