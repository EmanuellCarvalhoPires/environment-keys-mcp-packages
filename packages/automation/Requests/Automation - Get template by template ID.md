---
tags:
  - api/request
  - api/service/atlassian
  - api/app/automation
  - api/resource/templates
  - api/operation/get
  - api/effect/read
up: "[[MCP - Automation]]"
app: "Automation"
method: GET
path: "/rest/v1/template/{templateId}"
category: "Templates"
writes_data: false
tool_note: "[[automation_get_template_by_template_id]]"
---
# Automation - Get template by template ID

**Get template by template ID** — `GET /rest/v1/template/{templateId}`

- Run by the tool [[automation_get_template_by_template_id]].
- Official documentation: https://developer.atlassian.com/cloud/automation/rest/

```http
GET {{service.url}}/gateway/api/automation/public/{{param:product}}/{{service.cloud_id}}/rest/v1/template/{{param:templateId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `templateId` (path, string, required) — The ID of the template to retrieve
- `product` (path, string, required) — Product where the rule runs: jira or confluence.

## Original description

Performs a request to retrieve the metadata associated with the provided template ID.
This includes any parameters the template has.
