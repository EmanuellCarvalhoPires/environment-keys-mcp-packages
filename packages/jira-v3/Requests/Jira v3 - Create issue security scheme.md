---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issuesecurityschemes"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_create_issue_security_scheme]]"
---
# Jira v3 - Create issue security scheme

**Create issue security scheme** — `POST /rest/api/3/issuesecurityschemes`

- Run by the tool [[jira_create_issue_security_scheme]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issuesecurityschemes
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Newly created issue security scheme",
  "levels": [
    {
      "description": "Newly created level",
      "isDefault": true,
      "members": [
        {
          "parameter": "administrators",
          "type": "group"
        }
      ],
      "name": "New level"
    }
  ],
  "name": "New security scheme"
}
```

## Original description

Creates a security scheme with security scheme levels and levels' members. You can create up to 100 security scheme levels and security scheme levels' members per request.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
