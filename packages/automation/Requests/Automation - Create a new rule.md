---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/create
  - api/effect/write
up: "[[MCP - Automation]]"
app: "Automation"
method: POST
path: "/rest/v1/rule"
category: "Rule management"
writes_data: true
tool_note: "[[automation_create_a_new_rule]]"
---
# Automation - Create a new rule

**Create a new rule** — `POST /rest/v1/rule`

- Run by the tool [[automation_create_a_new_rule]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
POST {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a new rule from the provided Rule Payload.

If providing a UUID for your new rule, it must be unique and V7. The time-based nature of V7 will impact sorting and pagination of your rule.

Accepts a rule payload, which has the same structure as the get a rule by UUID response.
