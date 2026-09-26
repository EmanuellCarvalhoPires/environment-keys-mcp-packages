---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/announcement-banner
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/announcementBanner"
category: "Announcement banner"
writes_data: true
tool_note: "[[jira_update_announcement_banner_configuration]]"
---
# Jira v3 - Update announcement banner configuration

**Update announcement banner configuration** — `PUT /rest/api/3/announcementBanner`

- Run by the tool [[jira_update_announcement_banner_configuration]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/announcementBanner
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "isDismissible": false,
  "isEnabled": true,
  "message": "This is a public, enabled, non-dismissible banner, set using the API",
  "visibility": "public"
}
```

## Original description

Updates the announcement banner configuration.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
