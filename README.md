# Discord Person Detect

Fun project to get discord notification when a person is detected on a webcam. Works in semi-realtime. Yolos-tiny is quite an intensive model so can be a little slow, but does the job!

### Discord Setup

* Click the settings icon on the channel where you want the alerts on.

![image](https://github.com/RoryGracey/discord-person-detect-webhook/assets/47629117/cdeecdbf-2bb6-4662-afcb-2bd8c6f45c73)

* Click `Integrations`

* Click `Webooks`

* Click `New Webhook`

* Copy Webhook url

Once you've got the URL create a .env file in the source directory of the `discord-person-detect-webhook` directory.

In there create a `url` environment variable and a `alert_id` environment variable.

The `url` is the webook url and the `alert_id` is the user_id of discord user you want to notify (probably your own).

Your .env file should look like this.

```
url=https://discord.com/api/webhooks/<>/<>
alert_id=1234567890
```

### Python Installation

*Tested on Python `3.12.1`*

Create VirtualEnv

```python
python -m venv object-detection
source object-detection/Scripts/activate
```

Install Requirements

```python
python -m pip install -r requirements.txt
```

Run script with webcam plugged in

```
python main.py
```
