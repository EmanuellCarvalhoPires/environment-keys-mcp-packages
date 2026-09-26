---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-settings
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_advanced_settings
title: "Jira v3 - Get advanced settings"
kind: request
request: "[[Jira v3 - Get advanced settings]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/application-properties/advanced-settings · Get advanced settings. Returns the application properties that are accessible on the Advanced Settings page. To navigate to the Advanced Settings page in Jira, choose the Jira icon Jira settings System, General Configuration and then click Advanced Settings (in the upper right). Writes data: no."
writes: false
expose: false
---
# jira_get_advanced_settings

`GET /rest/api/3/application-properties/advanced-settings` — Get advanced settings

- Request: [[Jira v3 - Get advanced settings]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
