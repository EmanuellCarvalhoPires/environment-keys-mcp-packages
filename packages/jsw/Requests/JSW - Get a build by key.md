---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/builds
  - api/operation/get
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/builds/0.1/pipelines/{pipelineId}/builds/{buildNumber}"
category: "Builds"
writes_data: false
---
# JSW - Get a build by key

**Get a build by key** — `GET /rest/builds/0.1/pipelines/{pipelineId}/builds/{buildNumber}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get a build by key"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/builds/0.1/pipelines/{{param:pipelineId}}/builds/{{param:buildNumber}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pipelineId` (path, string, required) — The pipelineId of the build.
- `buildNumber` (path, string, required) — The buildNumber of the build.

## Original description

Retrieve the currently stored build data for the given `pipelineId` and `buildNumber` combination.

The result will be what is currently stored, ignoring any pending updates or deletes.
