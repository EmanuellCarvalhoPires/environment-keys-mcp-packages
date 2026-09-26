---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/operations
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/operations/1.0/linkedWorkspaces/bulk"
category: "Operations"
writes_data: true
---
# JSW - Delete Operations Workpaces by Id

**Delete Operations Workpaces by Id** — `DELETE /rest/operations/1.0/linkedWorkspaces/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete Operations Workpaces by Id"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/operations/1.0/linkedWorkspaces/bulk
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Bulk delete all Operations Workspaces that match the given request.

Only Connect apps that define the `jiraOperationsInfoProvider` module can access this resource.
This resource requires the 'DELETE' scope for Connect apps.

e.g. DELETE /bulk?workspaceIds=111-222-333,444-555-666
