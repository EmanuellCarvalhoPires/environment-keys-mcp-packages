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
path: "/rest/operations/1.0/incidents/{incidentId}"
category: "Operations"
writes_data: true
---
# JSW - Delete a Incident by ID

**Delete a Incident by ID** — `DELETE /rest/operations/1.0/incidents/{incidentId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete a Incident by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/operations/1.0/incidents/{{param:incidentId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `incidentId` (path, string, required) — The ID of the Incident to delete.

## Original description

Delete the Incident data currently stored for the given ID.

Deletion is performed asynchronously. The getIncidentById operation can be used to confirm that data has been deleted successfully (if needed).

Only Connect apps that define the `jiraOperationsInfoProvider` module can access this resource.
This resource requires the 'DELETE' scope for Connect apps.
