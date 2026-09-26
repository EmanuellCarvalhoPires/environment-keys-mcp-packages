---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/security-information
  - api/operation/list
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/security/1.0/linkedWorkspaces"
category: "Security Information"
writes_data: false
---
# JSW - Get linked Security Workspaces

**Get linked Security Workspaces** — `GET /rest/security/1.0/linkedWorkspaces`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get linked Security Workspaces"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/security/1.0/linkedWorkspaces
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Retrieve all Security Workspaces linked with the Jira site.

The result will be what is currently stored, ignoring any pending updates or deletes.
