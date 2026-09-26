---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-properties
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/properties"
category: "Issue properties"
writes_data: true
tool_note: "[[jira_bulk_set_issues_properties_by_list]]"
---
# Jira v3 - Bulk set issues properties by list

**Bulk set issues properties by list** — `POST /rest/api/3/issue/properties`

- Run by the tool [[jira_bulk_set_issues_properties_by_list]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/properties
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Sets or updates a list of entity property values on issues. A list of up to 10 entity properties can be specified along with up to 10,000 issues on which to set or update that list of entity properties.

The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON. The maximum length of single issue property value is 32768 characters. This operation can be accessed anonymously.

This operation is:

 *  transactional, either all properties are updated in all eligible issues or, when errors occur, no properties are updated.
 *  [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Edit issues* [project permissions](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
