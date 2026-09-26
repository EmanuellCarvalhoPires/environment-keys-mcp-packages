---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/builds
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/builds/0.1/bulkByProperties"
category: "Builds"
writes_data: true
---
# JSW - Delete builds by Property

**Delete builds by Property** — `DELETE /rest/builds/0.1/bulkByProperties`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete builds by Property"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/builds/0.1/bulkByProperties?_updateSequenceNumber={{param:_updateSequenceNumber}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `_updateSequenceNumber` (query, string, optional) — This parameter usage is no longer supported. An optional updateSequenceNumber to use to control deletion.

## Original description

Bulk delete all builds data that match the given request.

One or more query params must be supplied to specify Properties to delete by.
Optional param `_updateSequenceNumber` is no longer supported.
If more than one Property is provided, data will be deleted that matches ALL of the
Properties (e.g. treated as an AND).

See the documentation for the `submitBuilds` operation for more details.

e.g. DELETE /bulkByProperties?accountId=account-123&repoId=repo-345

Deletion is performed asynchronously. The `getBuildByKey` operation can be used to confirm that data has been
deleted successfully (if needed).
