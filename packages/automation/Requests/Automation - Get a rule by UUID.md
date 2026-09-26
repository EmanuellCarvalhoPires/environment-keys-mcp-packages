---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/get
  - api/effect/read
up: "[[MCP - Automation]]"
app: "Automation"
method: GET
path: "/rest/v1/rule/{ruleUuid}"
category: "Rule management"
writes_data: false
tool_note: "[[automation_get_a_rule_by_uuid]]"
---
# Automation - Get a rule by UUID

**Get a rule by UUID** — `GET /rest/v1/rule/{ruleUuid}`

- Run by the tool [[automation_get_a_rule_by_uuid]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
GET {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/{{param:ruleUuid}}?redactSensitiveFields={{param:redactSensitiveFields}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `ruleUuid` (path, string, required) — The UUID of the rule to retrieve
- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `redactSensitiveFields` (query, string, optional) — Indicates if sensitive fields, such as the hidden header values in the send web request action, in the rule config should be redacted. If not set, no fields will be redacted.

## Original description

Performs a request to retrieve the rule with the provided UUID.
This includes the rule payload, trigger, components, and other metadata.
