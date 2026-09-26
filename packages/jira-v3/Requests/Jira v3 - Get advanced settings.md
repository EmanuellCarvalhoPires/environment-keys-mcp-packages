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
path: "/rest/api/3/application-properties/advanced-settings"
category: "Jira settings"
writes_data: false
tool_note: "[[jira_get_advanced_settings]]"
---
# Jira v3 - Get advanced settings

**Get advanced settings** — `GET /rest/api/3/application-properties/advanced-settings`

- Run by the tool [[jira_get_advanced_settings]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/application-properties/advanced-settings
Authorization: {{service.auth_token}}
Accept: application/json
```

## Original description

Returns the application properties that are accessible on the *Advanced Settings* page. To navigate to the *Advanced Settings* page in Jira, choose the Jira icon > **Jira settings** > **System**, **General Configuration** and then click **Advanced Settings** (in the upper right).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
