---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/security-information
  - api/operation/get
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/security/1.0/linkedWorkspaces/{workspaceId}"
category: "Security Information"
writes_data: false
---
# JSW - Get a linked Security Workspace by ID

**Get a linked Security Workspace by ID** — `GET /rest/security/1.0/linkedWorkspaces/{workspaceId}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get a linked Security Workspace by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/security/1.0/linkedWorkspaces/{{param:workspaceId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `workspaceId` (path, string, required) — The ID of the workspace to fetch.

## Original description

Retrieve a specific Security Workspace linked to the Jira site for the given workspace ID.

The result will be what is currently stored, ignoring any pending updates or deletes.
