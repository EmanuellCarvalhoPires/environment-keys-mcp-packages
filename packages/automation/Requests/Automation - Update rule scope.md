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
path: "/rest/v1/rule/{ruleUuid}/rule-scope"
category: "Rule management"
writes_data: true
tool_note: "[[automation_update_rule_scope]]"
---
# Automation - Update rule scope

**Update rule scope** — `PUT /rest/v1/rule/{ruleUuid}/rule-scope`

- Run by the tool [[automation_update_rule_scope]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
PUT {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/{{param:ruleUuid}}/rule-scope
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `ruleUuid` (path, string, required) — Value of ruleUuid in the path.
- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Update the scope of a rule by UUID.
