---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/remote-links
  - api/operation/delete
  - api/effect/write
  - api/restriction/oauth-devops
up: "[[MCP - JSW]]"
app: "JSW"
method: DELETE
path: "/rest/remotelinks/1.0/remotelink/{remoteLinkId}"
category: "Remote Links"
writes_data: true
---
# JSW - Delete a Remote Link by ID

**Delete a Remote Link by ID** — `DELETE /rest/remotelinks/1.0/remotelink/{remoteLinkId}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSW - Delete a Remote Link by ID"`.
- **Restriction:** DevOps integration API; requires app OAuth 2.0 / JWT credentials, not the user Basic token.
- Official documentation: https://developer.atlassian.com/cloud/jira/software/rest/

```http
DELETE {{service.url}}/rest/remotelinks/1.0/remotelink/{{param:remoteLinkId}}?_updateSequenceNumber={{param:_updateSequenceNumber}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `remoteLinkId` (path, string, required) — The ID of the Remote Link to fetch.
- `_updateSequenceNumber` (query, string, optional) — This parameter usage is no longer supported. An optional updateSequenceNumber to use to control deletion.

## Original description

Delete the Remote Link data currently stored for the given ID.

Deletion is performed asynchronously. The `getRemoteLinkById` operation can be used to confirm that data has been
deleted successfully (if needed).
