---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/{issueIdOrKey}/assignee"
category: "Issues"
writes_data: true
tool_note: "[[jira_assign_issue]]"
---
# Jira v3 - Assign issue

**Assign issue** — `PUT /rest/api/3/issue/{issueIdOrKey}/assignee`

- Run by the tool [[jira_assign_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/assignee
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue to be assigned.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "accountId": "5b10ac8d82e05b22cc7d4ef5"
}
```

## Original description

Assigns an issue to a user. Use this operation when the calling user does not have the *Edit Issues* permission but has the *Assign issue* permission for the project that the issue is in.

If `name` or `accountId` is set to:

 *  `"-1"`, the issue is assigned to the default assignee for the project.
 *  `null`, the issue is set to unassigned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse Projects* and *Assign Issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
