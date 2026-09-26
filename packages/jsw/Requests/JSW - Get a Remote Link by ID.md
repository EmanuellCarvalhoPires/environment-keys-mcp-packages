---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/remote-links
  - api/operation/get
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/remotelinks/1.0/remotelink/{remoteLinkId}"
category: "Remote Links"
writes_data: false
---
# JSW - Get a Remote Link by ID

**Get a Remote Link by ID** — `GET /rest/remotelinks/1.0/remotelink/{remoteLinkId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get a Remote Link by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/remotelinks/1.0/remotelink/{{param:remoteLinkId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `remoteLinkId` (path, string, required) — The ID of the Remote Link to fetch.

## Original description

Retrieve the currently stored Remote Link data for the given ID.

The result will be what is currently stored, ignoring any pending updates or deletes.
