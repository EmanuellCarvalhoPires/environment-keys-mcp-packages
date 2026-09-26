---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/deployments
  - api/operation/list
  - api/effect/read
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: GET
path: "/rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}/gating-status"
category: "Deployments"
writes_data: false
---
# JSW - Get deployment gating status by key

**Get deployment gating status by key** — `GET /rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}/gating-status`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSW - Get deployment gating status by key"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
GET {{service.url}}/rest/deployments/0.1/pipelines/{{param:pipelineId}}/environments/{{param:environmentId}}/deployments/{{param:deploymentSequenceNumber}}/gating-status
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pipelineId` (path, string, required) — The ID of the Deployment's pipeline.
- `environmentId` (path, string, required) — The ID of the Deployment's environment.
- `deploymentSequenceNumber` (path, string, required) — The Deployment's deploymentSequenceNumber.

## Original description

Retrieve the  Deployment gating status for the given `pipelineId + environmentId + deploymentSequenceNumber` combination.
Only apps that define the `jiraDeploymentInfoProvider` module can access this resource. This resource requires the 'READ' scope.
