---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-search
  - api/operation/search
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/issue/picker"
category: "Issue search"
writes_data: false
tool_note: "[[jira_get_issue_picker_suggestions]]"
---
# Jira v3 - Get issue picker suggestions

**Get issue picker suggestions** — `GET /rest/api/3/issue/picker`

- Run by the tool [[jira_get_issue_picker_suggestions]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/issue/picker?query={{param:query}}&currentJQL={{param:currentJQL}}&currentIssueKey={{param:currentIssueKey}}&currentProjectId={{param:currentProjectId}}&showSubTasks={{param:showSubTasks}}&showSubTaskParent={{param:showSubTaskParent}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `query` (query, string, optional) — A string to match against text fields in the issue such as title, description, or comments.
- `currentJQL` (query, string, optional) — A JQL query defining a list of issues to search for the query term. Note that username and userkey cannot be used as search terms for this parameter, due to privacy reasons. Use accountId instead.
- `currentIssueKey` (query, string, optional) — The key of an issue to exclude from search results. For example, the issue the user is viewing when they perform this query.
- `currentProjectId` (query, string, optional) — The ID of a project that suggested issues must belong to.
- `showSubTasks` (query, string, optional) — Indicate whether to include subtasks in the suggestions list.
- `showSubTaskParent` (query, string, optional) — When currentIssueKey is a subtask, whether to include the parent issue in the suggestions if it matches the query.

## Original description

Returns lists of issues matching a query string. Use this resource to provide auto-completion suggestions when the user is looking for an issue using a word or string.

This operation returns two lists:

 *  `History Search` which includes issues from the user's history of created, edited, or viewed issues that contain the string in the `query` parameter.
 *  `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain the string in the `query` parameter.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
