---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/deployments
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/deployments/0.1/bulk"
category: "Deployments"
writes_data: true
---
# JSW - Submit deployment data

**Submit deployment data** — `POST /rest/deployments/0.1/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Submit deployment data"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/deployments/0.1/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update / insert deployment data.

Deployments are identified by the combination of `pipelineId`, `environmentId` and `deploymentSequenceNumber`, and existing deployment data for the same deployment will be replaced if it exists and the `updateSequenceNumber` of existing data is less than the incoming data.

Submissions are processed asynchronously. Submitted data will eventually be available in Jira. Most updates are available within a short period of time, but may take some time during peak load and/or maintenance times. The `getDeploymentByKey` operation can be used to confirm that data has been stored successfully (if needed).

In the case of multiple deployments being submitted in one request, each is validated individually prior to submission. Details of which deployments failed submission (if any) are available in the response object.
