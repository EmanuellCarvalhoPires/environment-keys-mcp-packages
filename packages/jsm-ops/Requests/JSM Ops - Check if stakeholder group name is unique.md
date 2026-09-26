---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/stakeholder-user-management
  - api/operation/get
  - api/effect/read
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: GET
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/validate/name/{name}"
category: "Stakeholder User management"
writes_data: false
---
# JSM Ops - Check if stakeholder group name is unique

**Check if stakeholder group name is unique** — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/validate/name/{name}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Check if stakeholder group name is unique"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholder_groups/validate/name/{{param:name}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `name` (path, string, required) — Name to validate.

## Original description

Check if a stakeholder group name is unique and available for use.
