---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options
  - api/operation/delete
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
tool: jira_replace_custom_field_options
title: "Jira v3 - Replace custom field options"
kind: request
request: "[[Jira v3 - Replace custom field options]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue · Replace custom field options. Replaces the options of a custom field. Note that this operation only works for issue field select list options created in Jira or using operations from the Issue custom field options resource, it cannot be used with issue field select list options created by Connect or Forge app… Writes data: yes."
params:
  "fieldId":
    type: string
    required: true
    description: "The ID of the custom field."
  "contextId":
    type: string
    required: true
    description: "The ID of the context."
  "optionId":
    type: string
    required: true
    description: "The ID of the option to be deselected."
  "replaceWith":
    type: string
    required: false
    description: "The ID of the option that will replace the currently selected option."
  "jql":
    type: string
    required: false
    description: "A JQL query that specifies the issues to be updated. For example, project=10000."
writes: true
expose: false
---
# jira_replace_custom_field_options

`DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue` — Replace custom field options

- Request: [[Jira v3 - Replace custom field options]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
