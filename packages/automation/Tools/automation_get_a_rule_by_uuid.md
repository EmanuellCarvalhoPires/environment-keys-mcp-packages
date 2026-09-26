---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/rule-management
  - api/operation/get
  - api/effect/read
up: "[[MCP - Automation]]"
tool: automation_get_a_rule_by_uuid
title: "Automation - Get a rule by UUID"
kind: request
request: "[[Automation - Get a rule by UUID]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · GET /rest/v1/rule/{ruleUuid} · Get a rule by UUID. Performs a request to retrieve the rule with the provided UUID. This includes the rule payload, trigger, components, and other metadata. Writes data: no."
params:
  "ruleUuid":
    type: string
    required: true
    description: "The UUID of the rule to retrieve"
  "product":
    type: string
    required: true
    enum: ["jira", "confluence"]
    description: "Product where the rule runs: jira or confluence."
  "redactSensitiveFields":
    type: string
    required: false
    description: "Indicates if sensitive fields, such as the hidden header values in the send web request action, in the rule config should be redacted. If not set, no fields will be redacted."
writes: false
expose: true
---
# automation_get_a_rule_by_uuid

`GET /rest/v1/rule/{ruleUuid}` — Get a rule by UUID

- Request: [[Automation - Get a rule by UUID]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
