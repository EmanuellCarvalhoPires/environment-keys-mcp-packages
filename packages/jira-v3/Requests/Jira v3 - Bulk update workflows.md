---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/workflows
  - api/operation/action
  - api/effect/write
  - api/permission/project-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/workflows/update"
category: "Workflows"
writes_data: true
tool_note: "[[jira_bulk_update_workflows]]"
---
# Jira v3 - Bulk update workflows

**Bulk update workflows** — `POST /rest/api/3/workflows/update`

- Run by the tool [[jira_bulk_update_workflows]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/workflows/update
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "statuses": [
    {
      "description": "",
      "name": "To Do",
      "statusCategory": "TODO",
      "statusReference": "f0b24de5-25e7-4fab-ab94-63d81db6c0c0"
    },
    {
      "description": "",
      "name": "In Progress",
      "statusCategory": "IN_PROGRESS",
      "statusReference": "c7a35bf0-c127-4aa6-869f-4033730c61d8"
    },
    {
      "description": "",
      "name": "Done",
      "statusCategory": "DONE",
      "statusReference": "6b3fc04d-3316-46c5-a257-65751aeb8849"
    }
  ],
  "workflows": [
    {
      "defaultStatusMappings": [
        {
          "newStatusReference": "10011",
          "oldStatusReference": "10010"
        }
      ],
      "description": "",
      "id": "10001",
      "startPointLayout": {
        "x": -100.00030899047852,
        "y": -153.00020599365234
      },
      "statusMappings": [
        {
          "issueTypeId": "10002",
          "projectId": "10003",
          "statusMigrations": [
            {
              "newStatusReference": "10011",
              "oldStatusReference": "10010"
            }
          ]
        }
      ],
      "statuses": [
        {
          "layout": {
            "x": 114.99993896484375,
            "y": -16
          },
          "properties": {},
          "statusReference": "f0b24de5-25e7-4fab-ab94-63d81db6c0c0"
        },
        {
          "layout": {
            "x": 317.0000915527344,
            "y": -16
          },
          "properties": {},
          "statusReference": "c7a35bf0-c127-4aa6-869f-4033730c61d8"
        },
        {
          "layout": {
            "x": 508.000244140625,
            "y": -16
          },
          "properties": {},
          "statusReference": "6b3fc04d-3316-46c5-a257-65751aeb8849"
        }
      ],
      "transitions": [
        {
          "actions": [],
          "description": "",
          "id": "1",
          "links": [],
          "name": "Create",
          "properties": {},
          "toStatusReference": "f0b24de5-25e7-4fab-ab94-63d81db6c0c0",
          "triggers": [],
          "type": "INITIAL",
          "validators": []
        },
        {
          "actions": [],
          "description": "",
          "id": "11",
          "links": [],
          "name": "To Do",
          "properties": {},
          "toStatusReference": "f0b24de5-25e7-4fab-ab94-63d81db6c0c0",
          "triggers": [],
          "type": "GLOBAL",
          "validators": []
        },
        {
          "actions": [],
          "description": "",
          "id": "21",
          "links": [],
          "name": "In Progress",
          "properties": {},
          "toStatusReference": "c7a35bf0-c127-4aa6-869f-4033730c61d8",
          "triggers": [],
          "type": "GLOBAL",
          "validators": []
        },
        {
          "actions": [],
          "description": "Move a work item from in progress to done",
          "id": "31",
          "links": [
            {
              "fromPort": 0,
              "fromStatusReference": "c7a35bf0-c127-4aa6-869f-4033730c61d8",
              "toPort": 1
            }
          ],
          "name": "Done",
          "properties": {},
          "toStatusReference": "6b3fc04d-3316-46c5-a257-65751aeb8849",
          "triggers": [],
          "type": "DIRECTED",
          "validators": []
        }
      ],
      "version": {
        "id": "6f6c988b-2590-4358-90c2-5f7960265592",
        "versionNumber": 1
      }
    }
  ]
}
```

## Original description

Update workflows and related statuses.

**[Permissions](#permissions) required:**

 *  *Administer Jira* project permission to create all, including global-scoped, workflows
 *  *Administer projects* project permissions to create project-scoped workflows
