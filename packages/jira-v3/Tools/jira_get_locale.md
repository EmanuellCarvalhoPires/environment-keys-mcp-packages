---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_locale
title: "Jira v3 - Get locale"
kind: request
request: "[[Jira v3 - Get locale]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/mypreferences/locale · Get locale. Returns the locale for the user. If the user has no language preference set (which is the default setting) or this resource is accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale using the Accept-Language header in the request. Writes data: no."
writes: false
expose: false
---
# jira_get_locale

`GET /rest/api/3/mypreferences/locale` — Get locale

- Request: [[Jira v3 - Get locale]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
