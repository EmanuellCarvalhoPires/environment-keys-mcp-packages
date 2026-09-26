---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/create
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/issue/{issueIdOrKey}/comment"
category: "Issue comments"
writes_data: true
tool_note: "[[jira_add_comment]]"
---
# Jira v3 - Add comment

**Add comment** — `POST /rest/api/3/issue/{issueIdOrKey}/comment`

- Run by the tool [[jira_add_comment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/comment?expand={{param:expand}}
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `expand` (query, string, optional) — Use expand to include additional information about comments in the response. This parameter accepts renderedBody, which returns the comment body rendered in HTML.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "body": {
    "content": [
      {
        "content": [
          {
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.",
            "type": "text"
          }
        ],
        "type": "paragraph"
      }
    ],
    "type": "doc",
    "version": 1
  },
  "visibility": {
    "identifier": "Administrators",
    "type": "role",
    "value": "Administrators"
  }
}
```

## Original description

Adds a comment to an issue.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* and *Add comments* [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
