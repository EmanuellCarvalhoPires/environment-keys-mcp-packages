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
path: "/rest/api/3/issue/unarchive"
category: "Issues"
writes_data: true
tool_note: "[[jira_unarchive_issue_s_by_issue_keys_id]]"
---
# Jira v3 - Unarchive issue(s) by issue keys ID

**Unarchive issue(s) by issue keys/ID** — `PUT /rest/api/3/issue/unarchive`

- Run by the tool [[jira_unarchive_issue_s_by_issue_keys_id]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/unarchive
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

Enables admins to unarchive up to 1000 issues in a single request using issue ID/key, returning details of the issue(s) unarchived in the process and the errors encountered, if any.

**Note that:**

 *  you can't unarchive subtasks directly, only through their parent issues
 *  you can only unarchive issues from software, service management, and business projects

**[Permissions](#permissions) required:** Jira admin or site admin: [global permission](https://confluence.atlassian.com/x/x4dKLg)

**License required:** Premium or Enterprise

**Signed-in users only:** This API can't be accessed anonymously.
