---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/project-features
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/project/{projectIdOrKey}/features/{featureKey}"
category: "Project features"
writes_data: true
tool_note: "[[jira_set_project_feature_state]]"
---
# Jira v3 - Set project feature state

**Set project feature state** — `PUT /rest/api/3/project/{projectIdOrKey}/features/{featureKey}`

- Run by the tool [[jira_set_project_feature_state]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/project/{{param:projectIdOrKey}}/features/{{param:featureKey}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `projectIdOrKey` (path, string, required) — The ID or (case-sensitive) key of the project.
- `featureKey` (path, string, required) — The key of the feature.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "state": "ENABLED"
}
```

## Original description

Sets the state of a project feature.
