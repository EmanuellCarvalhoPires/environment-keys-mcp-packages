---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/action
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/{issueIdOrKey}/transitions"
category: "Issues"
writes_data: true
tool_note: "[[jira_transition_issue]]"
---
# Jira v3 - Transition issue

**Transition issue** — `POST /rest/api/3/issue/{issueIdOrKey}/transitions`

- Run by the tool [[jira_transition_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/transitions
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "fields": {
    "assignee": {
      "name": "bob"
    },
    "resolution": {
      "name": "Fixed"
    }
  },
  "historyMetadata": {
    "activityDescription": "Complete order processing",
    "actor": {
      "avatarUrl": "http://mysystem/avatar/tony.jpg",
      "displayName": "Tony",
      "id": "tony",
      "type": "mysystem-user",
      "url": "http://mysystem/users/tony"
    },
    "cause": {
      "id": "myevent",
      "type": "mysystem-event"
    },
    "description": "From the order testing process",
    "extraData": {
      "Iteration": "10a",
      "Step": "4"
    },
    "generator": {
      "id": "mysystem-1",
      "type": "mysystem-application"
    },
    "type": "myplugin:type"
  },
  "transition": {
    "id": "5"
  },
  "update": {
    "comment": [
      {
        "add": {
          "body": {
            "content": [
              {
                "content": [
                  {
                    "text": "Bug has been fixed",
                    "type": "text"
                  }
                ],
                "type": "paragraph"
              }
            ],
            "type": "doc",
            "version": 1
          }
        }
      }
    ]
  }
}
```

## Original description

Performs an issue transition and, if the transition has a screen, updates the fields from the transition screen.

sortByCategory To update the fields on the transition screen, specify the fields in the `fields` or `update` parameters in the request body. Get details about the fields using [ Get transitions](#api-rest-api-3-issue-issueIdOrKey-transitions-get) with the `transitions.fields` expand.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Transition issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
