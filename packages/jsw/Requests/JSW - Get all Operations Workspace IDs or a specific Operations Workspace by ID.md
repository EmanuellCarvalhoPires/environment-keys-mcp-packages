---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/operations
  - api/operation/list
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/operations/1.0/linkedWorkspaces"
category: "Operations"
writes_data: false
---
# JSW - Get all Operations Workspace IDs or a specific Operations Workspace by ID

**Get all Operations Workspace IDs or a specific Operations Workspace by ID** — `GET /rest/operations/1.0/linkedWorkspaces`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get all Operations Workspace IDs or a specific Operations Workspace by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/operations/1.0/linkedWorkspaces
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Retrieve the either all Operations Workspace IDs associated with the Jira site or a specific Operations Workspace ID for the given ID.

The result will be what is currently stored, ignoring any pending updates or deletes.

e.g. GET /workspace?workspaceId=111-222-333

Only Connect apps that define the `jiraOperationsInfoProvider` module can access this resource.
This resource requires the 'READ' scope for Connect apps.
