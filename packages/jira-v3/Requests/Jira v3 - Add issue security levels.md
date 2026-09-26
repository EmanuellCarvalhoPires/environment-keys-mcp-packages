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
path: "/rest/api/3/issuesecurityschemes/{schemeId}/level"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_add_issue_security_levels]]"
---
# Jira v3 - Add issue security levels

**Add issue security levels** — `PUT /rest/api/3/issuesecurityschemes/{schemeId}/level`

- Run by the tool [[jira_add_issue_security_levels]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuesecurityschemes/{{param:schemeId}}/level
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `schemeId` (path, string, required) — The ID of the issue security scheme.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "levels": [
    {
      "description": "First Level Description",
      "isDefault": true,
      "members": [
        {
          "type": "reporter"
        },
        {
          "parameter": "jira-administrators",
          "type": "group"
        }
      ],
      "name": "First Level"
    }
  ]
}
```

## Original description

Adds levels and levels' members to the issue security scheme. You can add up to 100 levels per request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
