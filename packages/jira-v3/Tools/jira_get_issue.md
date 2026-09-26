---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/get
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue
title: "Jira v3 - Get issue"
kind: request
request: "[[Jira v3 - Get issue]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/{issueIdOrKey} · Get issue. Returns the details for an issue. The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-insensitive search and check for moved issues is performed. Writes data: no."
params:
  "issueIdOrKey":
    type: string
    required: true
    description: "The ID or key of the issue."
  "fields":
    type: string
    required: false
    description: "A list of fields to return for the issue. This parameter accepts a comma-separated list. Use it to retrieve a subset of fields. Allowed values: all Returns all fields."
  "fieldsByKeys":
    type: string
    required: false
    description: "Whether fields in fields are referenced by keys rather than IDs. This parameter is useful where fields have been added by a connect app and a field's key may differ from its ID."
  "expand":
    type: string
    required: false
    description: "Use expand to include additional information about the issues in the response. This parameter accepts a comma-separated list."
  "properties":
    type: string
    required: false
    description: "A list of issue properties to return for the issue. This parameter accepts a comma-separated list. Allowed values: all Returns all issue properties."
  "updateHistory":
    type: string
    required: false
    description: "Whether the project in which the issue is created is added to the user's Recently viewed project list, as shown under Projects in Jira. This also populates the JQL issues search lastViewed field."
  "failFast":
    type: string
    required: false
    description: "Whether to fail the request quickly in case of an error while loading fields for an issue. For failFast=true, if one field fails, the entire operation fails."
writes: false
expose: true
---
# jira_get_issue

`GET /rest/api/3/issue/{issueIdOrKey}` — Get issue

- Request: [[Jira v3 - Get issue]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
