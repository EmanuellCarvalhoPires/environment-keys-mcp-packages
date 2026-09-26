---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-links
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
tool: jira_create_issue_link
title: "Jira v3 - Create issue link"
kind: request
request: "[[Jira v3 - Create issue link]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/api/3/issueLink · Create issue link. Creates a link between two issues. Use this operation to indicate a relationship between two issues and optionally add a comment to the from (outward) issue. To use this resource the site must have Issue Linking enabled. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jira_create_issue_link

`POST /rest/api/3/issueLink` — Create issue link

- Request: [[Jira v3 - Create issue link]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
