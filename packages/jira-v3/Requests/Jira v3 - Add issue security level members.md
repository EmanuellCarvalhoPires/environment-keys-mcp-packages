---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_add_issue_security_level_members]]"
---
# Jira v3 - Add issue security level members

**Add issue security level members** — `PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member`

- Run by the tool [[jira_add_issue_security_level_members]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuesecurityschemes/{{param:schemeId}}/level/{{param:levelId}}/member
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the issue security scheme.
- `levelId` (path, string, required) — The ID of the issue security level.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "members": [
    {
      "type": "reporter"
    },
    {
      "parameter": "jira-administrators",
      "type": "group"
    }
  ]
}
```

## Original description

Adds members to the issue security level. You can add up to 100 members per request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
