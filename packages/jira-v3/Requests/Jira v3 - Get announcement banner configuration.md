---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/announcement-banner
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/announcementBanner"
category: "Announcement banner"
writes_data: false
tool_note: "[[jira_get_announcement_banner_configuration]]"
---
# Jira v3 - Get announcement banner configuration

**Get announcement banner configuration** — `GET /rest/api/3/announcementBanner`

- Run by the tool [[jira_get_announcement_banner_configuration]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/announcementBanner
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the current announcement banner configuration.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
