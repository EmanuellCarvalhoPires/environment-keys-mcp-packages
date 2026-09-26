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
path: "/rest/devinfo/0.10/repository/{repositoryId}"
category: "Development Information"
writes_data: true
---
# JSW - Delete repository

**Delete repository** — `DELETE /rest/devinfo/0.10/repository/{repositoryId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete repository"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/devinfo/0.10/repository/{{param:repositoryId}}?_updateSequenceId={{param:_updateSequenceId}}
Authorization: {{service.auth_token}}
```

## Parameters

- `repositoryId` (path, string, required) — The ID of repository to delete
- `_updateSequenceId` (query, string, optional) — An optional property to use to control deletion. Only stored data with an updateSequenceId less than or equal to that provided will be deleted.

## Original description

Deletes the repository data stored by the given ID and all related development information entities. Deletion is performed asynchronously.
