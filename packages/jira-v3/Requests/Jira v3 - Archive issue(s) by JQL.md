---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/action
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/archive"
category: "Issues"
writes_data: true
tool_note: "[[jira_archive_issue_s_by_jql]]"
---
# Jira v3 - Archive issue(s) by JQL

**Archive issue(s) by JQL** — `POST /rest/api/3/issue/archive`

- Run by the tool [[jira_archive_issue_s_by_jql]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/archive
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "jql": "project = FOO AND updated < -2y"
}
```

## Original description

Enables admins to archive up to 100,000 issues in a single request using JQL, returning the URL to check the status of the submitted request.

You can use the [get task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-get) and [cancel task](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-tasks/#api-rest-api-3-task-taskid-cancel-post) APIs to manage the request.

**Note that:**

 *  you can't archive subtasks directly, only through their parent issues
 *  you can only archive issues from software, service management, and business projects

**[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

**License required:** Premium or Enterprise

**Signed-in users only:** This API can't be accessed anonymously.

**Rate limiting:** Only a single request per jira instance can be active at any given time.
