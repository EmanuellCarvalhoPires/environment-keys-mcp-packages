---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-attachments
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_jira_attachment_settings
title: "Jira v3 - Get Jira attachment settings"
kind: request
request: "[[Jira v3 - Get Jira attachment settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/attachment/meta · Get Jira attachment settings. Returns the attachment settings, that is, whether attachments are enabled and the maximum attachment size allowed. Note that there are also project permissions that restrict whether users can create and delete attachments. This operation can be accessed anonymously. Writes data: no."
writes: false
expose: false
---
# jira_get_jira_attachment_settings

`GET /rest/api/3/attachment/meta` — Get Jira attachment settings

- Request: [[Jira v3 - Get Jira attachment settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
