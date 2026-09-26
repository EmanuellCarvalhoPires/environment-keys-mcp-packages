---
tags:
  - mcp/tool
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
tool: jira_get_issue_picker_suggestions
title: "Jira v3 - Get issue picker suggestions"
kind: request
request: "[[Jira v3 - Get issue picker suggestions]]"
service_tag: atlassian/instance
service_param: instance
service_exclude_tag: template
description: "Jira v3 · GET /rest/api/3/issue/picker · Get issue picker suggestions. Returns lists of issues matching a query string. Use this resource to provide auto-completion suggestions when the user is looking for an issue using a word or string. Writes data: no."
params:
  "query":
    type: string
    required: false
    description: "A string to match against text fields in the issue such as title, description, or comments."
  "currentJQL":
    type: string
    required: false
    description: "A JQL query defining a list of issues to search for the query term. Note that username and userkey cannot be used as search terms for this parameter, due to privacy reasons. Use accountId instead."
  "currentIssueKey":
    type: string
    required: false
    description: "The key of an issue to exclude from search results. For example, the issue the user is viewing when they perform this query."
  "currentProjectId":
    type: string
    required: false
    description: "The ID of a project that suggested issues must belong to."
  "showSubTasks":
    type: string
    required: false
    description: "Indicate whether to include subtasks in the suggestions list."
  "showSubTaskParent":
    type: string
    required: false
    description: "When currentIssueKey is a subtask, whether to include the parent issue in the suggestions if it matches the query."
writes: false
expose: false
---
# jira_get_issue_picker_suggestions

`GET /rest/api/3/issue/picker` — Get issue picker suggestions

- Request: [[Jira v3 - Get issue picker suggestions]]
- Instance: `instance` parameter (notes tagged `atlassian/instance`)
- Writes data: no
