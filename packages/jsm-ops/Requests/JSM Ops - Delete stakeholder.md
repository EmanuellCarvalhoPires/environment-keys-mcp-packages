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
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholders/{stakeholderId}/delete"
category: "Stakeholder User management"
writes_data: true
---
# JSM Ops - Delete stakeholder

**Delete stakeholder** — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/{stakeholderId}/delete`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Delete stakeholder"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholders/{{param:stakeholderId}}/delete
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `stakeholderId` (path, string, required) — Identifier of the stakeholder.

## Original description

Delete a stakeholder from stakeholder communications.
