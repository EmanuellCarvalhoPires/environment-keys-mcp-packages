---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/archive"
category: "Issues"
writes_data: true
tool_note: "[[jira_archive_issue_s_by_issue_id_key]]"
---
# Jira v3 - Archive issue(s) by issue ID key

**Archive issue(s) by issue ID/key** — `PUT /rest/api/3/issue/archive`

- Run by the tool [[jira_archive_issue_s_by_issue_id_key]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/archive
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "issueIdsOrKeys": [
    "PR-1",
    "1001",
    "PROJECT-2"
  ]
}
```

## Original description

Enables admins to archive up to 1000 issues in a single request using issue ID/key, returning details of the issue(s) archived in the process and the errors encountered, if any.

**Note that:**

 *  you can't archive subtasks directly, only through their parent issues
 *  you can only archive issues from software, service management, and business projects

**[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

**License required:** Premium or Enterprise

**Signed-in users only:** This API can't be accessed anonymously.
