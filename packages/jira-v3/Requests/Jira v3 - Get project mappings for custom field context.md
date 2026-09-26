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
path: "/rest/api/3/field/{fieldId}/context/projectmapping"
category: "Issue custom field contexts"
writes_data: false
tool_note: "[[jira_get_project_mappings_for_custom_field_context]]"
---
# Jira v3 - Get project mappings for custom field context

**Get project mappings for custom field context** — `GET /rest/api/3/field/{fieldId}/context/projectmapping`

- Run by the tool [[jira_get_project_mappings_for_custom_field_context]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/context/projectmapping?contextId={{param:contextId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field, for example customfield\10000.
- `contextId` (query, string, optional) — The list of context IDs. To include multiple context, separate IDs with ampersand: contextId=10000&contextId=10001.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of context to project mappings for a custom field. The result can be filtered by `contextId`. Otherwise, all mappings are returned. Invalid IDs are ignored.

**Note:** Jira is adding support for multiple field contexts per project. On sites where this is enabled, a custom field can have more than one context associated with the same project, so this operation can return several mappings that share the same `projectId`, each with a different `contextId`. Do not assume that a project appears at most once in the response. See [CHANGE-3082](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-3082) for more details.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
