---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/update
  - api/effect/write
up: "[[MCP - Automation]]"
app: "Automation"
method: PUT
path: "/rest/v1/rule/{ruleUuid}/state"
category: "Rule management"
writes_data: true
tool_note: "[[automation_enable_or_disable_a_rule]]"
---
# Automation - Enable or disable a rule

**Enable or disable a rule** — `PUT /rest/v1/rule/{ruleUuid}/state`

- Run by the tool [[automation_enable_or_disable_a_rule]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
PUT {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/{{param:ruleUuid}}/state
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `ruleUuid` (path, string, required) — Value of ruleUuid in the path.
- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Enable or disable a rule by rule UUID.
