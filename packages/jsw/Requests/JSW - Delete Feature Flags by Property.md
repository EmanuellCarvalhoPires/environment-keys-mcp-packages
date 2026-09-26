---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/feature-flags
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/featureflags/0.1/bulkByProperties"
category: "Feature Flags"
writes_data: true
---
# JSW - Delete Feature Flags by Property

**Delete Feature Flags by Property** — `DELETE /rest/featureflags/0.1/bulkByProperties`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete Feature Flags by Property"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/featureflags/0.1/bulkByProperties?_updateSequenceId={{param:_updateSequenceId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `_updateSequenceId` (query, string, optional) — This parameter usage is no longer supported. An optional updateSequenceId to use to control deletion. Only stored data with an updateSequenceId less than or equal to that provided will be deleted.

## Original description

Bulk delete all Feature Flags that match the given request.

One or more query params must be supplied to specify Properties to delete by. Optional param `_updateSequenceId` is no longer supported.
If more than one Property is provided, data will be deleted that matches ALL of the Properties (e.g. treated as an AND).
See the documentation for the submitFeatureFlags operation for more details.

e.g. DELETE /bulkByProperties?accountId=account-123&createdBy=user-456

Deletion is performed asynchronously. The getFeatureFlagById operation can be used to confirm that data has been deleted successfully (if needed).
