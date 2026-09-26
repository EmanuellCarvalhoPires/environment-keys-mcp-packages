---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/templates
  - api/operation/get
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_get_template_by_template_id
title: "Automation - Get template by template ID"
kind: request
request: "[[Automation - Get template by template ID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · GET /rest/v1/template/{templateId} · Get template by template ID. Performs a request to retrieve the metadata associated with the provided template ID. This includes any parameters the template has. Writes data: no."
params:
  "templateId":
    type: string
    required: true
    description: "The ID of the template to retrieve"
  "product":
    type: string
    required: true
    enum: ["jira", "confluence"]
    description: "Product where the rule runs: jira or confluence."
writes: false
expose: false
---
# automation_get_template_by_template_id

`GET /rest/v1/template/{templateId}` — Get template by template ID

- Request: [[Automation - Get template by template ID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
