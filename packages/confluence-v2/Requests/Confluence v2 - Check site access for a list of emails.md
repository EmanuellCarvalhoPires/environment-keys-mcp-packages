---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user
  - api/operation/search
  - api/effect/read
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/user/access/check-access-by-email"
category: "User"
writes_data: false
tool_note: "[[confluence_check_site_access_for_a_list_of_emails]]"
---
# Confluence v2 - Check site access for a list of emails

**Check site access for a list of emails** — `POST /user/access/check-access-by-email`

- Run by the tool [[confluence_check_site_access_for_a_list_of_emails]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/user/access/check-access-by-email
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Returns the list of emails from the input list that do not have access to site.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
