---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/remote-links
  - api/operation/action
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: POST
path: "/rest/remotelinks/1.0/bulk"
category: "Remote Links"
writes_data: true
---
# JSW - Submit Remote Link data

**Submit Remote Link data** — `POST /rest/remotelinks/1.0/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Submit Remote Link data"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
POST {{service.url}}/rest/remotelinks/1.0/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update / insert Remote Link data.

Remote Links are identified by their ID, existing Remote Link data for the same ID will be replaced if it
exists and the updateSequenceId of existing data is less than the incoming data.

Submissions are performed asynchronously. Submitted data will eventually be available in Jira; most updates are
available within a short period of time, but may take some time during peak load and/or maintenance times.
The `getRemoteLinkById` operation can be used to confirm that data has been stored successfully (if needed).

In the case of multiple Remote Links being submitted in one request, each is validated individually prior to
submission. Details of which Remote LInk failed submission (if any) are available in the response object.
