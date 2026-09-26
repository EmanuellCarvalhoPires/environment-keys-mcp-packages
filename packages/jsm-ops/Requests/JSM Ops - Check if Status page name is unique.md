---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/status-page
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/validate/name/{name}"
category: "Status Page"
writes_data: false
---
# JSM Ops - Check if Status page name is unique

**Check if Status page name is unique** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/validate/name/{name}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Check if Status page name is unique"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/validate/name/{{param:name}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `name` (path, string, required) — Name to validate.

## Original description

Check if a page name is unique and available for use.
