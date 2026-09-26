---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-options-apps
  - api/operation/search
  - api/effect/read
  - api/restriction/app-connect
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/{fieldKey}/option/suggestions/search"
category: "Issue custom field options (apps)"
writes_data: false
---
# Jira v3 - Get visible issue field options

**Get visible issue field options** — `GET /rest/api/3/field/{fieldKey}/option/suggestions/search`

- No dedicated tool: run it with `atlassian_request_read` passing `request:"Jira v3 - Get visible issue field options"`.
- **Restriction:** the documentation says only Connect/Forge apps can call this endpoint; a user token is expected to be rejected.
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldKey}}/option/suggestions/search?startAt={{param:startAt}}&maxResults={{param:maxResults}}&projectId={{param:projectId}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldKey` (path, string, required) — The field key is specified in the following format: $(app-key)\\$(field-key). For example, example-add-on\\example-issue-field.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.
- `projectId` (query, string, optional) — Filters the results to options that are only available in the specified project.

## Original description

Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed by the user.

Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.

**[Permissions](#permissions) required:** Permission to access Jira.
