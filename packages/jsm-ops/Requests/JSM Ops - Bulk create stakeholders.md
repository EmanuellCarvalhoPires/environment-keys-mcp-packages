---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm-ops
  - api/resource/stakeholder-user-management
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSM Ops]]"
app: "JSM Ops"
method: POST
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholders/bulk"
category: "Stakeholder User management"
writes_data: true
---
# JSM Ops - Bulk create stakeholders

**Bulk create stakeholders** — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/bulk`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Bulk create stakeholders"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholders/bulk
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create multiple stakeholders in Stakeholder Comms.
