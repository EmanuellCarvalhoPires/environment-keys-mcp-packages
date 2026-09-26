---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/templates
  - api/operation/create
  - api/effect/write
up: "[[MCP - Automation]]"
app: "Automation"
method: POST
path: "/rest/v1/template/create"
category: "Templates"
writes_data: true
tool_note: "[[automation_create_a_rule_from_a_template]]"
---
# Automation - Create a rule from a template

**Create a rule from a template** — `POST /rest/v1/template/create`

- Run by the tool [[automation_create_a_rule_from_a_template]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
POST {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/template/create
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `product` (path, string, required) — Product where the rule runs: jira or confluence.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Create a rule from a template. This template may optionally accept parameters.
