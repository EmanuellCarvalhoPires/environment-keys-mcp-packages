---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/operations
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/operations/1.0/bulk"
category: "Operations"
writes_data: true
---
# JSW - Submit Incident or Review data

**Submit Incident or Review data** — `POST /rest/operations/1.0/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Submit Incident or Review data"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/operations/1.0/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update / insert Incident or Review data.

Incidents and reviews are identified by their ID, and existing Incident and Review data for the same ID will be replaced if it exists and the updateSequenceNumber of existing data is less than the incoming data.

Submissions are performed asynchronously. Submitted data will eventually be available in Jira; most updates are available within a short period of time, but may take some time during peak load and/or maintenance times. The getIncidentById or getReviewById operation can be used to confirm that data has been stored successfully (if needed).

In the case of multiple Incidents and Reviews being submitted in one request, each is validated individually prior to submission. Details of which entities failed submission (if any) are available in the response object.

A maximum of 1000 incidents can be submitted in one request.

Only Connect apps that define the `jiraOperationsInfoProvider` module can access this resource.
This resource requires the 'WRITE' scope for Connect apps.
