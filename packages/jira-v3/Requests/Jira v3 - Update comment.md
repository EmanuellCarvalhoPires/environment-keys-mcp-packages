---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/issue-comments
  - api/operation/update
  - api/effect/write
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: PUT
path: "/rest/api/3/issue/{issueIdOrKey}/comment/{id}"
category: "Issue comments"
writes_data: true
tool_note: "[[jira_update_comment]]"
---
# Jira v3 - Update comment

**Update comment** — `PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}`

- Run by the tool [[jira_update_comment]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
PUT {{service.url}}/rest/api/3/issue/{{param:issueIdOrKey}}/comment/{{param:id}}?notifyUsers={{param:notifyUsers}}&overrideEditableFlag={{param:overrideEditableFlag}}&expand={{param:expand}}
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `issueIdOrKey` (path, string, required) — The ID or key of the issue.
- `id` (path, string, required) — The ID of the comment.
- `notifyUsers` (query, string, optional) — Whether users are notified when a comment is updated.
- `overrideEditableFlag` (query, string, optional) — Whether screen security is overridden to enable uneditable fields to be edited. Available to Connect app users with the Administer Jira global permission and Forge apps acting on behalf of users with…
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

Updates a comment.

This operation can be accessed anonymously.

**[Permissions](#permissions) required:**

 *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue containing the comment is in.
 *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
 *  *Edit all comments*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any comment or *Edit own comments* to update comment created by the user.
 *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.

**WARNING:** Child comments inherit visibility from their parent comment. Attempting to update a child comment's visibility will result in a 400 (Bad Request) error.
