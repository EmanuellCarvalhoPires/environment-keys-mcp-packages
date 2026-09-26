---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-type-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move"
category: "Issue type schemes"
writes_data: true
tool_note: "[[jira_change_order_of_issue_types]]"
---
# Jira v3 - Change order of issue types

**Change order of issue types** — `PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move`

- Run by the tool [[jira_change_order_of_issue_types]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuetypescheme/{{param:issueTypeSchemeId}}/issuetype/move
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueTypeSchemeId` (path, string, required) — The ID of the issue type scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "after": "10008",
  "issueTypeIds": [
    "10001",
    "10004",
    "10002"
  ]
}
```

## Original description

Changes the order of issue types in an issue type scheme.

The request body parameters must meet the following requirements:

 *  all of the issue types must belong to the issue type scheme.
 *  either `after` or `position` must be provided.
 *  the issue type in `after` must not be in the issue type list.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
