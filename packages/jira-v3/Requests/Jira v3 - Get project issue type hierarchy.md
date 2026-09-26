---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/project/{projectId}/hierarchy"
category: "Projects"
writes_data: false
tool_note: "[[jira_get_project_issue_type_hierarchy]]"
---
# Jira v3 - Get project issue type hierarchy

**Get project issue type hierarchy** — `GET /rest/api/3/project/{projectId}/hierarchy`

- Run by the tool [[jira_get_project_issue_type_hierarchy]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/project/{{param:projectId}}/hierarchy
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `projectId` (path, string, required) — The ID of the project.

## Original description

Get the issue type hierarchy for a next-gen project.

The issue type hierarchy for a project consists of:

 *  *Epic* at level 1 (optional).
 *  One or more issue types at level 0 such as *Story*, *Task*, or *Bug*. Where the issue type *Epic* is defined, these issue types are used to break down the content of an epic.
 *  *Subtask* at level -1 (optional). This issue type enables level 0 issue types to be broken down into components. Issues based on a level -1 issue type must have a parent issue.

**[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
