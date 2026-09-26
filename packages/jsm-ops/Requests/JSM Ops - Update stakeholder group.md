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
path: "/stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/update"
category: "Stakeholder User management"
writes_data: true
---
# JSM Ops - Update stakeholder group

**Update stakeholder group** — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/update`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"JSM Ops - Update stakeholder group"`.
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

```http
POST https://api.atlassian.com/jsm/ops/stakeholder-comms/cloudId/{{service.cloud_id}}/api/stakeholder_groups/{{param:groupId}}/update
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `groupId` (path, string, required) — Identifier of the stakeholder group.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update a stakeholder group for stakeholder communications.
