---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/jql
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_field_auto_complete_suggestions
title: "Jira v3 - Get field auto complete suggestions"
kind: request
request: "[[Jira v3 - Get field auto complete suggestions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/jql/autocompletedata/suggestions · Get field auto complete suggestions. Returns the JQL search auto complete suggestions for a field. Suggestions can be obtained by providing: fieldName to get a list of all values for the field. fieldName and fieldValue to get a list of values containing the text in fieldValue. Writes data: no."
params:
  "fieldName":
    type: string
    required: false
    description: "The name of the field."
  "fieldValue":
    type: string
    required: false
    description: "The partial field item name entered by the user."
  "predicateName":
    type: string
    required: false
    description: "The name of the CHANGED operator predicate for which the suggestions are generated. The valid predicate operators are by, from, and to."
  "predicateValue":
    type: string
    required: false
    description: "The partial predicate item name entered by the user."
writes: false
expose: false
---
# jira_get_field_auto_complete_suggestions

`GET /rest/api/3/jql/autocompletedata/suggestions` — Get field auto complete suggestions

- Request: [[Jira v3 - Get field auto complete suggestions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
