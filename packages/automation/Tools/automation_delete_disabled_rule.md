---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/delete
  - api/effect/write
up: "[[MCP - Automation]]"
tool: automation_delete_disabled_rule
title: "Automation - Delete disabled rule"
kind: request
request: "[[Automation - Delete disabled rule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · DELETE /rest/v1/rule/{ruleUuid} · Delete disabled rule. Delete a disabled rule by UUID. Writes data: yes."
params:
  "ruleUuid":
    type: string
    required: true
    description: "The UUID of the rule to delete"
  "product":
    type: string
    required: true
    enum: ["jira", "confluence"]
    description: "Product where the rule runs: jira or confluence."
writes: true
expose: false
---
# automation_delete_disabled_rule

`DELETE /rest/v1/rule/{ruleUuid}` — Delete disabled rule

- Request: [[Automation - Delete disabled rule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
