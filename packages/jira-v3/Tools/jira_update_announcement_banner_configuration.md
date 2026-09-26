---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/announcement-banner
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_update_announcement_banner_configuration
title: "Jira v3 - Update announcement banner configuration"
kind: request
request: "[[Jira v3 - Update announcement banner configuration]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/announcementBanner · Update announcement banner configuration. Updates the announcement banner configuration. Permissions required: Administer Jira global permission. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_update_announcement_banner_configuration

`PUT /rest/api/3/announcementBanner` — Update announcement banner configuration

- Request: [[Jira v3 - Update announcement banner configuration]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
