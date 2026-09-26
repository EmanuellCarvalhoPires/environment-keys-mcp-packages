---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/operations
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/operations/1.0/linkedWorkspaces/bulk"
category: "Operations"
writes_data: true
---
# JSW - Submit Operations Workspace Ids

**Submit Operations Workspace Ids** — `POST /rest/operations/1.0/linkedWorkspaces/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Submit Operations Workspace Ids"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/operations/1.0/linkedWorkspaces/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Insert Operations Workspace IDs to establish a relationship between them and the Jira site the app is installed in. If a relationship between the Workspace ID and Jira already exists then the workspace ID will be ignored and Jira will process the rest of the entries.

Only Connect apps that define the `jiraOperationsInfoProvider` module can access this resource.
This resource requires the 'WRITE' scope for Connect apps.
