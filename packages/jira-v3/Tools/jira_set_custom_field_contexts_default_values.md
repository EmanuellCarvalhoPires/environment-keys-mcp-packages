---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_set_custom_field_contexts_default_values
title: "Jira v3 - Set custom field contexts default values"
kind: request
request: "[[Jira v3 - Set custom field contexts default values]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · PUT /rest/api/3/field/{fieldId}/context/defaultValue · Set custom field contexts default values. Sets default for contexts of a custom field. Default are defined using these objects: CustomFieldContextDefaultValueDate (type datepicker) for date fields. CustomFieldContextDefaultValueDateTime (type datetimepicker) for date-time fields. Writes data: yes."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_set_custom_field_contexts_default_values

`PUT /rest/api/3/field/{fieldId}/context/defaultValue` — Set custom field contexts default values

- Request: [[Jira v3 - Set custom field contexts default values]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
