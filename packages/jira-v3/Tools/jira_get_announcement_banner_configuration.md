---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/announcement-banner
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_announcement_banner_configuration
title: "Jira v3 - Get announcement banner configuration"
kind: request
request: "[[Jira v3 - Get announcement banner configuration]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/announcementBanner · Get announcement banner configuration. Returns the current announcement banner configuration. Permissions required: Administer Jira global permission. Writes data: no."
writes: false
expose: false
---
# jira_get_announcement_banner_configuration

`GET /rest/api/3/announcementBanner` — Get announcement banner configuration

- Request: [[Jira v3 - Get announcement banner configuration]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
