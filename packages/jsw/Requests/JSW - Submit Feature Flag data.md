---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/feature-flags
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/featureflags/0.1/bulk"
category: "Feature Flags"
writes_data: true
---
# JSW - Submit Feature Flag data

**Submit Feature Flag data** — `POST /rest/featureflags/0.1/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Submit Feature Flag data"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/featureflags/0.1/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update / insert Feature Flag data.

Feature Flags are identified by their ID, and existing Feature Flag data for the same ID will be replaced if it exists and the updateSequenceId of existing data is less than the incoming data.

Submissions are performed asynchronously. Submitted data will eventually be available in Jira; most updates are available within a short period of time, but may take some time during peak load and/or maintenance times. The getFeatureFlagById operation can be used to confirm that data has been stored successfully (if needed).

In the case of multiple Feature Flags being submitted in one request, each is validated individually prior to submission. Details of which Feature Flags failed submission (if any) are available in the response object.
