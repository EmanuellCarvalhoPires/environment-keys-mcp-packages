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
path: "/rest/api/3/issuesecurityschemes/level/default"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_set_default_issue_security_levels]]"
---
# Jira v3 - Set default issue security levels

**Set default issue security levels** — `PUT /rest/api/3/issuesecurityschemes/level/default`

- Run by the tool [[jira_set_default_issue_security_levels]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuesecurityschemes/level/default
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "defaultValues": [
    {
      "defaultLevelId": "20000",
      "issueSecuritySchemeId": "10000"
    },
    {
      "defaultLevelId": "30000",
      "issueSecuritySchemeId": "12000"
    }
  ]
}
```

## Original description

Sets default issue security levels for schemes.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
