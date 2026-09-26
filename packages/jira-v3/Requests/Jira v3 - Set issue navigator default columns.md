---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-navigator-settings
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
  - api/format/multipart
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/settings/columns"
category: "Issue navigator settings"
writes_data: true
---
# Jira v3 - Set issue navigator default columns

**Set issue navigator default columns** — `PUT /rest/api/3/settings/columns`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Jira v3 - Set issue navigator default columns"`.
- **Format:** the endpoint expects `multipart/form-data` (file upload), which the plugin `http` block cannot build. Kept as reference.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/settings/columns
Authorization: {{service.auth_token}}
```

## Original description

Sets the default issue navigator columns.

The `columns` parameter accepts a navigable field value and is expressed as HTML form data. To specify multiple columns, pass multiple `columns` parameters. For example, in curl:

`curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/settings/columns`

If no column details are sent, then all default columns are removed.

A navigable field is one that can be used as a column on the issue navigator. Find details of navigable issue columns using [Get fields](#api-rest-api-3-field-get).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
