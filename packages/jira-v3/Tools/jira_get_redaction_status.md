---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-redaction
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_redaction_status
title: "Jira v3 - Get redaction status"
kind: request
request: "[[Jira v3 - Get redaction status]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/redact/status/{jobId} · Get redaction status. Retrieves the current status of a redaction job ID. The jobStatus will be one of the following: IN\\PROGRESS - The redaction job is currently in progress COMPLETED - The redaction job has completed successfully. PENDING - The redaction job has not started yet Writes data: no."
params:
  "jobId":
    type: string
    required: true
    description: "Redaction job id"
writes: false
expose: false
---
# jira_get_redaction_status

`GET /rest/api/3/redact/status/{jobId}` — Get redaction status

- Request: [[Jira v3 - Get redaction status]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
