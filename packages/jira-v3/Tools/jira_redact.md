---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-redaction
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_redact
title: "Jira v3 - Redact"
kind: request
request: "[[Jira v3 - Redact]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/redact · Redact. Submit a job to redact issue field data. This will trigger the redaction of the data in the specified fields asynchronously. The redaction status can be polled using the job id. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_redact

`POST /rest/api/3/redact` — Redact

- Request: [[Jira v3 - Redact]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
