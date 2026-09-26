---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/devops-components
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/devopscomponents/1.0/devopscomponents/{componentId}"
category: "DevOps Components"
writes_data: true
---
# JSW - Delete a Component by ID

**Delete a Component by ID** — `DELETE /rest/devopscomponents/1.0/devopscomponents/{componentId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete a Component by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/devopscomponents/1.0/devopscomponents/{{param:componentId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `componentId` (path, string, required) — The ID of the Component to delete.

## Original description

Delete the Component data currently stored for the given ID.

Deletion is performed asynchronously. The getComponentById operation can be used to confirm that data has been deleted successfully (if needed).

Only Connect apps that define the `jiraDevOpsComponentProvider` module can access this resource.
This resource requires the 'DELETE' scope for Connect apps.
