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
path: "/stakeholder-comms/cloudId/{cloudId}/api/pages/subdomain/validate/{subdomain}"
category: "Status Page"
writes_data: false
---
# JSM Ops - Check if subdomain is available

**Check if subdomain is available** — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/subdomain/validate/{subdomain}`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"JSM Ops - Check if subdomain is available"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
GET https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/pages/subdomain/validate/{{param:subdomain}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `subdomain` (path, string, required) — Subdomain to validate.

## Original description

Check if a subdomain is available for use.
