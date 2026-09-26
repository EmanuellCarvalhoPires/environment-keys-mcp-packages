---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-email
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project/{projectId}/email"
category: "Project email"
writes_data: true
tool_note: "[[jira_set_project_s_sender_email]]"
---
# Jira v3 - Set project's sender email

**Set project's sender email** — `PUT /rest/api/3/project/{projectId}/email`

- Run by the tool [[jira_set_project_s_sender_email]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project/{{param:projectId}}/email
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectId` (path, string, required) — The project ID.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "emailAddress": "jira@example.atlassian.net"
}
```

## Original description

Sets the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).

If `emailAddress` is an empty string, the default email address is restored.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)
