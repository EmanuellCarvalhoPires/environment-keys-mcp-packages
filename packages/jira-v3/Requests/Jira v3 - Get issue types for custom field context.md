---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-custom-field-contexts
  - api/operation/list
  - api/effect/read
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: GET
path: "/rest/api/3/field/{fieldId}/context/issuetypemapping"
category: "Issue custom field contexts"
writes_data: false
tool_note: "[[jira_get_issue_types_for_custom_field_context]]"
---
# Jira v3 - Get issue types for custom field context

**Get issue types for custom field context** — `GET /rest/api/3/field/{fieldId}/context/issuetypemapping`

- Run by the tool [[jira_get_issue_types_for_custom_field_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/issuetypemapping?contextId={{param:contextId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `contextId` (query, string, optional) — The ID of the context. To include multiple contexts, provide an ampersand-separated list. For example, contextId=10001&contextId=10002.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of context to issue type mappings for a custom field. Mappings are returned for all contexts or a list of contexts. Mappings are ordered first by context ID and then by issue type ID.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
