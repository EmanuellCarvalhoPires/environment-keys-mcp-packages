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
path: "/rest/featureflags/0.1/flag/{featureFlagId}"
category: "Feature Flags"
writes_data: true
---
# JSW - Delete a Feature Flag by ID

**Delete a Feature Flag by ID** — `DELETE /rest/featureflags/0.1/flag/{featureFlagId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete a Feature Flag by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/featureflags/0.1/flag/{{param:featureFlagId}}?_updateSequenceId={{param:_updateSequenceId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `featureFlagId` (path, string, required) — The ID of the Feature Flag to delete.
- `_updateSequenceId` (query, string, optional) — This parameter usage is no longer supported. An optional updateSequenceId to use to control deletion. Only stored data with an updateSequenceId less than or equal to that provided will be deleted.

## Original description

Delete the Feature Flag data currently stored for the given ID.

Deletion is performed asynchronously. The getFeatureFlagById operation can be used to confirm that data has been deleted successfully (if needed).
