---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/other-operations
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_worklogs_by_issue_id_and_worklog_id
title: "Jira v3 - Get worklogs by issue id and worklog id"
kind: request
request: "[[Jira v3 - Get worklogs by issue id and worklog id]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · POST /rest/internal/api/latest/worklog/bulk · Get worklogs by issue id and worklog id. Returns worklog details for a list of issue ID and worklog ID pairs. This is an internal API for bulk fetching worklogs by their issue and worklog IDs. Worklogs that don't exist will be filtered out from the response. The returned list of worklogs is limited to 1000 items. Writes data: no."
params:
  "body":
    type: object
    required: true
    description: "JSON request body. See the example in the request note."
writes: false
expose: false
---
# jira_get_worklogs_by_issue_id_and_worklog_id

`POST /rest/internal/api/latest/worklog/bulk` — Get worklogs by issue id and worklog id

- Request: [[Jira v3 - Get worklogs by issue id and worklog id]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
