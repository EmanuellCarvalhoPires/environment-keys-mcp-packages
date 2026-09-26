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
tool: jira_get_application_property
title: "Jira v3 - Get application property"
kind: request
request: "[[Jira v3 - Get application property]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/application-properties · Get application property. Returns all application properties or an application property. If you specify a value for the key parameter, then an application property is returned as an object (not in an array). Otherwise, an array of all editable application properties is returned. Writes data: no."
params:
  "key":
    type: string
    required: false
    description: "The key of the application property."
  "permissionLevel":
    type: string
    required: false
    description: "The permission level of all items being returned in the list."
  "keyFilter":
    type: string
    required: false
    description: "When a key isn't provided, this filters the list of results by the application property key using a regular expression. For example, using jira.lf."
writes: false
expose: false
---
# jira_get_application_property

`GET /rest/api/3/application-properties` — Get application property

- Request: [[Jira v3 - Get application property]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
