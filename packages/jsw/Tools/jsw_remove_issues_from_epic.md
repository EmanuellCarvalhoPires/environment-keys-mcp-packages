---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira-software
  - api/resource/epic
  - api/operation/action
  - api/effect/write
up: "[[MCP - JSW]]"
tool: jsw_remove_issues_from_epic
title: "JSW - Remove issues from epic"
kind: request
request: "[[JSW - Remove issues from epic]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "JSW · POST /rest/agile/1.0/epic/none/issue · Remove issues from epic. Removes issues from epics. The user needs to have the edit issue permission for all issue they want to remove from epics. The maximum number of issues that can be moved in one operation is 50. Note: This operation does not work for epics in next-gen projects. Writes data: yes."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: true
expose: false
---
# jsw_remove_issues_from_epic

`POST /rest/agile/1.0/epic/none/issue` — Remove issues from epic

- Request: [[JSW - Remove issues from epic]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: **yes**
