---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/automation
  - api/resource/manual-rules
  - api/operation/action
  - api/effect/write
up: "[[MCP - Automation]]"
tool: automation_invoke_a_manual_rule
title: "Automation - Invoke a manual rule"
kind: request
request: "[[Automation - Invoke a manual rule]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Automation · POST /rest/v1/rule/manual/{ruleId}/invocation · Invoke a manual rule. Invoke a manual rule with one or more target objects and optional inputs. A rule will be executed for each target object provided. Writes data: yes."
params:
  "ruleId":
    type: string
    required: true
    description: "Value of ruleId in the path."
  "product":
    type: string
    required: true
    enum: ["jira", "confluence"]
    description: "Product where the rule runs: jira or confluence."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: true
---
# automation_invoke_a_manual_rule

`POST /rest/v1/rule/manual/{ruleId}/invocation` — Invoke a manual rule

- Request: [[Automation - Invoke a manual rule]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
