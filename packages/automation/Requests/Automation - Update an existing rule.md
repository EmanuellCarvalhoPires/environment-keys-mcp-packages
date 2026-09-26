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
path: "/rest/v1/rule/{ruleUuid}"
category: "Rule management"
writes_data: true
tool_note: "[[automation_update_an_existing_rule]]"
---
# Automation - Update an existing rule

**Update an existing rule** — `PUT /rest/v1/rule/{ruleUuid}`

- Run by the tool [[automation_update_an_existing_rule]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
PUT {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/rule/{{param:ruleUuid}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `ruleUuid` (path, string, required) — The UUID of the rule to update
- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates an existing rule by accepting a rule payload, which has the same structure as the get a rule by UUID response.
ComponentIds are only required for pre-existing components.
New components will be created or deleted as needed.
