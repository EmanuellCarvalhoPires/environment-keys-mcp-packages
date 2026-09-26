---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/myself
  - api/operation/list
  - api/effect/read
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/mypreferences/locale"
category: "Myself"
writes_data: false
tool_note: "[[jira_get_locale]]"
---
# Jira v3 - Get locale

**Get locale** — `GET /rest/api/3/mypreferences/locale`

- Run by the tool [[jira_get_locale]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/mypreferences/locale
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the locale for the user.

If the user has no language preference set (which is the default setting) or this resource is accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale using the *Accept-Language* header in the request. However, if this doesn't match a locale available Jira, the site default locale is returned.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:** None.
