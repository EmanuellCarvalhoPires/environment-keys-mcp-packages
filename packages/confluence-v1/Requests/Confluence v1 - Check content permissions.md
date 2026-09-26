---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/content-permissions
  - api/operation/search
  - api/effect/read
  - api/version/v1
  - api/permission/global-admin
up: "[[MCP - Confluence v1]]"
app: "Confluence v1"
method: POST
path: "/wiki/rest/api/content/{id}/permission/check"
category: "Content permissions"
writes_data: false
tool_note: "[[confluence_v1_check_content_permissions]]"
---
# Confluence v1 - Check content permissions

**Check content permissions** — `POST /wiki/rest/api/content/{id}/permission/check`

- Run by the tool [[confluence_v1_check_content_permissions]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v1/

```http
POST {{service.url}}/wiki/rest/api/content/{{param:id}}/permission/check
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `id` (path, string, required) — The ID of the content to check permissions against.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Check if a user or a group can perform an operation to the specified content. The `operation` to check
must be provided. The user’s account ID or the ID of the group can be provided in the `subject` to check
permissions against a specified user or group. The following permission checks are done to make sure that the
user or group has the proper access:

- site permissions
- space permissions
- content restrictions

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission) if checking permission for self,
otherwise 'Confluence Administrator' global permission is required.
