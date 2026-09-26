---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/deployments
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}"
category: "Deployments"
writes_data: true
---
# JSW - Delete a deployment by key

**Delete a deployment by key** — `DELETE /rest/deployments/0.1/pipelines/{pipelineId}/environments/{environmentId}/deployments/{deploymentSequenceNumber}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete a deployment by key"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/deployments/0.1/pipelines/{{param:pipelineId}}/environments/{{param:environmentId}}/deployments/{{param:deploymentSequenceNumber}}?_updateSequenceNumber={{param:_updateSequenceNumber}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `pipelineId` (path, string, required) — The ID of the deployment's pipeline.
- `environmentId` (path, string, required) — The ID of the deployment's environment.
- `deploymentSequenceNumber` (path, string, required) — The deployment's deploymentSequenceNumber.
- `_updateSequenceNumber` (query, string, optional) — This parameter usage is no longer supported. An optional updateSequenceNumber to use to control deletion.

## Original description

Delete the currently stored deployment data for the given `pipelineId`, `environmentId` and `deploymentSequenceNumber` combination.

Deletion is performed asynchronously. The `getDeploymentByKey` operation can be used to confirm that data has been deleted successfully (if needed).
