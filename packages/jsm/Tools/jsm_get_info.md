---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jsm
  - api/resource/info
  - api/operation/list
  - api/effect/read
up: "[[MCP - JSM]]"
tool: jsm_get_info
title: "JSM - Get info"
kind: request
request: "[[JSM - Get info]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSM · GET /rest/servicedeskapi/info · Get info. This method retrieves information about the Jira Service Management instance such as software version, builds, and related links. Permissions required: None, the user does not need to be logged in. Writes data: no."
writes: false
expose: false
---
# jsm_get_info

`GET /rest/servicedeskapi/info` — Get info

- Request: [[JSM - Get info]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
