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
path: "/rest/devopscomponents/1.0/bulkByProperties"
category: "DevOps Components"
writes_data: true
---
# JSW - Delete DevOps Components by Property

**Delete DevOps Components by Property** — `DELETE /rest/devopscomponents/1.0/bulkByProperties`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete DevOps Components by Property"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/devopscomponents/1.0/bulkByProperties
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Bulk delete all Components that match the given request.

One or more query params must be supplied to specify Properties to delete by.
If more than one Property is provided, data will be deleted that matches ALL of the Properties (e.g. treated as an AND).
See the documentation for the submitComponents operation for more details.

e.g. DELETE /bulkByProperties?accountId=account-123&createdBy=user-456

Deletion is performed asynchronously. The getComponentById operation can be used to confirm that data has been deleted successfully (if needed).

Only Connect apps that define the `jiraDevOpsComponentProvider` module can access this resource.
This resource requires the 'DELETE' scope for Connect apps.
