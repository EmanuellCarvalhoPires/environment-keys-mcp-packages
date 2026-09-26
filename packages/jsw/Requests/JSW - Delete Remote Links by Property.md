---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/remote-links
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/remotelinks/1.0/bulkByProperties"
category: "Remote Links"
writes_data: true
---
# JSW - Delete Remote Links by Property

**Delete Remote Links by Property** — `DELETE /rest/remotelinks/1.0/bulkByProperties`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete Remote Links by Property"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/remotelinks/1.0/bulkByProperties?_updateSequenceNumber={{param:_updateSequenceNumber}}&params={{param:params}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `_updateSequenceNumber` (query, string, optional) — This parameter usage is no longer supported. An optional updateSequenceNumber to use to control deletion.
- `params` (query, string, optional) — Free-form query parameters to specify which properties to delete by. Properties refer to the arbitrary information the provider tagged Remote Links with previously.

## Original description

Bulk delete all Remote Links data that match the given request.

One or more query params must be supplied to specify Properties to delete by.
Optional param `_updateSequenceNumber` is no longer supported. If more than one Property is provided,
data will be deleted that matches ALL of the Properties (e.g. treated as an AND).

See the documentation for the `submitRemoteLinks` operation for more details.

e.g. DELETE /bulkByProperties?accountId=account-123&repoId=repo-345

Deletion is performed asynchronously. The `getRemoteLinkById` operation can be used to confirm that data has been
deleted successfully (if needed).
