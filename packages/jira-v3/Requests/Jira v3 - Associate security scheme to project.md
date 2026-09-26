---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-security-schemes
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issuesecurityschemes/project"
category: "Issue security schemes"
writes_data: true
tool_note: "[[jira_associate_security_scheme_to_project]]"
---
# Jira v3 - Associate security scheme to project

**Associate security scheme to project** — `PUT /rest/api/3/issuesecurityschemes/project`

- Run by the tool [[jira_associate_security_scheme_to_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issuesecurityschemes/project
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "oldToNewSecurityLevelMappings": [
    {
      "newLevelId": "30001",
      "oldLevelId": "30000"
    }
  ],
  "projectId": "10000",
  "schemeId": "20000"
}
```

## Original description

Associates an issue security scheme with a project and remaps security levels of issues to the new levels, if provided.

This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates.

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
