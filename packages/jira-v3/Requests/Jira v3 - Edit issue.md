---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issues
  - api/operation/update
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/{issueIdOrKey}"
category: "Issues"
writes_data: true
tool_note: "[[jira_edit_issue]]"
---
# Jira v3 - Edit issue

**Edit issue** — `PUT /rest/api/3/issue/{issueIdOrKey}`

- Run by the tool [[jira_edit_issue]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}?notifyUsers={{param:notifyUsers}}&overrideScreenSecurity={{param:overrideScreenSecurity}}&overrideEditableFlag={{param:overrideEditableFlag}}&returnIssue={{param:returnIssue}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `notifyUsers` (query, string, optional) — Whether a notification email about the issue update is sent to all watchers. To disable the notification, administer Jira or administer project permissions are required.
- `overrideScreenSecurity` (query, string, optional) — Whether screen security is overridden to enable hidden fields to be edited. Available to Connect and Forge app users with Administer Jira global permission and Forge apps acting on behalf of users wit…
- `overrideEditableFlag` (query, string, optional) — Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect and Forge app users with Administer Jira global permission and Forge apps acting on behalf of users…
- `returnIssue` (query, string, optional) — Whether the response should contain the issue with fields edited in this request. The returned issue will have the same format as in the Get issue API.
- `expand` (query, string, optional) — The Get issue API expand parameter to use in the response if the returnIssue parameter is true.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "fields": {
    "customfield_10000": {
      "content": [
        {
          "content": [
            {
              "text": "Investigation underway",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "customfield_10010": 1,
    "summary": "Completed orders still displaying in pending"
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
  "properties": [
    {
      "key": "key1",
      "value": "Order number 10784"
    },
    {
      "key": "key2",
      "value": "Order number 10923"
    }
  ],
  "update": {
    "components": [
      {
        "set": ""
      }
    ],
    "labels": [
      {
        "add": "triaged"
      },
      {
        "remove": "blocker"
      }
    ],
    "summary": [
      {
        "set": "Bug in business logic"
      }
    ],
    "timetracking": [
      {
        "edit": {
          "originalEstimate": "1w 1d",
          "remainingEstimate": "4d"
        }
      }
    ]
  }
}
```

## Original description

Edits an issue. Issue properties may be updated as part of the edit. Please note that issue transition is not supported and is ignored here. To transition an issue, please use [Transition issue](#api-rest-api-3-issue-issueIdOrKey-transitions-post).

The edits to the issue's fields are defined using `update` and `fields`. The fields that can be edited are determined using [ Get edit issue metadata](#api-rest-api-3-issue-issueIdOrKey-editmeta-get).

**Note:** This endpoint doesn't check screen configurations to determine if a field is editable. For more context, see the [Deprecation of override screen security](https://community.developer.atlassian.com/t/deprecation-of-override-screen-security/97153) announcement.

The parent field may be set by key or ID. For standard issue types, the parent may be removed by setting `update.parent.set.none` to *true*. Note that the `description`, `environment`, and any `textarea` type custom fields (multi-line text fields) take Atlassian Document Format content. Single line custom fields (`textfield`) accept a string and don't handle Atlassian Document Format content.

Connect apps having an app user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can override the screen security configuration using `overrideScreenSecurity` and `overrideEditableFlag`.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
