---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/security-information
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/security/1.0/linkedWorkspaces/bulk"
category: "Security Information"
writes_data: true
---
# JSW - Submit Security Workspaces to link

**Submit Security Workspaces to link** — `POST /rest/security/1.0/linkedWorkspaces/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Submit Security Workspaces to link"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/security/1.0/linkedWorkspaces/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Insert Security Workspace IDs to establish a relationship between them and the Jira site the app is installed on. If a relationship between the workspace ID and Jira already exists then the workspace ID will be ignored and Jira will process the rest of the entries.
