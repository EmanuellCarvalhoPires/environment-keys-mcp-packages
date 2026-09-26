---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/security-information
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/security/1.0/linkedWorkspaces/bulk"
category: "Security Information"
writes_data: true
---
# JSW - Delete linked Security Workspaces

**Delete linked Security Workspaces** — `DELETE /rest/security/1.0/linkedWorkspaces/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete linked Security Workspaces"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/security/1.0/linkedWorkspaces/bulk
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Bulk delete all linked Security Workspaces that match the given request.

e.g. DELETE /bulk?workspaceIds=111-222-333,444-555-666
