---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/builds
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/builds/0.1/bulk"
category: "Builds"
writes_data: true
---
# JSW - Submit build data

**Submit build data** — `POST /rest/builds/0.1/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Submit build data"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/builds/0.1/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update / insert builds data.

Builds are identified by the combination of `pipelineId` and `buildNumber`, and existing build data for the same
build will be replaced if it exists and the `updateSequenceNumber` of the existing data is less than the
incoming data.

Submissions are performed asynchronously. Submitted data will eventually be available in Jira; most updates are
available within a short period of time, but may take some time during peak load and/or maintenance times.
The `getBuildByKey` operation can be used to confirm that data has been stored successfully (if needed).

In the case of multiple builds being submitted in one request, each is validated individually prior to
submission. Details of which build failed submission (if any) are available in the response object.
