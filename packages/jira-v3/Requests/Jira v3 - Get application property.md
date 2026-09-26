---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/jira-settings
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/application-properties"
category: "Jira settings"
writes_data: false
tool_note: "[[jira_get_application_property]]"
---
# Jira v3 - Get application property

**Get application property** — `GET /rest/api/3/application-properties`

- Run by the tool [[jira_get_application_property]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/application-properties?key={{param:key}}&permissionLevel={{param:permissionLevel}}&keyFilter={{param:keyFilter}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `key` (query, string, optional) — The key of the application property.
- `permissionLevel` (query, string, optional) — The permission level of all items being returned in the list.
- `keyFilter` (query, string, optional) — When a key isn't provided, this filters the list of results by the application property key using a regular expression. For example, using jira.lf.

## Original description

Returns all application properties or an application property.

If you specify a value for the `key` parameter, then an application property is returned as an object (not in an array). Otherwise, an array of all editable application properties is returned. See [Set application property](#api-rest-api-3-application-properties-id-put) for descriptions of editable properties.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
