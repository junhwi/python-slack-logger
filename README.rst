python-slack-logger
===================
.. image:: https://img.shields.io/pypi/pyversions/slack-logger.svg?maxAge=2592000?style=flat-square
    :target: https://pypi.python.org/pypi/slack-logger

Python logging handler for Slack web hook integration with simple configuration.

Installation
------------
.. code-block:: bash

    pip install slack-logger

Example
-------
.. code-block:: python

  import logging
  from slack_logger import SlackHandler

  sh = SlackHandler('YOUR_WEB_HOOK_URL') # url is like 'https://hooks.slack.com/...'
  logging.basicConfig(handlers=[sh])
  logging.warning('warn message')

  logger = logging.getLogger(__name__)
  sh = SlackHandler(username='logger', icon_emoji=':robot_face:', url='YOUR_WEB_HOOK_URL')
  logger.addHandler(sh)
  logger.warn('warn message')

Next step
---------
Making formatter for better representation in Slack
