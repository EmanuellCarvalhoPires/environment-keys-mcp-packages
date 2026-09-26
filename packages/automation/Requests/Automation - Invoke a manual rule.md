---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/manual-rules
  - api/operation/action
  - api/effect/write
up: "[[MCP - Automation]]"
app: "Automation"
method: POST
path: "/rest/v1/rule/manual/{ruleId}/invocation"
category: "Manual rules"
writes_data: true
tool_note: "[[automation_invoke_a_manual_rule]]"
---
# Automation - Invoke a manual rule

**Invoke a manual rule** — `POST /rest/v1/rule/manual/{ruleId}/invocation`

- Run by the tool [[automation_invoke_a_manual_rule]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
POST {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/manual/{{param:ruleId}}/invocation
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `ruleId` (path, string, required) — Value of ruleId in the path.
- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Invoke a manual rule with one or more target objects and optional inputs.
A rule will be executed for each target object provided.
