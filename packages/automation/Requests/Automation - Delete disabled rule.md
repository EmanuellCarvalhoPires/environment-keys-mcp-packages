---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Automation]]"
app: "Automation"
method: DELETE
path: "/rest/v1/rule/{ruleUuid}"
category: "Rule management"
writes_data: true
tool_note: "[[automation_delete_disabled_rule]]"
---
# Automation - Delete disabled rule

**Delete disabled rule** — `DELETE /rest/v1/rule/{ruleUuid}`

- Run by the tool [[automation_delete_disabled_rule]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
DELETE {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/{{param:ruleUuid}}
Authorization: {{service.auth_token}}
```

## Parameters

- `ruleUuid` (path, string, required) — The UUID of the rule to delete
- `product` (path, string, required) — Product where the rule runs: jira or confluence.

## Original description

Delete a disabled rule by UUID.
