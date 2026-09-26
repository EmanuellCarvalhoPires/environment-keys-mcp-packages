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
path: "/rest/builds/0.1/pipelines/{pipelineId}/builds/{buildNumber}"
category: "Builds"
writes_data: true
---
# JSW - Delete a build by key

**Delete a build by key** — `DELETE /rest/builds/0.1/pipelines/{pipelineId}/builds/{buildNumber}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete a build by key"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/builds/0.1/pipelines/{{param:pipelineId}}/builds/{{param:buildNumber}}?_updateSequenceNumber={{param:_updateSequenceNumber}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pipelineId` (path, string, required) — The pipelineId of the build to delete.
- `buildNumber` (path, string, required) — The buildNumber of the build to delete.
- `_updateSequenceNumber` (query, string, optional) — This parameter usage is no longer supported. An optional updateSequenceNumber to use to control deletion.

## Original description

Delete the build data currently stored for the given `pipelineId` and `buildNumber` combination.

Deletion is performed asynchronously. The `getBuildByKey` operation can be used to confirm that data has been
deleted successfully (if needed).
