---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/get
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_get_custom_field_option
title: "Jira v3 - Get custom field option"
kind: request
request: "[[Jira v3 - Get custom field option]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/customFieldOption/{id} · Get custom field option. Returns a custom field option. For example, an option in a select list. Note that this operation only works for issue field select list options created in Jira or using operations from the Issue custom field options resource, it cannot be used with issue field select list options… Writes data: no."
params:
  "id":
    type: string
    required: true
    description: "The ID of the custom field option."
writes: false
expose: false
---
# jira_get_custom_field_option

`GET /rest/api/3/customFieldOption/{id}` — Get custom field option

- Request: [[Jira v3 - Get custom field option]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
