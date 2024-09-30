###Launch server:

```bash
nohup fastapi run app/main.py --reload --port 8281 &
```

### Config:

`MATTERMOST_URL` - webhook link to MM channel
`BLOCKFROST_API_KEY` - api key for blockfrost
`PAYERS` - payers data (should be edited)

`during_day_interval` - daily check
`timezone` - timezone for app

```bash
ps aux | grep fastapi
```

```bash
pkill -f fastapi
```