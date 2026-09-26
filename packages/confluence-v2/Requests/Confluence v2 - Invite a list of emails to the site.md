---
tags:
  - api/request
  - api/service/atlassian
  - api/app/confluence
  - api/resource/user
  - api/operation/create
  - api/effect/write
  - api/version/v2
up: "[[MCP - Confluence v2]]"
app: "Confluence v2"
method: POST
path: "/user/access/invite-by-email"
category: "User"
writes_data: true
tool_note: "[[confluence_invite_a_list_of_emails_to_the_site]]"
---
# Confluence v2 - Invite a list of emails to the site

**Invite a list of emails to the site** — `POST /user/access/invite-by-email`

- Run by the tool [[confluence_invite_a_list_of_emails_to_the_site]].
- Official documentation: https://developer.atlassian.com/cloud/confluence/rest/v2/

```http
POST {{service.url}}/wiki/api/v2/user/access/invite-by-email
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Invite a list of emails to the site.

Ignores all invalid emails and no action is taken for the emails that already have access to the site.

NOTE: This API is asynchronous and may take some time to complete.

**[Permissions](https://confluence.atlassian.com/x/_AozKw) required**:
Permission to access the Confluence site ('Can use' global permission).
