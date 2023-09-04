Automation for Notion (private use)


## Usage

Build (after code change):

```docker build . -t notion_automator```

Run (in detach mode):

```docker run -d --env-file=.env notion_automator```

See logs:

```docker logs <container_id>```

Stop running:

```docker stop <container_id>```
