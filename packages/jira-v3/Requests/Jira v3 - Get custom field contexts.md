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
path: "/rest/api/3/field/{fieldId}/context"
category: "Issue custom field contexts"
writes_data: false
tool_note: "[[jira_get_custom_field_contexts]]"
---
# Jira v3 - Get custom field contexts

**Get custom field contexts** — `GET /rest/api/3/field/{fieldId}/context`

- Run by the tool [[jira_get_custom_field_contexts]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
GET {{service.url}}/rest/api/3/field/{{param:fieldId}}/context?isAnyIssueType={{param:isAnyIssueType}}&isGlobalContext={{param:isGlobalContext}}&contextId={{param:contextId}}&startAt={{param:startAt}}&maxResults={{param:maxResults}}
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `fieldId` (path, string, required) — The ID of the custom field.
- `isAnyIssueType` (query, string, optional) — Whether to return contexts that apply to all issue types.
- `isGlobalContext` (query, string, optional) — Whether to return contexts that apply to all projects.
- `contextId` (query, string, optional) — The list of context IDs. To include multiple contexts, separate IDs with ampersand: contextId=10000&contextId=10001.
- `startAt` (query, string, optional) — The index of the first item to return in a page of results (page offset).
- `maxResults` (query, string, optional) — The maximum number of items to return per page.

## Original description

Returns a [paginated](#pagination) list of [ contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html) for a custom field. Contexts can be returned as follows:

 *  With no other parameters set, all contexts.
 *  By defining `id` only, all contexts from the list of IDs.
 *  By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to all issue types (true) or those that apply to only a subset of issue types (false)
 *  By defining `isGlobalContext`, limit the list of contexts return to either those that apply to all projects (global contexts) (true) or those that apply to only a subset of projects (false).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). *Edit Workflow* [edit workflow permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/#Edit-Workflows)
