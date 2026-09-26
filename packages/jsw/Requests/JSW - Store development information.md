---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/development-information
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/devinfo/0.10/bulk"
category: "Development Information"
writes_data: true
---
# JSW - Store development information

**Store development information** — `POST /rest/devinfo/0.10/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Store development information"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/devinfo/0.10/bulk
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Stores development information provided in the request to make it available when viewing issues in Jira. Existing repository and entity data for the same ID will be replaced if the updateSequenceId of existing data is less than the incoming data. Submissions are performed asynchronously. Submitted data will eventually be available in Jira; most updates are available within a short period of time, but may take some time during peak load and/or maintenance times.
