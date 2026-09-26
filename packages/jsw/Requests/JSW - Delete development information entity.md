---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/development-information
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/devinfo/0.10/repository/{repositoryId}/{entityType}/{entityId}"
category: "Development Information"
writes_data: true
---
# JSW - Delete development information entity

**Delete development information entity** — `DELETE /rest/devinfo/0.10/repository/{repositoryId}/{entityType}/{entityId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete development information entity"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/devinfo/0.10/repository/{{param:repositoryId}}/{{param:entityType}}/{{param:entityId}}?_updateSequenceId={{param:_updateSequenceId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repositoryId` (path, string, required) — Value of repositoryId in the path.
- `entityType` (path, string, required) — Value of entityType in the path.
- `entityId` (path, string, required) — Value of entityId in the path.
- `_updateSequenceId` (query, string, optional) — An optional property to use to control deletion. Only stored data with an updateSequenceId less than or equal to that provided will be deleted.

## Original description

Deletes particular development information entity. Deletion is performed asynchronously.
