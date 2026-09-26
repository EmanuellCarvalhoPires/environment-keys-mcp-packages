---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/deployments
  - api/operation/get
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}"
category: "Deployments"
writes_data: false
---
# JSW - Get a deployment by key

**Get a deployment by key** — `GET /rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get a deployment by key"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/deployments/0.1/pipelines/{{param:pipelineId}}/environments/{{param:environmentId}}/deployments/{{param:deploymentSequenceNumber}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pipelineId` (path, string, required) — The ID of the deployment's pipeline.
- `environmentId` (path, string, required) — The ID of the deployment's environment.
- `deploymentSequenceNumber` (path, string, required) — The deployment's deploymentSequenceNumber.

## Original description

Retrieve the currently stored deployment data for the given `pipelineId`, `environmentId` and `deploymentSequenceNumber` combination.

The result will be what is currently stored, ignoring any pending updates or deletes.
